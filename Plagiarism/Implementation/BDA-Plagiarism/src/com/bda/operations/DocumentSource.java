package com.bda.operations;

import org.apache.beam.sdk.io.FileIO;
import org.apache.beam.sdk.io.FileIO.ReadableFile;
import org.apache.beam.sdk.transforms.MapElements;
import org.apache.beam.sdk.transforms.PTransform;
import org.apache.beam.sdk.transforms.SimpleFunction;
import org.apache.beam.sdk.values.KV;
import org.apache.beam.sdk.values.PBegin;
import org.apache.beam.sdk.values.PCollection;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Created by Laurens on 8/10/19.
 */
public class DocumentSource extends PTransform<PBegin, PCollection<KV<Long, String>>> {
    private static final long serialVersionUID = -5780401297085502944L;
    private static final Logger LOG = LoggerFactory.getLogger(DocumentSource.class);

    private final String inputDirectory;

    public DocumentSource(String inputDirectory) {
        this.inputDirectory = inputDirectory;
    }

    @Override
    public PCollection<KV<Long, String>> expand(PBegin input) {
        return input
                .apply("List files", FileIO.match().filepattern(inputDirectory))
                .apply("Get matches", FileIO.readMatches())
                .apply("Extrace document contents", MapElements.via(new DocumentExtractor()));
    }

    private static class DocumentExtractor extends SimpleFunction<ReadableFile, KV<Long, String>> {
        private static final long serialVersionUID = 811354739510796727L;

        public KV<Long, String> apply(ReadableFile file) {
            try {
            	String filename = file.getMetadata().resourceId().getFilename();
            	String contents = file.readFullyAsUTF8String();

//                LOG.info("{}, {}", filename, contents);

                // Simply use the filename as the ID
                return KV.of(Long.parseLong(resolveFileName(filename)), contents);
            } catch (Exception e) {
                throw new RuntimeException("[ERROR]: Parsing ReadableFile to Document on "
            			+ file.getMetadata().resourceId()
						+ ".\n" + e.toString());
            }
        }

        private String resolveFileName(String fileName) {
            return fileName.contains(".")
        		 ? fileName.split("\\.")[0]
        		 : fileName;
        }
    }
}
