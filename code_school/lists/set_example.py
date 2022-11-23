# intersection
animals = {"lizards", "bunnys", "rattlesnakes"}
mammals = {"cats", "bunnys", "dogs"}

animals_which_are_mammals = animals.intersection(mammals)

print(animals_which_are_mammals)
"""
vs
"""
# intersection update
animals = {"lizards", "bunnys", "rattlesnakes"}
mammals = {"cats", "bunnys", "dogs"}

animals.intersection_update(mammals)
print(animals)
