# MECHATRONICS QUIZ APP
# Created by: Your Name
# Department: Mechatronics Engineering

# List containing quiz questions, options and answers
questions = [
    {
        "question": "What does PLC stand for?",
        "options": ["A. Power Logic Controller", "B. Programmable Logic Controller",
                    "C. Programming Line Computer", "D. Power Line Control"],
        "answer": "B"
    },
    {
        "question": "What does SCADA stand for?",
        "options": ["A. Supervisory Control and Data Acquisition",
                    "B. System Control and Data Analysis",
                    "C. Software Computer Data Application",
                    "D. Simple Control and Digital Automation"],
        "answer": "A"
    },
    {
        "question": "Which device is used to control electrical circuits?",
        "options": ["A. Sensor", "B. Resistor", "C. Relay", "D. Capacitor"],
        "answer": "C"
    },
    {
        "question": "What is the full meaning of CPU?",
        "options": ["A. Central Processing Unit",
                    "B. Computer Power Unit",
                    "C. Central Program Utility",
                    "D. Control Processing User"],
        "answer": "A"
    },
    {
        "question": "Which component detects changes in the environment?",
        "options": ["A. Motor", "B. Sensor", "C. Battery", "D. Switch"],
        "answer": "B"
    },
    {
        "question": "What is the function of an actuator?",
        "options": ["A. Store data", "B. Display information",
                    "C. Produce physical movement", "D. Supply light"],
        "answer": "C"
    },
    {
        "question": "Which of these is a programming language?",
        "options": ["A. Python", "B. Keyboard", "C. Monitor", "D. Printer"],
        "answer": "A"
    },
    {
        "question": "What does DC stand for?",
        "options": ["A. Digital Current", "B. Direct Current",
                    "C. Double Circuit", "D. Data Control"],
        "answer": "B"
    },
    {
        "question": "Which component stores electrical energy?",
        "options": ["A. Switch", "B. Fuse", "C. Capacitor", "D. Relay"],
        "answer": "C"
    },
    {
        "question": "What is the main function of a robot?",
        "options": ["A. Perform tasks automatically",
                    "B. Produce electricity",
                    "C. Store water",
                    "D. Print documents"],
        "answer": "A"
    }
]


# Function to calculate the student's grade
def calculate_grade(score):
    percentage = (score / len(questions)) * 100

    if percentage >= 70:
        grade = "Excellent"
    elif percentage >= 50:
        grade = "Good"
    elif percentage >= 40:
        grade = "Pass"
    else:
        grade = "Fail"

    return percentage, grade


# Main function of the quiz
def start_quiz():
    score = 0

    print("================================")
    print("     MECHATRONICS QUIZ APP")
    print("================================")

    name = input("Enter your name: ")

    print("\nWelcome", name, "!")
    
    # Get the number of questions to attempt
    while True:
        try:
            number_of_questions = int(input("How many questions do you want to answer (1-10)? "))

            if 1 <= number_of_questions <= 10:
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print("\nChoose A, B, C or D.\n")

    # Loop through the selected questions
    for number, item in enumerate(questions[:number_of_questions], start=1):

        print("\nQuestion", number)
        print(item["question"])

        for option in item["options"]:
            print(option)

        # Accept and validate the student's answer
        answer = input("Your answer: ").strip().upper()

        while answer not in ["A", "B", "C", "D"]:
            print("Invalid answer! Please enter A, B, C or D.")
            answer = input("Your answer: ").strip().upper()

        # Check the answer
        if answer == item["answer"]:
            print("Correct! Well done.")
            score += 1
        else:
            print("Wrong answer!")
            print("The correct answer is:", item["answer"])

    # Calculate final result
    percentage = (score / number_of_questions) * 100
    percentage, grade = calculate_grade(score)

    print("\n================================")
    print("           QUIZ RESULT")
    print("================================")
    print("Student Name:", name)
    print("Total Questions:", number_of_questions)
    print("Correct Answers:", score)
    print("Wrong Answers:", number_of_questions - score)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)

    print("\nThank you for taking the quiz!")


# Run the quiz
start_quiz()