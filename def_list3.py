def f3(list):
    s = ""
    for character in map(chr, list):
        s = s + character
    return s