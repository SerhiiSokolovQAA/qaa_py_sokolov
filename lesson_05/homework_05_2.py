people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
people_records_1 = [
  ('Serhii', 'Sokolov', 36, 'QA Engineer', 'Poltava'),
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
#Point #1
my_record = ('Serhii', 'Sokolov', 36, 'QA Engineer', 'Poltava')
updated_people_records = people_records.insert(0, my_record)
print(f"Updated records: {people_records}")

#Point #2.1
first_record = people_records[1]
fifth_record = people_records[5]
print(f"Record under first index is {first_record}")
print(f"Record under fifth index is {fifth_record}")
del_first_record = people_records.remove(first_record)
del_fifth_record = people_records.remove(fifth_record)
print(f"Records with deleted items {people_records}")
switch_people_records_1 = people_records.insert(1, fifth_record)
switch_people_records_2 = people_records.insert(5, first_record)
print(f"Records with switched items {people_records}.")

#Point #2.2
# от себя -> не сообразил, как записать переменную people_records так,
# что бы оба способа работали одновременно.
# только задавая переменную people_records еще раз

people_records_1[1], people_records_1[5] = people_records_1[5], people_records_1[1]
print(f"Records with switched in another way items : {people_records_1}.")

#Point #3.1
#тут делал на пару с gpt, не получалось вывести именно рекорды из people_records,
# где людям меньше 30-ти лет
indexes_1 = int(input("Select first index: "))
indexes_2 = int(input("Select second index: "))
indexes_3 = int(input("Select third index: "))
indexes = [indexes_1,  indexes_2, indexes_3]
under_30_people = []
required_age = 30
for i in indexes:
    age = people_records[i][2]
    if age < required_age:
        under_30_people.append(people_records[i])
if not under_30_people:
    print("All people at least 30 years old")
else:
  print(f"Not all people is 30 years old.\nPeople under 30 years old:\n{under_30_people}")

#Point #3.2
# тут делал сам
indexes_01 = int(input("Select first index: "))
indexes_02 = int(input("Select second index: "))
indexes_03 = int(input("Select third index: "))
indexes_my = [indexes_01,  indexes_02, indexes_03]
all_over_30 = all(people_records[i][2] >= 30 for i in indexes_my)
if all_over_30:
  print("All people at least 30 years old")
else:
   print("Not all people is 30 years old")