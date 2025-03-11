def age():
    age = int(input("Classify Age: "))
    if age >= 65:
        print("You are a Senior Citizen.")
    elif age >= 20:
        print("You are a Adult.")
    elif age >= 13:
        print("You are a Teen.")
    elif age >= 0:
        print("You are a Child")
    else:
        print("Error!, Please try again.")

while True:
    age()