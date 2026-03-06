# Robust Continuous Grade Calculator

def get_alpha_input(prompt):
    """Get an alphabetic string input"""
    while True:
        text = input(prompt).strip()
        if text.isalpha():
            return text
        else:
            print("Input must only contain letters. Try again.")

def get_integer_marks(subject):
    """Get integer marks between 0 and 100"""
    while True:
        try:
            marks = int(input(f"Enter marks for {subject}: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("Invalid input. Enter an integer between 0 and 100.")

while True:
    name = get_alpha_input("\nEnter student's name: ")

    subjects = []
    marks = []

    # Get 3 subjects and marks
    for i in range(1, 4):
        subject_name = get_alpha_input(f"Enter name of Subject {i}: ")
        subjects.append(subject_name)
        subject_marks = get_integer_marks(subject_name)
        marks.append(subject_marks)

    # Calculate average
    average = sum(marks) / len(marks)

    # Determine grade
    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    # Clean output
    print("\n--- Result ---")
    print(f"Name   : {name}")
    print(f"Average: {average:.2f}")
    print(f"Grade  : {grade}")
    print("--------------")

    # Exit option
    choice = input("Type 'exit' to quit or press Enter to continue: ").strip().lower()
    if choice == "exit":
        print("Exiting program. Goodbye!")
        break