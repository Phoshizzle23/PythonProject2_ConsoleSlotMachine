###########################################
### Python | Slot Machine Project | MK2 ###
###########################################
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

SYMBOL_VALUES = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


class SlotMachine:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        """
        Prompt the user to deposit funds into the slot machine balance.
        """
        while True:
            amount = input("What amount would you like to deposit? $: ")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    break
                else:
                    print("Amount must be greater than 0!!!")
            else:
                print("Please enter a number!!!")
        self.balance += amount

    def get_number_of_lines(self):
        """
        Prompt the user to enter the number of lines they want to bet on.
        """
        while True:
            lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= MAX_LINES:
                    break
                else:
                    print("Enter a valid number of lines!!!")
            else:
                print("Please enter a number!!!")
        return lines

    def get_bet(self):
        """
        Prompt the user to enter the amount they want to bet on each line.
        """
        while True:
            amount = input(f"What amount would you like to bet on each line? (${MIN_BET}-${MAX_BET}): ")
            if amount.isdigit():
                amount = int(amount)
                if MIN_BET <= amount <= MAX_BET:
                    break
                else:
                    print(f"Amount must be between ${MIN_BET} - ${MAX_BET}!!!")
            else:
                print("Please enter a number!!!")
        return amount

    def spin(self, lines, bet):
        """
        Simulate a spin of the slot machine and calculate the winnings.
        """
        total_bet = bet * lines

        if total_bet > self.balance:
            print(f"You do not have enough funds to bet that amount, your current balance is: ${self.balance}")
            return 0

        print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

        slots = self.get_slot_machine_spin(ROWS, COLS, SYMBOL_COUNT)
        self.print_slot_machine(slots)
        winnings, winning_lines = self.check_winnings(slots, lines, bet, SYMBOL_VALUES)

        if winnings > 0:
            print(f"🤑💲💲💲🤑You won ${winnings}.🤑💲💲💲🤑")
            print("You won on:", *winning_lines)
        else:
            print(f"☠💸💸💸☠You lost ${total_bet}.☠💸💸💸☠")

        return winnings - total_bet

    def get_slot_machine_spin(self, rows, cols, symbols):
        """
        Generate a random spin of the slot machine with the specified number of rows and columns.
        """
        all_symbols = []
        for symbol, symbol_count in symbols.items():
            for _ in range(symbol_count):
                all_symbols.append(symbol)

        columns = []
        for _ in range(cols):
            column = random.sample(all_symbols, rows)
            columns.append(column)

        return columns

    @staticmethod
    def print_slot_machine(columns):
        """
        Print the current state of the slot machine.
        """
        for row in range(len(columns[0])):
            print(" | ".join(column[row] for column in columns))

    @staticmethod
    def check_winnings(columns, lines, bet, values):
        """
        Check the winnings for each line based on the spin result.
        """
        winnings = 0
        winning_lines = []
        for line in range(lines):
            symbol = columns[0][line]
            for column in columns:
                symbol_to_check = column[line]
                if symbol != symbol_to_check:
                    break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)

        return winnings, winning_lines

    def play_game(self):
        """
        Main game loop to manage the gameplay.
        """
        self.deposit()
        while True:
            print(f"Current balance is: ${self.balance}")
            answer = input("Press enter to play (Q to quit!): ")
            if answer.lower() == "q":
                break
            bet = self.get_bet()
            lines = self.get_number_of_lines()
            winnings = self.spin(lines, bet)
            self.balance += winnings

        print(f"You left with ${self.balance}")


def main():
    slot_machine = SlotMachine()
    slot_machine.play_game()


if __name__ == "__main__":
    main()

