import random

no_responses = [
    "No problem! Feel free to browse our menu at your leisure!",
    "Sure, take your time. If you have any questions, let me know.",
    "Thank you for taking a look. Hope to see you next time!"

]
# Menu and introduction 
print(random)
user_name = (input("""Hello there:-)
What is your name?"""))

print(f"""Thank you {user_name} for coming to RC Hookah Lounge!
We got 3 Hookah flavors and 3 drinks
A hookah cost $20 (mix any flavor free of charge) and a drink cost $3
Would you like to know what they are?""")


menu_response = input("Y for Yes and N for No (Y/N)").upper()


if menu_response == "Y":
    print("""Great! For flavors we have Mint, Blueberry, Cherry and Cappucino
And for drinks we have Soda, Hot Tea and Coffee""")
    

elif menu_response == "N":
    print(random.choice(no_responses))
   
else: 
    input("Sorry I didn't quite catch that. Please type 'Y' for Yes or 'N' for No.").upper()

#return to question for correct anwswer
#flavors =[" Mint", "Cherry"," Capaocinno"]
#drinks = ["Soda", ,Tea " Coffee"]  

responses = [
            "Great, staff will be with you shortly.",
            "Thank you, staff member will attend to you shortly."
            ]

while True:
    guest_input = input("How many people would need seat?")

    try:
        guest_number = int(guest_input)
    
        if guest_number > 6 :
            print("Please wait for staff to explain group policies. Thank you")
            break
        elif guest_number >= 1 and guest_number <= 6:
            print(random.choice(responses))
            break
        else: 
            print("Please enter number of guest 1 or more")

    except ValueError:
        print("Invalid input, Please enter number")


#input("What flavor(s) would you like to get?")

    
#guest_choices= input("Are you getting (h)ookah, (drinks), or (b)oth?")
#Choice_menu = input("what flavor and drinks would you like to get")






