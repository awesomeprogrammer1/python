problem_list = [
    "Living Giant Tree",
    "AlienFlying Saucer",
    "monster Spirit from theParallel Universe",
    "Evil Artificial Intelligence",
    "Parasites That Capture the Brain",
    "Mutant Centipede",
    "Mad Godzilla",
    "Black Dragon",
    "Titanium",
]

# for element in problem_list:
#     if element.lower().startswith("m"):
#         print(element)

# for element in problem_list:
#     if len(element.split()) > 2:
#         print(element)

for element in problem_list:
    if element.istitle():
        print(element)
