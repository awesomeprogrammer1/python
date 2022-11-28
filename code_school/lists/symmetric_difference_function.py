def symmetric_difference(set1: set, set2: set):
    diff_set1 = set1.difference(set2)
    diff_set2 = set2.difference(set1)
    return diff_set1.union(diff_set2)


animals = {"lizards", "bunnys", "rattlesnakes", "sharkie"}
mammals = {"cats", "bunnys", "dogs"}

print(symmetric_difference(animals, mammals))
print(animals.symmetric_difference(mammals))
