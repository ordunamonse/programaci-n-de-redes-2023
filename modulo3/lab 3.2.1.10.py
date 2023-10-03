'''
nombre:Monserat Orduña Basaldua
Descripcion: laboratorio 3.2.1.10
Fecha:2/10/2023
'''

user_word = input("Ingresa una palabra: ")

user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)