alphabet = "abcdefghijklmnopqrstuvwxyz"

out = open("Output.txt", "w")
for letter in alphabet:
    inf = open("War and Peace.txt", "r")
    a = 0
    for i in inf:
        a += i.count(letter)
        a += i.count(letter.upper())
    inf.close()
    s = letter + "\t" + str(a) + "\n"
    print(s)
    out.write(s)
out.close()
