def atsign_checker(str):
    x = 0
    for character in str:
        if character == "@":
            x = x + 1
    if x == 1:
        return True        
    else:
        return False
def point_checker(str):
    y = 0
    for character in str:
        if character == ".":
            y = y + 1
    if y >= 1:
        return True
    else:
        return False
    
mail = input("Please enter your mail address : ")
if (atsign_checker(mail) and point_checker(mail) == True):
    print("Your mail adress is valid.")
else:
    print("Your mail adress isn't valid.")