################################################################################
#     ____                          __     _                          ___ 
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__ \
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         __/ /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / __/ 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/ 
#                                                                         
#  Question 2
################################################################################
#
# Instructions:
# Write a function that will swap a tuple of two items. For example, the function 
# should change (x, y) into (y, x). 
# Assign the function to `swapper` so that the function `run_swapper(..)` can use
# it. As always, there is a test suite that checks the result. It is in 
# `question2_test.py.`
# Instrucciones:
# Escribe una función que intercambie una tupla de dos elementos. Por ejemplo, la función
# debería cambiar (x, y) a (y, x).
# Asigne la función a `swapper` para que la función `run_swapper(..)` pueda usar
# it. Como siempre, hay un conjunto de pruebas que comprueba el resultado. Está en
# `pregunta2_prueba.py.`

swapper = None

def run_swapper(swapper):
  list_of_tuples = [(t[1],t[0]) for t in swapper]
  return list(list_of_tuples)