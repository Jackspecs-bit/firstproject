import random

no_responses = [
    "No problem! Feel free to browse our menu at your leisure!",
    "Sure, take your time. If you have any questions, let me know.",
    "Thank you for taking a look. Hope to see you next time."

]

print(random)
#No problem! Feel free to browse our menu at your leisure
user_name = (input("""Hello there:-)
What is your name?"""))
print(f"""Thank you {user_name} for coming to RC Hookah Lounge!
We got 3 Hookah flavors and 3 drinks
A hookah cost $20 (combine any flavor free of charge) and a drink cost $3
Would you like to know what they are?""")
menu_response = input("Y for Yes and N for No (Y/N)"). upper()
if menu_response == "Y":
    print("""Great! For flavors we have Mint, Blueberry, Cherry and Cappucino
And for drinks we have Soda, Hot Tea and Coffee""")
elif menu_response == "N":
    print(random.choice(no_responses))
    
else: 
    print("Sorry I didn't quite catch that. Please type 'Y' for Yes or 'N' for No.")
#Flavors =[" Mint", "Cherry"," Capaocinno"]
#Drinks = ["Soda", ,Tea " Coffee"]
