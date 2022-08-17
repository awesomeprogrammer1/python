# Homework
# 1. Implement function replace(s: str) -> str,
# s in 1 char, don't use python standard library functions
# 2. Implement operator in (create function in(s: str) -> bool),
# s is 1 char long, don't use python standard library functions
# 3. Explain the difference between commenting with #
# and with multi-line strings
# 4. Finish the string methods presentation
# 5. finish contact_book


print("Hello")

a = "Hello"
print(a)

k = "Hello, World!"
print(k)
k = k.replace("H", "J")
print(k)


b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

c = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(c)

for x in "banana":
    print(x)

d = "Hello, World!"
print(d[1])

e = "Hello, World!"
print(len(e))

txt = "The best things in life are free!"
print("free" in txt)

txt2 = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


f = "Hello, World!"
print(f[2:5])

g = "Hello, World!"
print(g[-5:-2])

h = "Hello, World!"
print(h.upper())

i = "Hello, World!"
print(i.lower())

j = " Hello, World! "
print(j.strip())

k = "Hello, World!"
print(k.replace("H", "J"))

l = "Hello, World!"
print(l.split(","))

m = "Hello"
n = "World"
o = m + n
print(o)

p = "Hello"
q = "World"
r = p + " " + q
print(r)

s = 'We are the so-called "Vikings" from the north.'
print(s)

t = "Hello, Andrew"
print(t[-5:-2])

u = "Hello, user"
print(u.capitalize())
print(u.casefold())
print(u.rindex("l"))
print(u.index(""))
print(u.swapcase())
print(u.casefold())
print(u.center(100))
print(u.count("l"))
print(u.format())
print(u.partition("l"))
