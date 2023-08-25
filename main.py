import random

def generate_random_number():
    return [random.randint(0, 9) for _ in range(4)]

def compare_numbers(guess, secret):
    correct_positions = 0
    incorrect_positions = 0
    for i in range(4):
        if guess[i] == secret[i]:
            correct_positions += 1
        elif guess[i] in secret:
            incorrect_positions += 1
    return correct_positions, incorrect_positions

def main():
    print("Welcome to the Guess the Number game!")

    play_again = True
    while play_again:
        secret_number = generate_random_number()
        attempts = 0

        while True:
            try:
                guess = input("Enter your 4-digit guess (or 'q' to quit): ")
                if guess.lower() == 'q':
                    print(f"The secret number was: {''.join(map(str, secret_number))}")
                    break
                guess = [int(digit) for digit in guess]
                if len(guess) != 4:
                    print("Please enter a 4-digit number.")
                    continue

                attempts += 1
                correct_positions, incorrect_positions = compare_numbers(guess, secret_number)
                if correct_positions == 4:
                    print(f"Congratulations! You guessed the number {guess} correctly in {attempts} attempts.")
                    break

                print(f"Hints: {'O' * correct_positions} {'X' * incorrect_positions}")
            except ValueError:
                print("Invalid input. Please enter a 4-digit number or 'q' to quit.")

        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input != 'yes':
            play_again = False

    print("Thanks for playing Guess the Number!")

if __name__ == "__main__":
    main()