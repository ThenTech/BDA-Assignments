package com.selligent.tech.models.coders;

import com.selligent.tech.models.OptiExtEvent;
import org.apache.beam.sdk.coders.*;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

/**
 * Created by Laurens on 14/02/19.
 */
public class OptiExtEventCoder extends CustomCoder<OptiExtEvent> {
    @Override
    public void encode(OptiExtEvent value, OutputStream outStream) throws CoderException, IOException {

        StringUtf8Coder stringUtf8Coder = StringUtf8Coder.of();
        VarLongCoder varLongCoder = VarLongCoder.of();
        VarIntCoder varIntCoder = VarIntCoder.of();

        stringUtf8Coder.encode(value.getTenantId(), outStream);
        stringUtf8Coder.encode(value.getOrganizationId(), outStream);

        varIntCoder.encode(value.getAudienceId(), outStream);
        stringUtf8Coder.encode(value.getConsumerId(), outStream);
        stringUtf8Coder.encode(value.getType(), outStream);

        varLongCoder.encode(value.getTimestamp(), outStream);
        stringUtf8Coder.encode(value.getChannel(), outStream);
        stringUtf8Coder.encode(value.getJourneyId(), outStream);
        stringUtf8Coder.encode(value.getActionId(), outStream);
        stringUtf8Coder.encode(value.getMessageId(), outStream);

        stringUtf8Coder.encode(value.getAction(), outStream);
    }

    @Override
    public OptiExtEvent decode(InputStream inStream) throws CoderException, IOException {

        StringUtf8Coder stringUtf8Coder = StringUtf8Coder.of();
        VarLongCoder varLongCoder = VarLongCoder.of();
        VarIntCoder varIntCoder = VarIntCoder.of();

        OptiExtEvent event = new OptiExtEvent();

        event.setTenantId(stringUtf8Coder.decode(inStream));
        event.setOrganizationId(stringUtf8Coder.decode(inStream));

        event.setAudienceId(varIntCoder.decode(inStream));
        event.setConsumerId(stringUtf8Coder.decode(inStream));
        event.setType(stringUtf8Coder.decode(inStream));

        event.setTimestamp(varLongCoder.decode(inStream));
        event.setChannel(stringUtf8Coder.decode(inStream));
        event.setJourneyId(stringUtf8Coder.decode(inStream));
        event.setActionId(stringUtf8Coder.decode(inStream));
        event.setMessageId(stringUtf8Coder.decode(inStream));

        event.setAction(stringUtf8Coder.decode(inStream));

        return event;
    }

    @Override
    public void verifyDeterministic() throws NonDeterministicException {

    }
}
