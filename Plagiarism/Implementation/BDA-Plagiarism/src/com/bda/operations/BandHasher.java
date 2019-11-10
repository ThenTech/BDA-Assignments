package com.bda.operations;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.beam.sdk.transforms.SimpleFunction;
import org.apache.beam.sdk.values.KV;
import org.apache.commons.codec.digest.DigestUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public class BandHasher extends SimpleFunction<KV<Integer, Iterable<KV<Long, String[]>>>, KV<Integer, Map<String, List<Long>>>>{
	private static final long serialVersionUID = 7758026036612994809L;
	private static final Logger LOG = LoggerFactory.getLogger(BandHasher.class);

	public BandHasher() {
		
	}
	
	public KV<Integer, Map<String, List<Long>>> apply(KV<Integer, Iterable<KV<Long, String[]>>> band) {
		Map<String, List<Long>> bucket = new HashMap<String, List<Long>>();
		
		band.getValue().forEach((file) -> this.hash_file_band(file, bucket));
		
//		List<String> maplist = new ArrayList<String>();
//		bucket.forEach((k, v) -> maplist.add(String.format("(%s: %s)", k, v.toString())));
//		LOG.info("{}: {}", band.getKey(), maplist.toString());
		
		return KV.of(band.getKey(), bucket);
	}
	
	private void hash_file_band(KV<Long, String[]> file, Map<String, List<Long>> bucket) {
		final String key = DigestUtils.md5Hex(Arrays.toString(file.getValue()));
		
		if (!bucket.containsKey(key)) {
			bucket.put(key, new ArrayList<>());
		}
		
		bucket.get(key).add(file.getKey());
	}
}
