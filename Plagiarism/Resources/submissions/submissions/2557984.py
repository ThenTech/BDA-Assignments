def helping_tool(whats_in, whats_out):
    if len(whats_out) != 0:
        for j in helping_tool(whats_in, whats_out[1:]):
            if j == "":
                print(j, end = "")
            elif j == helping_tool(whats_in, whats_out[1:])[len(helping_tool(whats_in, whats_out[1:])) - 1]:
                print(j)
            else:
                print(j, " ", sep = "", end = "")
        for i in helping_tool(whats_in + [whats_out[0]], whats_out[1:]):
            if i == "":
                print(i, end = "")
            elif i==helping_tool(whats_in + [whats_out[0]], whats_out[1:])[len(helping_tool(whats_in + [whats_out[0]], whats_out[1:])) - 1]:
                print(i)
            else:
                print(i, " ", sep = "", end = "")
        return ""
    else:
        return whats_in
given_in = input()
helping_tool([], given_in.split())