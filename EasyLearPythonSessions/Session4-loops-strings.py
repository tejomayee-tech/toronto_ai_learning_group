
a = True
b = False

print ( a == b )
print ( b < a )

while b == a:
    print("inside the loop")
    b=True

print("below the loop")

print("---------------------------")
a =10

while a <= 50:
    print(a)
    a += 10
    if a >= 30:
        break