package com.bda;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.apache.beam.runners.dataflow.DataflowRunner;
import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
import org.apache.beam.runners.direct.DirectRunner;
import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.coders.CoderRegistry;
import org.apache.beam.sdk.io.TextIO;
import org.apache.beam.sdk.options.Default;
import org.apache.beam.sdk.options.Description;
import org.apache.beam.sdk.options.PipelineOptionsFactory;
import org.apache.beam.sdk.options.Validation;
import org.apache.beam.sdk.transforms.GroupByKey;
import org.apache.beam.sdk.transforms.MapElements;
import org.apache.beam.sdk.transforms.ParDo;
import org.apache.beam.sdk.values.KV;
import org.apache.beam.sdk.values.PCollection;
import org.apache.beam.sdk.values.TypeDescriptors;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.bda.coders.BandBucketCoder;
import com.bda.operations.BandHasher;
import com.bda.operations.DocumentSource;
import com.bda.operations.MinHasher;
import com.bda.operations.ReduceCandidates;
import com.bda.operations.ShingleExtractor;
import com.bda.operations.SplitInBands;

public class PlagiarismPipeline {
	private static final Logger LOG = LoggerFactory.getLogger(PlagiarismPipeline.class);

	private static final boolean RUN_LOCAL = true;
	
	public interface PlagiarismPipelineOptions extends DataflowPipelineOptions {
		@Description("Shingle size")
		@Validation.Required
		@Default.Integer(7)
		int getKFactor();
		void setKFactor(int value);
		
		@Description("Amount of permutations in Signature Matrix")
		@Validation.Required
		@Default.Integer(100)
		int getPermutationCount();
		void setPermutationCount(int value);
		
	    @Description("Amount of bands")
	    @Validation.Required
	    @Default.Integer(20)
	    int getBandsCount();
	    void setBandsCount(int value);
	    
	    @Description("Input files")
	    @Validation.Required
	    @Default.String("gs://uhasselt-bda/tokens/*")
	    String getInput();
	    void setInput(String value);
	    
	    @Description("Output prefix")
	    @Validation.Required
	    @Default.String("gs://bda-plagiarism-temp/output/")
	    String getOutputPrefix();
	    void setOutputPrefix(String value);
	    
		@Description("Whether to write intermediary results to files")
		@Validation.Required
		@Default.Boolean(false)
		boolean getWriteTempOutput();
		void setWriteTempOutput(boolean value);
	}
	
