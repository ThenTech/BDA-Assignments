package com.bda.operations;

import java.security.MessageDigest;
import java.util.Set;
import java.util.TreeSet;

import org.apache.beam.sdk.transforms.SimpleFunction;
import org.apache.beam.sdk.values.KV;
import org.apache.commons.lang3.StringUtils;
import org.apache.commons.codec.binary.Hex;
import org.apache.commons.codec.digest.DigestUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ShingleExtractor extends SimpleFunction<KV<Long, String>, KV<Long, Set<String>>> {
	private static final long serialVersionUID = 5358166788047943173L;
    private static final Logger LOG = LoggerFactory.getLogger(ShingleExtractor.class);

    private static final String[] IGNORE  = {"ENCODING", "ENDMARKER", "NEWLINE", "INDENT", "DEDENT", "SEMICOLON"};
    private static final String[] REPLACE = {"NAME"};
    private static final char     REPLACE_CHAR = '$';

    private int K_factor;
    private MessageDigest hashf;

    public ShingleExtractor(int K_factor) {
        this.K_factor = K_factor;
        this.hashf = DigestUtils.getMd5Digest();
    }

    private String getHash(String value) {
        final byte[] bval = org.apache.commons.codec.binary.StringUtils.getBytesUtf8(value);
		final byte[] result = this.hashf.digest(bval);
		return Hex.encodeHexString(result);
	}

	public KV<Long, Set<String>> apply(KV<Long, String> file) {
        try {
        	Set<String> shingle_set = new TreeSet<>();
        	String untokenized = new String();

        	// For each line in tokenized input
        	for (String line : file.getValue().split("\n")) {
        		if (StringUtils.isWhitespace(line))
        			continue;

        		final String [] tmp = line.split(": ", 2)[1].split(" ", 2);
        		final String token_part = tmp[0];
        		final String value_part = tmp.length > 1 ? StringUtils.strip(tmp[1], "\'") : "";

        		if (StringUtils.containsAny(token_part, IGNORE)) {
        			// Ignore certain tokens
        			continue;
        		} else if (StringUtils.containsAny(token_part, REPLACE)) {
        			// Replace identifiers and names with a single token
        			untokenized += REPLACE_CHAR;
        		} else {
        			// Append everything else
        			untokenized += value_part;
        		}

        		// Parse for shingles as soon as possible to not need more memory
        		while (untokenized.length() >= this.K_factor) {
        			final String kshingle = untokenized.substring(0, this.K_factor);
        			shingle_set.add(this.getHash(kshingle));

        			untokenized = untokenized.substring(1);
        		}
        	}

            return KV.of(file.getKey(), shingle_set);
        } catch (Exception e) {
            throw new RuntimeException("[ERROR]: Parsing (fileid, file_contents) to (fileid, [shingle_hashes]) for "
            		+ file.getValue() + ".\n" + e.toString());
        }
    }
}
