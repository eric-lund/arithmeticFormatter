def operator_check(problems):
    n = 0    
    for i in problems:
        if '+' in problems[n]:
            pass
        elif '-' in problems[n]:
            pass
        else:
            raise ValueError("Error: Operator must be '+' or '-'.")
        n += 1    

def remove_spaces(problems):
    no_spaces = str.maketrans({' ': ''})
    result = []
    for i in problems:
        i = str(i)
        problems_without_spaces = i.translate(no_spaces)
        result.append(problems_without_spaces)
    
    return result
        
def get_operands(problems_without_spaces):
    operators = ['+','-']
    operands = []
    left_operand = []
    right_operand = []
    for d in problems_without_spaces:
        for o in operators:
            index = d.find(o)
            if index > 0:
                operands.append(
                    {'left_operand': d[0:index], 
                    'right_operand': d[index + 1:], 
                    'operator': d[index]
                    }
                )
                
    return operands
    

def digit_check(operands):
    for o in operands:
        if o.isdigit() == False:
            raise ValueError('Error: Numbers must only contain digits.')

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        raise ValueError('Error: Too many problems.')

    operator_check(problems)

    problems_without_spaces = remove_spaces(problems)

    print(problems_without_spaces)
    


    

    # number_check(get_operands(problems_without_spaces))


    # problem_dict = {
    #     "first_number": first_number,
    #     "second_number": second_number,
    #     "operand": operand
    #     }


    
    # return problems

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

# number_of_problems(problems)
# operator_check(problems)
# remove_spaces(problems)
arithmetic_arranger(problems)

# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
