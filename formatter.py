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
    operands_list = [[] for i in range(len(problems_without_spaces))]
    i = 0
    for d in problems_without_spaces:
        for o in operators:
            index = d.find(o)
            if index > 0:
                operands_list[i].append(d[0:index])
                operands_list[i].append(d[index + 1:])
                operands_list[i].append(d[index])
                i += 1

    return operands_list

def operand_length_check(operands):
    # combined_operands = dict(operands,)
    # combined_operands = filter(lambda o: operands['operator'] != 'operator', operands.item)
    for key, val in operands.item():
        pass
    print(operands)


def digit_check(operands):
    for o in operands:
        if o.isdigit() == False:
            raise ValueError('Error: Numbers must only contain digits.')

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        raise ValueError('Error: Too many problems.')

    operator_check(problems)
    problems_without_spaces = remove_spaces(problems)
    
    operands_dictionary = get_operands(problems_without_spaces)

    # print(type(operands))
    # operand_length_check(get_operands(problems_without_spaces))
    print(problems_without_spaces)
    print(operands_dictionary)

    #print(operands)    


    


    

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
