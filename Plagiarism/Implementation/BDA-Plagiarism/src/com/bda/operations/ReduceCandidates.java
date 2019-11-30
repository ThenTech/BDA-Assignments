package com.bda.operations;

import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.apache.beam.sdk.transforms.DoFn;

import org.apache.beam.sdk.values.KV;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ReduceCandidates extends DoFn<KV<Integer, Map<String, List<Long>>>, KV<Long, Iterable<Long>>> {
	private static final long serialVersionUID = 7209890248343962926L;
	private static final Logger LOG = LoggerFactory.getLogger(ReduceCandidates.class);

	public ReduceCandidates() {

	}

	@ProcessElement
	public void processElement(@Element KV<Integer, Map<String, List<Long>>> bucket, OutputReceiver<KV<Long, Iterable<Long>>> out) {
        // Create new candidate pairs by adding each file with
        // a list of the other files in the same bucket together.

        bucket.getValue().forEach(
			(String bhash, List<Long> files) -> {
				if (files.size() > 1) {
					for (Long file : files) {
                        // Create unique set of all files in the bucket
						Set<Long> distinct = new HashSet<Long>();
                        distinct.addAll(files);

                        // Remove the current file
                        distinct.remove(file);

                        // Add as candidate pairing list.
						out.output(KV.of(file, distinct));
					}
				}
		});
	}
}
