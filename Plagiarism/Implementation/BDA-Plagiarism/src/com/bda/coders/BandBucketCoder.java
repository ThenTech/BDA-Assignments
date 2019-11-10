package com.bda.coders;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.List;
import java.util.Map;

import org.apache.beam.sdk.coders.CoderException;
import org.apache.beam.sdk.coders.CustomCoder;
import org.apache.beam.sdk.coders.ListCoder;
import org.apache.beam.sdk.coders.MapCoder;
import org.apache.beam.sdk.coders.StringUtf8Coder;
import org.apache.beam.sdk.coders.VarIntCoder;
import org.apache.beam.sdk.coders.VarLongCoder;
import org.apache.beam.sdk.values.KV;


public class BandBucketCoder extends CustomCoder<KV<Integer, Map<String, List<Long>>>> {
	private static final long serialVersionUID = 6785374362913891886L;

	@Override
    public void encode(KV<Integer, Map<String, List<Long>>> value, OutputStream outStream) throws CoderException, IOException {
        VarIntCoder varIntCoder = VarIntCoder.of();
        ListCoder<Long> varListCoder = ListCoder.of(VarLongCoder.of());
        MapCoder<String, List<Long>> varMapCoder = MapCoder.of(StringUtf8Coder.of(), varListCoder);

        varIntCoder.encode(value.getKey(), outStream);
        varMapCoder.encode(value.getValue(), outStream);
    }

    @Override
    public KV<Integer, Map<String, List<Long>>> decode(InputStream inStream) throws CoderException, IOException {
        VarIntCoder varIntCoder = VarIntCoder.of();
        ListCoder<Long> varListCoder = ListCoder.of(VarLongCoder.of());
        MapCoder<String, List<Long>> varMapCoder = MapCoder.of(StringUtf8Coder.of(), varListCoder);

        int bucket_id = varIntCoder.decode(inStream);
        Map<String, List<Long>> maplisted = varMapCoder.decode(inStream);
        
        return KV.of(bucket_id, maplisted);
    }

    @Override
    public void verifyDeterministic() throws NonDeterministicException {

    }
}