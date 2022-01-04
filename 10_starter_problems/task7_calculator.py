def calculator(a, operator, b):
    supported_operators = ['+', '-', '*', '/']
    if operator in supported_operators:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b
    else:
        return 'not supported'
