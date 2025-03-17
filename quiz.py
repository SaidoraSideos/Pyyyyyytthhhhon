import random

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. Mark Twain", "C. William Shakespeare", "D. Jane Austen"],
        "answer": "C"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Deez nutz"],
        "answer": "D"
    },
    {
        "question": "In the japanese manga Delicious in Dungeon (Or Dungeon Meshi), How does Laios defeat the winged-lion?",
        "options": ["A. Frontshots", "B. He eats it", "C. Backshots", "D. He doesn't"],
        "answer": "B"
    }
]

random.shuffle(quiz_questions)

score = 0

print("Let's see how much you know :):\n")

for i, question in enumerate(quiz_questions, start=1):
    print(f"Question {i}: {question['question']}")
    for option in question["options"]:
        print(option)
    
    user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

    """Code for validating input"""
    while True:
        if user_answer in question["options"]:
            break
        print("Invalid option. Enter an option from A-D.")

    
    if user_answer == question["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Dumbass! The correct answer was {question['answer']}\n")

print(f"That's a wrap! Your score is {score}/{len(quiz_questions)}")