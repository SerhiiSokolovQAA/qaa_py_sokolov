def multiplication_table(number, limit=25):
    results = []
    multiplier = 1
    while True:
        result = number * multiplier
        if result > limit:
            break
        results.append(f"{number}x{multiplier}={result}")
        multiplier += 1
    return results

def add_number(a, b):
    return a + b

def arithmetic(numbers_lst):
    return sum(numbers_lst) / len(numbers_lst)

def reverse_string(s):
    return s[::-1]

def len_count(words):
    return max(words, key=len)

def find_substring(str1, str2):
    return str1.find(str2)

def unic_chars(data_to_check):
    unique_chars = []
    for char in data_to_check:
        if char not in unique_chars:
            unique_chars.append(char)
    return len(unique_chars) > 10

def character_counter(text, character_to_find):
    return sum(1 for i in text if i.lower() == character_to_find.lower())

def find_items_by_type(lst, type_name):
    type_map = {'str': str, 'int': int, 'bool': bool, 'float': float}
    selected_type = type_map.get(type_name)
    if not selected_type:
        raise ValueError("Unknown type")
    return [item for item in lst if isinstance(item, selected_type)]

def employee_list_editor(employee_list, f_name, l_name, age, job_title, city_of_birth):
    new_employee = (
        f_name.capitalize(),
        l_name.capitalize(),
        int(age),
        job_title.capitalize(),
        city_of_birth.capitalize()
    )
    employee_list.insert(0, new_employee)
    return employee_list
