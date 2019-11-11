package com.bda.operations;

import java.security.MessageDigest;
import java.util.Set;

import org.apache.beam.sdk.transforms.SimpleFunction;
import org.apache.beam.sdk.values.KV;
import org.apache.commons.codec.binary.Hex;
import org.apache.commons.codec.binary.StringUtils;
import org.apache.commons.codec.digest.DigestUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class MinHasher extends SimpleFunction<KV<Long, Set<String>>, KV<Long, String[]>>{
	private static final long serialVersionUID = -8133460251058951811L;
	private static final Logger LOG = LoggerFactory.getLogger(MinHasher.class);

	private int n_permutations;
	private MessageDigest hashf;
	private byte[][] pHash_LUT;

	public MinHasher(int n_permutations) {
		this.n_permutations = n_permutations;
		this.hashf = DigestUtils.getMd5Digest();
		this.pHash_LUT = new byte[this.n_permutations][];

		for (int pHash = 0; pHash < this.n_permutations; pHash++) {
			this.pHash_LUT[pHash] = StringUtils.getBytesUtf8(String.valueOf(pHash));
		}
	}

	private String getHash(int permutation, String value) {
		this.hashf.update(this.pHash_LUT[permutation]);
		final byte[] result = this.hashf.digest(StringUtils.getBytesUtf8(value));
		return Hex.encodeHexString(result);
	}

	public KV<Long, String[]> apply(KV<Long, Set<String>> multiset) {
		String[] SM = new String[this.n_permutations];

        // For each hashed shingle in the file's multiset
		for (String hashed_shingle : multiset.getValue()) {
            // Enumerate over every possible permutation hash
			for (int pHash = 0; pHash < this.n_permutations; pHash++) {
                // Rehash the shingle with the current permutation
				final String hashed_value = this.getHash(pHash, hashed_shingle);

                // Replace in SignMatr if the current permutation rehash is smaller
                // This Minhashing works because the SM would only be updated when a
                // new hash is smaller and only on elements in the binvector on a value of `1`.
                // Since only those exact values are per definition included in the
                // multiset, iterating over the multiset itself is the best way of
                // doing this. The multiset is a subset of the entire shingle hash domain
                // that only includes bitvector values of `1`.
				if (SM[pHash] == null || hashed_value.compareTo(SM[pHash]) < 0) {
					SM[pHash] = hashed_value;
				}
			}
		}

//		LOG.info("{}: {}", multiset.getKey(), Arrays.toString(SM));

		return KV.of(multiset.getKey(), SM);
	}
}
