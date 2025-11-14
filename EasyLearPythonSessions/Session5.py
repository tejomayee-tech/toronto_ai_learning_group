# Choice = input("enter y/n:")

# while Choice != "y" and Choice != "n":
#     Choice = input("enter y/n:")

# print(Choice)

sentense = "how are you."

def interations(start,stop,step):
    #                   Start      Stop           Step 
    for index in range (start,     stop,          step    ):
        print(index)

interations(10,20,4)
interations(1000,3000,100)
interations(100000,200000,1000)

