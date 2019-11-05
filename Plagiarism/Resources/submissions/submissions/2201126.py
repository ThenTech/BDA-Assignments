def cleanup_spaces(s):
	i = 0
	cleaned = ""
	prev_char_is_space = True
	while i < len(s):
		if s[i] == " " and not prev_char_is_space:
			prev_char_is_space = True
			cleaned += s[i]
		elif s[i] != " ":
			prev_char_is_space = False
			cleaned += s[i]
		i += 1
	if cleaned[len(cleaned)-1] == " ":
		cleaned = cleaned[:len(cleaned)-1]
	return cleaned