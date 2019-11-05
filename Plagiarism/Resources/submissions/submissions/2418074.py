def helping_tool(whats_in, whats_out):
    if len(whats_out) == 0:
        return whats_in
    else:
        print(helping_tool(whats_in + [whats_out[0]], whats_out[1:]))
        print(helping_tool(whats_in, whats_out[1:]), end = "")
        return ""
given_in = input()
helping_tool([], given_in.split())