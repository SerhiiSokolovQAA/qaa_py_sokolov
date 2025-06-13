from itertools import count

# task 1
def multiplication_table(number):
    multiplier = 1

    while True: # еще можно указать while multiplier <= 25, но как то "криво" выглядит
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1
multiplication_table(3)

#task 2
a = (int(input("Enter first number: ")))
b = (int(input("Enter second number: ")))
def add_number(a, b):
    return a + b
print(f"Result is: {a + b}")

# task 3
numbers_lst = [4, 5, 4, 10]
def arithmetic(numbers_lst):
    count(sum(numbers_lst))
    return sum(numbers_lst) / len(numbers_lst)
print(f"Result is: {sum(numbers_lst) / len(numbers_lst)}")

# task 4
some_text = "Some Text"
def reverse_string(s):
    return s[::-1]
text_to_revers = reverse_string(some_text.lower())
print(f"Text is: {text_to_revers}")

# task 5
words_lst = ("first", "second", "third", "longest in the list")
def len_count(words):
    longest_word = max(words, key=len)
    return longest_word
longest_counter = len_count(words_lst)
print(f"Longest is: '{longest_counter}'")

# task 6
def find_substring(str1, str2):
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

# task 7
def unic_chars(data_to_ckeck):
    unique_chars = []
    for char in data_to_ckeck:
        if char not in unique_chars:
            unique_chars.append(char)
    if len(unique_chars) > 10:
        print(True)
    else:
        print(False)
    return data_to_ckeck

# task 8
some_var = input("Enter your data: ")
results_are = unic_chars(some_var)

def character_counter(character):
    character_to_find = input("Enter your text: ")
    character_count = 0
    for i in character:
        if i == character_to_find.lower():
            character_count += 1
    return character_count

text_for_text = "asd ffererer"
c = character_counter(text_for_text)
print(c)

# task 9
def find_items_by_type(lst):
    type_input = input("Enter the type you want to find (str, int, bool, float): ")
    type_map = {'str': str, 'int': int, 'bool': bool, 'float': float}
    selected_type = type_map[type_input]
    result = []
    for item in lst:
        if isinstance(item, selected_type):
            result.append(item)
    print(f"Items of type '{type_input}': {result}")
    return result

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
find_items_by_type(lst1)

# task 10
employee_list = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago')]

def employee_list_editor(lst):
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    job_title = input("Enter job title: ")
    city_of_birth = input("Enter city of birth: ")
    new_employee = (f_name.capitalize(), l_name.capitalize(), int(age), job_title.capitalize(), city_of_birth.capitalize())
    employee_list.insert(0, new_employee)
    return employee_list

updated_employee_list = employee_list_editor(employee_list)
print(updated_employee_list)