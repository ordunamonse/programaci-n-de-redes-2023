'''
nombre:Monserat Orduña Basaldua
descripcion:lab 2.4.1.6
Fecha:05/11/2023
'''
digit_patterns = [
    ["###", "# #", "# #", "# #", "###"],  
    ["  #", "  #", "  #", "  #", "  #"],  
    ["###", "  #", "###", "#  ", "###"],  
    ["###", "  #", "###", "  #", "###"],  
    ["# #", "# #", "###", "  #", "  #"],  
    ["###", "#  ", "###", "  #", "###"],  
    ["###", "#  ", "###", "# #", "###"],  
    ["###", "  #", "  #", "  #", "  #"],  
    ["###", "# #", "###", "# #", "###"],  
    ["###", "# #", "###", "  #", "###"]   
]

def display_digit(number):

    digits = [int(digit) for digit in str(number)]
   
    for row in range(5):
        for digit in digits:
            print(digit_patterns[digit][row], end=" ")
        print()

numero = int(input("Ingrese un número entero no negativo: "))

display_digit(numero)
