package com.bda;

import java.util.Arrays;

import org.apache.beam.runners.dataflow.options.DataflowPipelineOptions;
import org.apache.beam.runners.direct.DirectRunner;
import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.io.TextIO;
import org.apache.beam.sdk.options.PipelineOptions;
import org.apache.beam.sdk.options.PipelineOptionsFactory;
import org.apache.beam.sdk.transforms.Count;
import org.apache.beam.sdk.transforms.Filter;
import org.apache.beam.sdk.transforms.FlatMapElements;
import org.apache.beam.sdk.transforms.MapElements;
import org.apache.beam.sdk.transforms.ParDo;
import org.apache.beam.sdk.values.KV;
import org.apache.beam.sdk.values.PCollection;
import org.apache.beam.sdk.values.TypeDescriptors;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.bda.operations.DocumentSource;

public class PlagiarismPipeline {
	private static final Logger LOG = LoggerFactory.getLogger(PlagiarismPipeline.class);
	
	public static void main(String[] args) {
		// Init options
		DataflowPipelineOptions options = PipelineOptionsFactory
			.fromArgs(args)
			.withValidation()
			.create()
			.as(DataflowPipelineOptions.class);

		options.setJobName("BDA-Plagiarism");
        options.setProject("bda-demo-258112");
//		options.setTempLocation("");
        options.setRegion("europe-west1");
        options.setZone("europe-west1-b");
        options.setWorkerMachineType("n1-standard-1");
        options.setRunner(DirectRunner.class);	// DataflowRunner.class
        options.setUpdate(true);
        

		// Init pipeline
		Pipeline p = Pipeline.create(options);
		
		// Build pipeline
		PCollection<KV<Long, String>> inputs = 
				(new DocumentSource("gs://uhasselt-bda/tokens/*"))
				.expand(p.begin());
		
//		inputs.apply(...);

		p.run().waitUntilFinish();
	}
}
