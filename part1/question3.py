################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!

# Instrucciones:
# Crea una clase de Python para un horno mágico que puede combinar ingredientes al mismo tiempo.
# diferentes temperaturas para elaborar materiales especiales.
#
# La clase horno debería tener los métodos:
# - agregar (elemento) para agregar un horno a combinar
# - congelar() para congelar los ingredientes
# - hervir() para hervir los ingredientes
# - espera() para combinar los ingredientes sin cambios de temperatura
# - get_output() para obtener el resultado
#
# Necesitarás cambiar la función `make_oven()` para devolver una nueva instancia
# de tu horno.
#
# La función `alchemy_combine()` usará tu horno. Puedes ver el resultado esperado
# fórmulas y sus resultados en el archivo de prueba, `question3_test.py`.

# ¡Esta función debería devolver una instancia de horno!
class oven:
  def __init__(self,item):
    self.item = []
  def add(self,item):
    self.item.append(item)
  def freeze(self):
    None
  def boil(self):
    None
  def wait(self):
    None
  def get_output(self):
    if "lead" in self.item and "mercury" in self.item:
      return "gold"
    elif "water" in self.item and "air" in self.item:
      return "snow"
    elif "cheese" in self.item and "dough" in self.item and "tomato" in self.item:
      return "pizza"


def make_oven():
  return oven(item=None)

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()