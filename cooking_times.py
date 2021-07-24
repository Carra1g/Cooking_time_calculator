#Cooking times

#user the app again
def again():
    again_input = str(input("Do you need to run the app again: y/n: "))
    for choice_input in again_input:
        #convers input to lower for error handling.
        if choice_input.lower() == "y":
            time_helper()
        else:
            choice_input.lower() == "n"
            print("Good Bye!")
            break

def time_helper():
    meat_option = ""
    print("What are you cooking:\n1 = Beef.\n2 = Chicken.\n3 = Lamb.\n4 = Pork.")
    #take user input.
    user_input = int(input("\nPick an option: "))

    if user_input == 1:
        meat_option = "Beef"
        weight = float(input("\nHow much does it weight?: "))
        print(f"\nYour {meat_option} weighs {weight}kg's")
        cook_time = (weight * 50) + 20# calculate cooking time
        print (f"\n\tCooking time of {meat_option}(Well Done) weighing {weight}kg is {cook_time} minutes.\n")
        again()
        
    elif user_input == 2:
        meat_option = "Chicken"
        weight = float(input("\nHow much does it weight?: "))
        print(f"\nYour {meat_option} weighs {weight}kg's")
        cook_time = (weight * 45) + 20# calculate cooking time
        print (f"\n\tCooking time of {meat_option} weighing {weight}kg is {cook_time} minutes.\n")
        again()
        
    elif user_input == 3:
        meat_option = "Lamb"
        weight = float(input("\nHow much does it weight?: "))
        print(f"\nYour {meat_option} weighs {weight}kg's")
        cook_time = (weight * 60) + 30# calculate cooking time
        print (f"\n\tCooking time of {meat_option} weighing {weight}kg is {cook_time} minutes.\n")
        again()
    else:
        meat_option = "Pork"
        weight = float(input("\nHow much does it weight?: "))
        print(f"\nYour {meat_option} weighs {weight}kg's")
        cook_time = (weight * 70) + 35# calculate cooking time
        print (f"\n\tCooking time of {meat_option} weighing {weight}kg is {cook_time} minutes.\n")
        again()
        
time_helper()

