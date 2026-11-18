class Keypad:
    def get_input(self) -> int:
        while True:
            try:
                return int(input())
            except ValueError:
                print("\n[Error: Invalid input. Please type numbers only.]")
                print("Enter your selection/number again: ", end="")
