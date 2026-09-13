# Name: Zoey Spies
# KUID: 3136594
# LAB Session (Day/Time): Monday 11 AM
# LAB Assignment: Lab 2
# Description: Takes command line input and gives response about if they are
#
#
#
# Collaborators/Sources: EECS 268 Notes

#   Note: if you are working in python, you are  
#   REQUIRED to call this function to get your
#   input, so all assignments are consistant 

#   Returns a list of number,letter pairs
def get_mapping_pairs() -> str:
    x = input("Enter your mapping pairs: ")
    items = x.replace("(", "").replace(" ", "").strip(")").split(")")
    pairs = []
    for item in items:
        pairs.append(item.split(","))
    return pairs


# Your Code Here
get_pairs = get_mapping_pairs()

inputs = []
outputs = []

#loops through user input and pulls out the pairs into seperate lists
for i in get_pairs:
    inputs.append(i[0])
    outputs.append(i[1])

#check if is function
if len(inputs) != len(set(inputs)):
    print("Not function")

else:
else:
    oto = inputs == set(outputs)

    onto = set(outputs) == {'A', 'B', 'C', 'D'}

    #check both then go through checking each
    if oto and onto:
        print("Function, one to one, onto")
    elif oto:
        print("Function, one to one")
    elif onto:
        print("Function, onto")
    else:
        print("Function")
