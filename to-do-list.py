print("Welcome to your to do list.")
objectives = []
objindex = ""
def activeobjectives():
    if not objectives:
        print("You haven't entered any objectives.")
    else:
            print("\nobjectives:")
            for index, objective in enumerate(objectives):
                print(f"{index + 1}. {objective}")        
       
    
def addobjective():
    try:
       objnum = int(input("Enter the number of objectives you wish to add:"))
       for sub in range(objnum):
           objective = input("Enter the objective")
           objectives.append({"Objective": objective, "Completed": False})
           print("The objective was added.")
    except ValueError:
        print("Invalid.")

def killobjective():
    activeobjectives()
    try:
        objindex = int(input("Enter to number corresponding to the task you wish to delete:")) -1
        if 0 < objindex < len(objectives):
            objectives.pop(objindex)
        else: 
            print("No objectives match this number.")
    except ValueError:
        print("Invalid.")

def completedobjective():
    activeobjectives()
    try:
        objindex = int(input("Enter to number corresponding to the objective:")) -1
        if 0 <= objindex < len(objectives):
            objectives[objindex]["Completed"] = True
            print(f"Objective {objectives[objindex]} has been marked as complete.")
        else:
            print("No objectives match this number.")
    except ValueError:
        print("Invalid.")


while True:
    
    print("1 : Check Active objectives")
    print("2 : Add an objective")
    print("3 : Delete an objective")
    print("4 : Mark an objective as complete")
    print("5 : End the program")
    selection = int(input("Select an option with the corresponding number:"))
    match selection:
        case 1:
            activeobjectives()

        case 2:
            addobjective()

        case 3:
            killobjective()

        case 4:
            completedobjective()

        case 5:
            print("See you later~(COMPLETE YOUR OBJECTIVES OR I'LL STEAL YOUR SOUL)")
            break

        case _:
          print("Invalid input, I hope you step on a lego :D")
