# # pip install -U ipykernel


a = 10
#                start  stop   step
for var in range(0,     a,     2):
    print(var)

print(var)

for var in range(8, -1, -2 ):
    print(var)


# start is optional and its default is 0
# step is optional and its default is 1

for var in range(10):
    print(var)

#          0,                9
numList = [1,2,3,4,5,6,7,8,9,10]
Fruits = ["apple","banana", 'kiwi',"mango"]
print(numList[0])
print(numList[-1])

for var in range(10):
    print("value of var",var)
    print("List value at", var, "is", numList[var])



