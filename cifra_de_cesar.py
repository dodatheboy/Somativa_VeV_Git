def cifra_de_cesar(texto, deslocamento):
    r = []
    for c in texto:
        if c.isalpha():
            b = ord('A') if c.isupper() else ord('a')
            r.append(chr((ord(c) - b + deslocamento) % 26 + b))
        else:
            r.append(c)
    return ''.join(r)