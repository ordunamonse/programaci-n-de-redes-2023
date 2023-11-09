'''
nombre:Monserat Orduña Basaldua
descripcion:apy 2 recetas 
Fecha:09/11/2023
'''
import requests

while True:
    input("Presiona Enter para obtener una receta aleatoria (o escribe 'quit' para salir)")

    main_api = "https://www.themealdb.com/api/json/v1/1/random.php"

    response = requests.get(main_api)

    if response.status_code == 200:
        data = response.json()
        meal = data['meals'][0]
        print("Nombre de la receta: " + meal['strMeal'])
        print("Categoría: " + meal['strCategory'])
        print("Instrucciones: " + meal['strInstructions'])
        print("Ingredientes:")
        for i in range(1, 21):
            ingredient_key = 'strIngredient' + str(i)
            measure_key = 'strMeasure' + str(i)
            ingredient = meal.get(ingredient_key)
            measure = meal.get(measure_key)
            if ingredient and measure:
                print(f"- {ingredient} ({measure})")
            else:
                break
    else:
        print("No se pudo obtener la receta. Inténtalo de nuevo más tarde.")

    user_input = input("¿Quieres ver otra receta? (y/n): ")
    if user_input.lower() != 'y':
        print("¡Buen provecho!")
        break

