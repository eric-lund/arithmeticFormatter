def problem_limit_check(list_length):
    if list_length > 5:
        raise ValueError('Error: Too many problems.')

def operator_check(problems):
    #rewrite this to use new listy list
    n = 0    
    for i in problems:
        if '+' in problems[n]:
            pass
        elif '-' in problems[n]:
            pass
        else:
            raise ValueError("Error: Operator must be '+' or '-'.")
        n += 1    

# needed??
def remove_spaces(problems):
    no_spaces = str.maketrans({' ': ''})
    result = []
    for i in problems:
        i = str(i)
        problems_without_spaces = i.translate(no_spaces)
        result.append(problems_without_spaces)
    
    return result
        
def get_operands(problems):
    problem_split = []
    for i in problems:
        problem_split.append(i.split())

    return problem_split

def operand_length_check(operands_list):
    for index, value in operands_list:
        if len(index) > 4 or len(value) > 4:
            raise ValueError('Error: Numbers cannot be more than four digits.')
        else: return

def digit_check(operands):
    for o in operands:
        if o.isdigit() == False:
            raise ValueError('Error: Numbers must only contain digits.')

def arithmetic_arranger(problems, show_answers=False):

    problems_without_spaces = remove_spaces(problems)  # needed??
    operands_list = get_operands(problems_without_spaces) #needed?

    problem_list = get_operands(problems)

    # Error checks
    problem_limit_check(len(problems))
    operator_check(problems)    # rewrite this one


    # digit_count = len(operands_list[0][0]) + len(operands_list[0][1])
    # for i in operands_list:
    # line1 = '{:>9}    {:>8}\n'.format(operands_list[0][0], operands_list[1][0])
    # line2 = '{:>8}    {:>8}\n'.format(operands_list[0][1], operands_list[1][1])
    # print(line1, line2)


    problem_list = get_operands(problems)
    operands_list = get_operands(problems)  # duplicate naming
    for index, value in enumerate(operands_list):
        if '+' in value:
            operands_list[index].remove('+')
        if '-' in value:
            operands_list[index].remove('-')

    operands_len_digits = [[len(item) for item in element] for element in operands_list]

    operands_max = list(map(max, operands_len_digits))

    for index, value in enumerate(problem_list):
        problem_list[index].append(operands_max[index])

    operand_length_check(operands_list)
    # print(problem_list)   
    # return problems

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

# number_of_problems(problems)
# operator_check(problems)
# remove_spaces(problems)
arithmetic_arranger(problems)


# create a list of letters
# my_list = ["blue", "red", "green", "orange", "yellow", "purple"]

# for index, value in enumerate(my_list):
#     # if index is even or the length of the value is less than 5
#     # replace the value with an asterisk
#     if index % 2 == 0 or len(value) < 5:
#         my_list[index] = "*"

# print(my_list)
            

# print(operands_list)
# print(operands_list_digits)
# print(operands_max)
    

# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
