'''
nombre:Monserat Orduña Basaldua
Descripcion: laboratorio 3.2.1.11
Fecha:2/10/2023
'''

user_word = input("Ingresa una palabra: ")

user_word = user_word.upper()

word_without_vowels = ""
for letter in user_word:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter

print(word_without_vowels)