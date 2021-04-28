print("What is your name?")
my_name = input ( )
print("Nice to meet you " + my_name + "!")
thank_you = input ( )
print("What is your favorite food, " + my_name + "?")
favorite_food = input ( )
print("Ah, your favorite food is " + favorite_food + ", mine too!")
while ( res:=input("Do you want to hear a story? (Enter y/n)").lower() ) not in {"y","n"}: pass
if res=='y':
    print("There was once a goddess birthed from a volcano. She travelled far and wide, she even met death. Eventually, she went back to the volcano, believing herself to be enough company.")
if res=='n':
    print("Maybe next time then. Thank you.")
response = input ( )
