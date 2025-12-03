# Choice = input("enter y/n:")

# while Choice != "y" and Choice != "n":
#     Choice = input("enter y/n:")

# print(Choice)

sentence = "how are you."

def iterations(start,stop,step):
    #                   Start      Stop           Step 
    for index in range (start,     stop,          step    ):
        print(index)

iterations(10,20,4)
iterations(1000,3000,100)
iterations(100000,200000,1000)

