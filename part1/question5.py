################################################################################
#     ____                          __     _                           ______
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____           / ____/
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         /___ \  
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ____/ /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_____/   
#                                                                            
#  Question 5
################################################################################
#
# Instructions:
# This questions continues to use the database we worked with in Question 4. In 
# this question, we will made some modifications ot the table.

# Instrucciones:
# Esta pregunta continúa utilizando la base de datos con la que trabajamos en la Pregunta 4. En
# esta pregunta, haremos algunas modificaciones en la tabla.

# Part 5.A:
# Create a new table, 'favorite_foods.' It should have the columns:
# food_id integer
# name text
# vegetarian integer

# Parte 5.A:
# Crea una nueva tabla, 'comidas_favoritas'. Debería tener las columnas:
# alimento_id entero
# texto del nombre
# entero vegetariano

sql_create_favorite_foods = """

CREATE TABLE favorite_foods (
      food_id integer,
      name text ,
      vegetarian
    );

"""

# Part 5.B:
# Alter the animals and people tables by adding a new column to each called 'favorite_food_id'
# The test suite will verify the new changes by inserting some new rows.

# Parte 5.B:
# Modifique las tablas de animales y personas agregando una nueva columna a cada una llamada 'favorite_food_id'
# El conjunto de pruebas verificará los nuevos cambios insertando algunas filas nuevas.

sql_alter_tables_with_favorite_food = """

ALTER TABLE animals
ADD favorite_food_id integer;

ALTER TABLE people
ADD favorite_food_id integer;

"""

# Part 5.C:
# Write a query to select all pets that are vegetarian.
# THe output should be a list of tuples in the format: (<pet name>, <food name>)

# Parte 5.C:
# Escriba una consulta para seleccionar todas las mascotas que sean vegetarianas.
# La salida debe ser una lista de tuplas en el formato: (<nombre de mascota>, <nombre de comida>)

sql_select_all_vegetarian_pets = """

SELECT a.name, f.name
FROM animals a
INNER JOIN favorite_foods f ON a.favorite_food_id = f.food_id
WHERE f.vegetarian = 1;

"""