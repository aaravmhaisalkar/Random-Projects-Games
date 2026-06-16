def number_until_x(x):
    list = []
    for i in range (x+1):
        list.append(i)
    return list

def convert_list_to_string(list):
    str = ''
    for i in list:
        str += f'{i}, '
    return str[:-2]