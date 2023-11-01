import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

# Instrucciones:
# Las preguntas 4 y 5 tratan sobre cómo escribir SQL. Usan la base de datos que es
# creado en el archivo `pets_db.py`.
# Estas preguntas utilizan una base de datos llamada SQLite. No necesitas instalar nada.
# En el archivo `pets_db.py` se crean tres tablas. Luego se agregan datos a cada
# de las mesas. Las siguientes preguntas tratan sobre cómo los datos de cada una de las tablas
# está relacionado.

# Parte 4.A:
# Escribe SQL para seleccionar las mascotas que no pertenecen a nadie.
# La salida debe ser una lista de tuplas en el formato: (<nombre de mascota>, <especie>, <edad>)

sql_pets_owned_by_nobody = """

SELECT NAME, SPECIES, AGE 
FROM animals
LEFT JOIN people_animals ON animals.animal_id = people_animals.pet_id
WHERE people_animals.pet_id IS NULL;

"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.


# Parte 4.B:
# Escriba SQL para seleccionar la cantidad de mascotas que son mayores que sus dueños.
# La salida debe ser un número entero.

sql_pets_older_than_owner = """

SELECT COUNT()
FROM animals a
INNER JOIN people_animals b ON b.pet_id = a.animal_id
INNER JOIN people c ON c.person_id = b.owner_id
WHERE a.age > c.age;

"""

# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)

# Parte 4.C: ¡DESAFÍO ADICIONAL!
# Escribe SQL para seleccionar las mascotas que pertenecen a Bessie y a nadie más.
# La salida debe ser una lista de tuplas en el formato: (<nombre de persona>, <nombre de mascota>, <especie>)

sql_only_owned_by_bessie = """ 

SELECT po.name, a.name, a.species
FROM people po
INNER JOIN people_animals pa ON po.person_id = pa.owner_id
INNER JOIN animals a ON pa.pet_id = a.animal_id
WHERE po.name = 'bessie'
AND NOT EXISTS (
    SELECT 1
    FROM people_animals pa2
    WHERE pa2.pet_id = a.animal_id
    AND pa2.owner_id <> pa.owner_id
);

"""