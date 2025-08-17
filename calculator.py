logo = r"""
     _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    '+':add,
    '-':sub,
    '*':multiply,
    '/':divide
}
def calculator():
    print(logo)
    should_accumulate = True
    num_1 = float(input("What's the first Number?: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        opr_symbol = input("Pick an Operation:")
        num_2 = float(input("What's the second number?:"))
        answer = operations[opr_symbol](num_1,num_2)
        print(f"{num_1} {opr_symbol} {num_2} = {answer}")

        choice = input(f"Type 'y' to continue calculation with {answer} or Type 'n' to start new calculation. ")

        if choice == 'y':
            num_1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()

