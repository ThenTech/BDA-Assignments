package com.bda.operations;

import java.util.Arrays;

import org.apache.beam.sdk.transforms.DoFn;
import org.apache.beam.sdk.values.KV;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class SplitInBands extends DoFn<KV<Long, String[]>, KV<Integer, KV<Long, String[]>>> {
	private static final long serialVersionUID = -2486860980626041784L;
	private static final Logger LOG = LoggerFactory.getLogger(SplitInBands.class);

	private final int n_bands;
	private final int length;  
	private final int rows;    
	private final int rest;    
	private final int surplus; 
	private final int chunks;  
	
	public SplitInBands(int n_bands, int permutations) {
		if(n_bands <= 0){
			throw new IllegalArgumentException("SplitInBands: Bands > 0 required!");
		}
		
		this.n_bands = n_bands;
		this.length  = permutations;                     
		this.rows    = (int)Math.ceil((double)length / this.n_bands);
		this.rest    = length % rows;                                
		this.surplus = (rest > 0 ? 1 : 0);                           
		this.chunks  = length / rows + surplus;                      
	}

	@ProcessElement
	public void processElement(@Element KV<Long, String[]> sigmat, OutputReceiver<KV<Integer, KV<Long, String[]>>> out) {
		for(int i = 0; i < (this.chunks - this.surplus); i++) {
			String[] band = Arrays.copyOfRange(
					sigmat.getValue(), 
					i * this.rows, 
					i * this.rows + this.rows);
			
//			LOG.info("({}, {}): {}", i, sigmat.getKey(), Arrays.toString(band));
			out.output(KV.of(i, KV.of(sigmat.getKey(), band)));
		}
		
	    if(this.rest > 0) {
			String[] band = Arrays.copyOfRange(
					sigmat.getValue(), 
					(this.chunks - 1) * this.rows, 
					(this.chunks - 1) * this.rows + this.rest);
			
//			LOG.info("({}, {}): {}", chunks - 1, sigmat.getKey(), Arrays.toString(band));
			out.output(KV.of(this.chunks - 1, KV.of(sigmat.getKey(), band)));
	    }
	}
}
