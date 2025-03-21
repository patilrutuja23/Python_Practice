import re

def extract(text):
    pattern = r'\b(\d{2}/\d{2}/\d{4})\b'
    date = re.findall(pattern, text)
    return date

input = "Today is 03/26/2024 and tomorrow is 03/27/2024."
output = extract(input)
print(output)


class BankAccount:
    def __init__(self, initial_balance):
        assert initial_balance >= 0, "Initial balance cannot be negative"
        self.balance = initial_balance
        print("Assertion Passed")

initial_balance = 1000

try:
    account = BankAccount(initial_balance)
except AssertionError:
    print("Assertion Error")
