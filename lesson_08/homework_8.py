data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def data_input():
    first_part = input("Enter first part of the data: ")
    second_part = input("Enter second part of the data: ")
    third_part = input("Enter second third of the data: ")
    final_data = [first_part, second_part, third_part]
    return final_data

def get_int_from_string(i):
    try:
        numbers = [int(x.strip()) for x in i.split(',')]
        return sum(numbers)
    except ValueError:
        return "Can't do it"

def process_data(data_list):
    for item in data_list:
        result = get_int_from_string(item)
        print(result)

process_data(data_input())
process_data(data)