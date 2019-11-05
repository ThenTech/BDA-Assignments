def cleanup_spaces(s):
    lijst = s.split()
    uitkomst = ''
    for x in lijst:
        uitkomst += x + ' '
    uitkomst = uitkomst[:len(uitkomst)-1]
    return uitkomst