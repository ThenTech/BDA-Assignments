package com.bda.operations;

import java.util.Arrays;

import org.apache.beam.sdk.transforms.DoFn;
import org.apache.beam.sdk.values.KV;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class SplitInBands extends DoFn<KV<Long, String[]>, KV<Integer, KV<Long, String[]>>> {
	private static final long serialVersionUID = -2486860980626041784L;
	private static final Logger LOG = LoggerFactory.getLogger(SplitInBands.class);

	private int n_bands;
	
	public SplitInBands(int n_bands) {
		this.n_bands = n_bands;
		
		if(this.n_bands <= 0){
			throw new IllegalArgumentException("SplitInBands: Bands > 0 required!");
		}
	}

	@ProcessElement
	public void processElement(@Element KV<Long, String[]> sigmat, OutputReceiver<KV<Integer, KV<Long, String[]>>> out) {
		final int length  = sigmat.getValue().length;
		final int rows    = (int)Math.ceil((double)length / this.n_bands);
		final int rest    = length % rows;
		final int surplus = (rest > 0 ? 1 : 0);
		final int chunks  = length / rows + surplus;

		for(int i = 0; i < (chunks - surplus); i++) {
			String[] band = Arrays.copyOfRange(
					sigmat.getValue(), 
					i * rows, 
					i * rows + rows);
			
//			LOG.info("({}, {}): {}", i, sigmat.getKey(), Arrays.toString(band));
			out.output(KV.of(i, KV.of(sigmat.getKey(), band)));
		}
		
	    if(rest > 0) {
			String[] band = Arrays.copyOfRange(
					sigmat.getValue(), 
					(chunks - 1) * rows, 
					(chunks - 1) * rows + rest);
			
//			LOG.info("({}, {}): {}", chunks - 1, sigmat.getKey(), Arrays.toString(band));
			out.output(KV.of(chunks - 1, KV.of(sigmat.getKey(), band)));
	    }
	}
}
