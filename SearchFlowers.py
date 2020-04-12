# Write your code here
path = "flowers.txt"

#def create_flower(filename):
flower_dict = {}
# HINT: create a dictionary from flowers.txt
with open(path) as flo:
    for name in flo:
        (key,val) = name.split(": ")
        flower_dict[str(key)] = val
#return flower_dict
#print(flower_dict)
# HINT: create a function to ask for user's first and last name
def whatsName():
    #flowerD = create_flower(path)
    userName = input("Enter your First [space] Last name only: ")
    firstName = userName[0]
    firstLetter = firstName[0]
    print("Unique Flower Name is: {}".format(flower_dict[firstLetter]))

# print the desired output

whatsName()