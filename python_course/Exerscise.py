import random

class KBCGame:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "options": ["A. London", "B. Paris", "C. Berlin", "D. Rome"], "correct_option": "B"},
            {"question": "Which planet is known as the Red Planet?", "options": ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"], "correct_option": "A"},
            {"question": "Who wrote 'Romeo and Juliet'?", "options": ["A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens", "D. Mark Twain"], "correct_option": "A"},
            # Add more questions as needed
        ]
        self.current_question_index = 0
        self.lifelines = {"5050": self.fifty_fifty, "phone": self.phone_a_friend}
        self.used_lifelines = set()

    def start_game(self):
        print("Welcome to Kaun Banega Crorepati!\n")
        while self.current_question_index < len(self.questions):
            self.display_question()
            user_input = input("Your answer: ").upper()
            if user_input == "Q":
                print("You quit the game. You won nothing.")
                break
            elif user_input in self.lifelines and user_input not in self.used_lifelines:
                lifeline_function = self.lifelines[user_input]
                lifeline_function()
                self.used_lifelines.add(user_input)
            elif user_input == self.questions[self.current_question_index]["correct_option"]:
                print("Correct!\n")
                self.current_question_index += 1
            else:
                print("Incorrect! Game over.")
                break
        print("Thanks for playing!")

    def display_question(self):
        question_data = self.questions[self.current_question_index]
        print(f"Question {self.current_question_index + 1}: {question_data['question']}")
        for option in question_data["options"]:
            print(option)
        print("Enter 'Q' to quit or use a lifeline (if available).")

    def fifty_fifty(self):
        question_data = self.questions[self.current_question_index]
        options = question_data["options"]
        correct_option = question_data["correct_option"]
        options.remove(correct_option)
        incorrect_option = random.choice(options)
        print(f"We will eliminate two incorrect options: {correct_option} and {incorrect_option}")

    def phone_a_friend(self):
        print("Calling a friend for help... Your friend thinks the answer is:", random.choice(["A", "B", "C", "D"]))


if __name__ == "__main__":
    game = KBCGame()
    game.start_game()
