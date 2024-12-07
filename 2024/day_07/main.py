from itertools import product


# Function to evaluate an expression from left to right without operator precedence
def evaluate_left_to_right(expression):
    tokens = expression.split()
    result = tokens[0]  # Start with the first number

    # Process each operator and operand sequentially
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = tokens[i + 1]

        if operator == "||":
            result = eval(str(result) + operand)
        elif operator == "+":
            result = eval(str(result) + "+" + operand)
        elif operator == "*":
            result = eval(str(result) + "*" + operand)

    return result


# List of lists with numbers as strings
with open("./input", "r") as f:
    list_of_lists = []
    answers = []
    for line in f:
        line = line.split()
        answers.append(int(line[0][0:-1]))
        list_of_lists.append(line[1:])


operators = ["+", "*", "||"]

# Iterate over each sublist to generate and evaluate expressions
total = 0
for idx, L in enumerate(list_of_lists):
    # Generate all possible combinations of operators for the given list length - 1
    operator_combinations = product(operators, repeat=len(L) - 1)

    expressions = []
    results = []

    # Create and evaluate all possible expressions using the combinations of operators
    for ops in operator_combinations:
        expr = L[0]
        for i in range(1, len(L)):
            expr += f" {ops[i - 1]} {L[i]}"
        
        expressions.append(expr)
        results.append(evaluate_left_to_right(expr))
        
        if evaluate_left_to_right(expr) == answers[idx]:
            # print(answers[idx])
            total += answers[idx]
            break

    # Print all expressions with their evaluation results
    # print(f"Expressions for list {idx + 1}:")
    # for i, (expression, result) in enumerate(zip(expressions, results), 1):
    #     print(f"{i}) {expression} = {result} | answer = {answers[idx]}")
    # print()  # Newline for better readability

print(total)
