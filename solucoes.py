def sao_anagrama(string1, string2):

    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False

def cifra_de_cesar(texto, deslocamento):
    # todo : implementar a logica
    pass

def valida_cpf(cpf_string):
    # todo : implementar a logica
    pass