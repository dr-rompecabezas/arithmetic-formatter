def arithmetic_arranger(problems, *solution):

    if len(problems) > 5:
        error = 'Error: Too many problems.'
        return error

    arranged_problems = ''
    first_line = ''  # left operand
    second_line = ''  # operator and right operand
    third_line = ''  # dashes
    fourth_line = ''  # result (optional)

    def dash_generator(num):
        dashes = ''
        for x in range(num):
            dashes = dashes + '-'
        return dashes

    def offset(num):
        spaces = ''
        for x in range(num):
            spaces = spaces + ' '
        return spaces

    def is_not_number(str):
        try:
            float(str)
        except ValueError:
            return True

    def calculate_result(a, operator, b):
        if operator == '+':
            return int(a) + int(b)
        elif operator == '-':
            return int(a) - int(b)

    for problem in problems:

        problem_components = problem.split()
        left_operand = problem_components[0]
        operator = problem_components[1]
        right_operand = problem_components[2]

        if operator == '+' or operator == '-':
            if is_not_number(left_operand) or is_not_number(right_operand):
                error = "Error: Numbers must only contain digits."
                return error
            elif len(left_operand) > 4 or len(right_operand) > 4:
                error = "Error: Numbers cannot be more than four digits."
                return error
            else:
                longest_operand_length = len(left_operand)
                if len(right_operand) > longest_operand_length:
                    longest_operand_length = len(right_operand)
                max_length = longest_operand_length + 2
                result = str(calculate_result(left_operand, operator, right_operand))
                result_length = len(result)
                if result.startswith('0'):
                    result_length = result_length - 1

                first_line = first_line + \
                    offset(
                        max_length - len(left_operand)) + left_operand + offset(4)

                second_line = second_line + operator + offset(
                    max_length - 1 - len(right_operand)) + right_operand + offset(4)

                third_line = third_line + dash_generator(max_length) + offset(4)

                fourth_line = fourth_line + offset(max_length - result_length) + result + offset(4)
        else: 
            error = "Error: Operator must be '+' or '-'."
            return error
        
    # Concatenate
    arranged_problems = arranged_problems + first_line.rstrip() + '\n' + \
        second_line.rstrip() + '\n' + third_line.rstrip()

    # Concatenate result line if optional argument is passed
    if solution:
        arranged_problems = arranged_problems + '\n' + fourth_line.rstrip()

    return arranged_problems