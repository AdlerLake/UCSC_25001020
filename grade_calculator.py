# Continuous Grade Calculator

def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject}: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 0 and 100.")

while True:
    name = input("\nEnter student's name: ")

    # Get marks
    sub1 = get_marks("Subject 1")
    sub2 = get_marks("Subject 2")
    sub3 = get_marks("Subject 3")

    # Calculate average
    average = (sub1 + sub2 + sub3) / 3

    # Determine grade
    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    # Cleanly formatted output
    print("\n--- Result ---")
    print(f"Name   : {name}")
    print(f"Average: {round(average, 2)}")
    print(f"Grade  : {grade}")
    print("--------------")

    # Check if user wants to continue
    choice = input("Type 'exit' to quit or press Enter to continue: ").strip().lower()
    if choice == "exit":
        print("Exiting program. Goodbye!")
        break