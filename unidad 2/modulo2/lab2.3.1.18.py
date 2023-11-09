'''
nombre:Monserat Orduña Basaldua
descripcion:lab 2.3.1.18
Fecha:05/11/2023
'''
def mysplit(strng):
    words = []
    current_word = ""
    for char in strng:
        if char.isspace():
            if current_word:
                words.append(current_word)
            current_word = ""
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    return words

print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit(" "))
print(mysplit(" abc "))
print(mysplit(""))