	public static void main(String[] args) {		
		// Init options
		PlagiarismPipelineOptions options = PipelineOptionsFactory
			.fromArgs(args)
			.withValidation()
			.create()
			.as(PlagiarismPipelineOptions.class);
		
		options.setJobName("bda-plagiarism");
        options.setProject("bda-demo-258112");
		options.setTempLocation("gs://bda-plagiarism-temp/temp");
		options.setGcpTempLocation("gs://bda-plagiarism-temp/temp");
        options.setRegion("europe-west1");
        options.setZone("europe-west1-b");
        options.setWorkerMachineType("n1-standard-1");
        options.setRunner(DataflowRunner.class);
        options.setStreaming(false);
        options.setUpdate(true);
        options.setDataflowJobFile("gs://bda-plagiarism-temp/temp/bda-plagiarism.json");
        
		if (RUN_LOCAL) {
			options.setRunner(DirectRunner.class);
			options.setInput("gs://uhasselt-bda/tokens/2126807.txt");
			options.setOutputPrefix("output/");
			options.setWriteTempOutput(true);
		}
		
		// Init pipeline
		Pipeline p = Pipeline.create(options);

		CoderRegistry cr = p.getCoderRegistry();
		cr.registerCoderForType(TypeDescriptors.kvs(TypeDescriptors.integers(), 
													TypeDescriptors.maps(TypeDescriptors.strings(), TypeDescriptors.lists(TypeDescriptors.longs()))), 
								 new BandBucketCoder());
		
		// Build pipeline
		
		// Step 1: Prepare = (fileid, file_contents) pairs
		PCollection<KV<Long, String>> inputs = 
				(new DocumentSource(options.getInput()))
				.expand(p.begin());
		
		// Step 2: Shingling = (fileid, file_contents) => (fileid, [shingle_hashes])
		PCollection<KV<Long, Set<String>>> shingle_sets = 
				inputs.apply("Extract shingles",  
							 MapElements.via(new ShingleExtractor(options.getKFactor())));
		if (options.getWriteTempOutput()) { 
			// Tmp output
			shingle_sets.apply("Write temp multiset output",
	                MapElements.into(TypeDescriptors.strings())
	                    .via(
	                        (KV<Long, Set<String>> multiset) ->
	                        	multiset.getKey() + ": " + multiset.getValue().toString()))
	            .apply(TextIO.write().to(options.getOutputPrefix() + "1_multisets"));
		}
		
		// Step 3: Minhashing = (fileid, [shingle_hashes]) => (filename, [signature_matrix_col])
		PCollection<KV<Long, String[]>> signature_matrix =
				shingle_sets.apply("Minhashing",
								   MapElements.via(new MinHasher(options.getPermutationCount())));
		
		if (options.getWriteTempOutput()) { 
			// Tmp output
			signature_matrix.apply("Write temp SigMat output",
	                MapElements.into(TypeDescriptors.strings())
	                    .via(
	                        (KV<Long, String[]> sigm) ->
	                        	sigm.getKey() + ": " + Arrays.toString(sigm.getValue())))
	            .apply(TextIO.write().to(options.getOutputPrefix() + "2_sigmatr"));
		}
		
		// Step 4: LSH prepare = (filename, [signature_matrix_col]) => (band, [(filename, [signature_matrix_band])])
		PCollection<KV<Integer, Iterable<KV<Long, String[]>>>> by_band =
				signature_matrix.apply("Divide SigMat in bands",
									   ParDo.of(new SplitInBands(options.getBandsCount())))
				.apply("Group by band id", GroupByKey.create());
		
		if (options.getWriteTempOutput()) { 
			// Tmp output
			by_band.apply("Write temp band output",
	                MapElements.into(TypeDescriptors.strings())
	                    .via(
	                        (KV<Integer, Iterable<KV<Long, String[]>>> band) -> {
	                        	List<String> list = new ArrayList<String>();
	                        	
	                        	band.getValue().forEach((KV<Long, String[]> sigm) ->
			                			list.add(String.format("(%d: %s)", 
			 					                               sigm.getKey(), 
			 					                               Arrays.toString(sigm.getValue()))));
	                        	
	                        	return String.format("%d: %s", band.getKey(), list.toString());
	                        }))
	            .apply(TextIO.write().to(options.getOutputPrefix() + "3_band"));
		}
		
		// Step 5: LSH = (band, [(filename, [signature_matrix_band])]) => (band, buckets: [file_names])
		PCollection<KV<Integer, Map<String, List<Long>>>> buckets =
				by_band.apply("LSH every band into buckets",
							  MapElements.via(new BandHasher()))
				.setCoder(new BandBucketCoder());
		
		if (options.getWriteTempOutput()) { 
			// Tmp output
			buckets.apply("Write temp bucket output",
	                MapElements.into(TypeDescriptors.strings())
	                    .via(
	                        (KV<Integer, Map<String, List<Long>>> bucket) -> {
	                        	List<String> list = new ArrayList<String>();
	                        	
	                        	bucket.getValue().forEach((k, v) -> 
	                        			list.add(String.format("(%s: %s)", k, v.toString())));
	             
	                        	return String.format("%d: %s", bucket.getKey(), list.toString());
	                        })
	                    )
	            .apply(TextIO.write().to(options.getOutputPrefix() + "4_buckets"));
		}
		
		// Step 6: Reduce = (band, buckets: [file_names]) => (file_name, candidates: [files])
//		PCollection<KV<Long, Set<Long>>> candidates = 
			buckets.apply("Create candidates", ParDo.of(new ReduceCandidates()))
				   .apply("Group by filename", GroupByKey.create())
				   .apply("Flatten candidates", 
						   MapElements.into(TypeDescriptors.kvs(TypeDescriptors.longs(), TypeDescriptors.sets(TypeDescriptors.longs())))
						   .via(input -> {
							   Set<Long> merged = new HashSet<Long>();
							   input.getValue().forEach(li -> merged.addAll((List<Long>)li));
							   return KV.of(input.getKey(), merged);
						   }))
		
		// Step 7: Output
			.apply("Write candidate pairs to output",
				   MapElements.into(TypeDescriptors.strings())
				   .via((KV<Long, Set<Long>> cand) -> {
					   return String.format("%d: %s", cand.getKey(), cand.getValue().toString());
	               }))
            .apply(TextIO.write().to(options.getOutputPrefix() + "5_candidates"));	   
		
		
		LOG.info("-- START RUN --");
		// To run, build and go to:
        //  https://console.cloud.google.com/dataflow?project=bda-demo-258112
        // And ceate a new job. Select "bda-plagiarism-temp/temp/bda-plagiarism.json" as template.
        // Output artefacts can be found at:
        //  https://console.cloud.google.com/storage/browser/bda-plagiarism-temp/output?project=bda-demo-258112
		p.run().waitUntilFinish();
		LOG.info("-- COMPLETE --");
	}
}
