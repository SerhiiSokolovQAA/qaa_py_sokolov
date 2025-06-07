from itertools import count


#Solution #1
number_lst_1 = [1, 2, 4, 33, 9]
even_lst = 0
for even_number in number_lst_1:
    if even_number % 2 == 0:
        even_lst += even_number

print(f"Sum of even numbers: {even_lst}") #:

#Solution #2
number_lst_2 = [1, 1, 11, 11, 9]
even_lst_2 = []
for even_number in number_lst_2:
    if even_number % 2 == 0:
        even_lst_2.append(even_number)
        count(sum(even_lst_2))
print(f"Sum of even numbers: {sum(even_lst_2)}") #: