#No problem! Feel free to browse our menu at your leisure
user_name = (input("""Hello there:-)
What is your name?"""))
print(f"""Thank you {user_name} for coming to RC Hookah Lounge!
We got 3 Hookah flavors and 3 drinks
A hookah cost $20 (combine any flavor free of charge) and a drink cost $3
Would you like to know what they are?""")
menu_response = input("y for Yes and n for No (y/n)")
if menu_response == "y":
    print("""Great! For flavors we have Mint, Blueberry, Cherry and Cappucino
And for drinks we have Soda, Hot Tea and Coffee""")
elif menu_response == "n":
        print("No problem! Feel free to browse our menu at your leisure!")
else: 
    print("Sorry I didn't quite catch that. Please type 'y' for Yes or 'n' for No.")
#Flavors =[" Mint", "Cherry"," Capaocinno"]
#Drinks = ["Soda", ,Tea " Coffee"]
