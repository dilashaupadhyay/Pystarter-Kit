import random
import time

def timed_math_challenge():
    score = 0
    num_questions = 10
    time_limit = 30  # seconds

    print("Welcome to the Timed Math Challenge!")
    print(f"You have {time_limit} seconds to answer {num_questions} questions.")
    input("Press Enter to start...")

    start_time = time.time()

    for _ in range(num_questions):
        if time.time() - start_time > time_limit:
            break

        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(["+", "-", "*"])

        question = f"{num1} {operator} {num2}"
        user_answer = input(f"What is {question}? (Type 'q' to quit) ")

        if user_answer.lower() == 'q':
            break

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue


        if operator == "+":
            correct_answer = num1 + num2
        elif operator == "-":
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\n*** Challenge Summary ***")
    print(f"Questions attempted: {num_questions}")
    print(f"Correct answers: {score}")
    print(f"Wrong answers: {num_questions - score}")
    print(f"Accuracy: {score / num_questions * 100:.2f}%")
    print(f"Time taken: {elapsed_time:.2f} seconds")

    if elapsed_time > time_limit:
        print("Time's up! The challenge is over.")
    else:
        remaining_time = time_limit - elapsed_time
        print(f"Time left: {remaining_time:.2f} seconds")

if __name__ == "__main__":
    timed_math_challenge()
