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
 
    # this prints the first equation in the correct format
    line1 = '{line1: >{padding}}'.format(line1 = problem_list[0][0], padding = problem_list[0][3]+2)
    operator = problem_list[0][1]

    line2 = '{operator:}'.format(operator = problem_list[0][1]) \
        + '{operand2: >{padding}}'.format(operand2 = problem_list[0][2], padding = problem_list[0][3]+1)

    bottom_line = ('-' * int(problem_list[0][3] + 2))
    
    line3 = f'{bottom_line}' + (' ' *4) + f'{bottom_line}'

    print(line1) 
    print(line2)
    print(line3)
    
    top_row = []
    line1 = ''
    bottom_lines = ''
    paddington = ''
    index = 0
    for i in problem_list:
        top_row.append(i[0])
        paddington = (len(i[0]))
        if index == 0:
            line1 += f'{i[0]}' + (' ' * (i[3] + 2))
        else: 
            line1 += ' ' * paddington + f'{i[0]}' #+ (' ' * (i[3] + 2))        
        bottom_lines += ('-' * (i[3] + 2) + (' ' * 4))
        # print((i[3] + 6) - len(str(i[0])), padding)
            

    print(top_row)
    print(line1)
    # print(bottom_lines)
    
    
    # return problems

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

# number_of_problems(problems)
# operator_check(problems)
# remove_spaces(problems)
arithmetic_arranger(problems)    

# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
