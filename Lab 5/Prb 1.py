a= "hello"
b= "b2b2b2"
c= "3g3g       "

d= a+" "+b+" "+c
print(d)

print(len(d))
print(d[:-3])
print(d[::-1])

print(d.upper())
print(d.lower())
print(d.title())
print(d.isdigit())
print(d.find("39"))
print(d.capitalize())
print(d.isalnum())
print(d.count("b2"))
print(d.split())
print(d.count("a2"))
print(d.replace("hello","python"))
print(d.swapcase())


x = "b2"
found = False

for i in range(len(d)):
    if x in d:
        found = True
        break
print(found)

