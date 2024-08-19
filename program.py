from pymongo import MongoClient

# Configuración de la conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['recetas_db']

# Colecciones
recipes_collection = db['recipes']

# Función para agregar una nueva receta
def add_recipe():
    name = input("Nombre de la receta: ")
    ingredients = add_ingredients()
    steps = add_steps()
    
    recipe = {
        "name": name,
        "ingredients": ingredients,
        "steps": steps
    }
    
    recipes_collection.insert_one(recipe)

# Función para agregar ingredientes a una receta
def add_ingredients():
    ingredients = []
    print("Agregar ingredientes (dejar vacío para terminar):")
    while True:
        ingredient = input("Ingrediente: ")
        if ingredient == "":
            break
        ingredients.append(ingredient)
    return ingredients

# Función para agregar pasos a una receta
def add_steps():
    steps = []
    print("Agregar pasos (dejar vacío para terminar):")
    while True:
        step = input("Paso: ")
        if step == "":
            break
        steps.append(step)
    return steps

# Función para actualizar una receta existente
def update_recipe():
    list_recipes()
    recipe_name = input("Nombre de la receta a actualizar: ")
    recipe = recipes_collection.find_one({"name": recipe_name})
    
    if recipe:
        option = input("Actualizar (1) Ingredientes o (2) Pasos: ")
        if option == "1":
            ingredients = add_ingredients()
            recipes_collection.update_one({"name": recipe_name}, {"$set": {"ingredients": ingredients}})
        elif option == "2":
            steps = add_steps()
            recipes_collection.update_one({"name": recipe_name}, {"$set": {"steps": steps}})
    else:
        print("Receta no encontrada.")

# Función para eliminar una receta existente
def delete_recipe():
    list_recipes()
    recipe_name = input("Nombre de la receta a eliminar: ")
    recipes_collection.delete_one({"name": recipe_name})

# Función para ver todas las recetas
def list_recipes():
    recipes = recipes_collection.find()
    for recipe in recipes:
        print(f"{recipe['name']}")

# Función para buscar los ingredientes y pasos de una receta
def search_recipe():
    list_recipes()
    recipe_name = input("Nombre de la receta a buscar: ")
    recipe = recipes_collection.find_one({"name": recipe_name})
    
    if recipe:
        print("\nIngredientes:")
        for ingredient in recipe['ingredients']:
            print(f"- {ingredient}")
        
        print("\nPasos:")
        for step in recipe['steps']:
            print(f"- {step}")
    else:
        print("Receta no encontrada.")

# Función principal del menú
def menu():
    while True:
        print("\nLibro de Recetas")
        print("1. Agregar nueva receta")
        print("2. Actualizar receta existente")
        print("3. Eliminar receta existente")
        print("4. Ver listado de recetas")
        print("5. Buscar ingredientes y pasos de receta")
        print("6. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            add_recipe()
        elif option == "2":
            update_recipe()
        elif option == "3":
            delete_recipe()
        elif option == "4":
            list_recipes()
        elif option == "5":
            search_recipe()
        elif option == "6":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
