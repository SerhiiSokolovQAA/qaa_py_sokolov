#task 01
alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
print(alice_in_wonderland)
#task 02
print("apostrophes in text above: ")
apostrophe_count = 0
for character in alice_in_wonderland:
    if character == "'":
        print(character)
        apostrophe_count = apostrophe_count + 1

print(f"Total count of the apostrophes is: {apostrophe_count}")
##task 03
print("\nFull Text:\n")
print(alice_in_wonderland)

# task 04
bl_see_sqr = 436402
az_see_sqr = 37800
ttl_sqr = bl_see_sqr + az_see_sqr
print(f"Total square is: {ttl_sqr}")

# task 05
total_goods = 375291
first_and_second = 250449
second_and_third = 222950
only_first = total_goods - second_and_third
print(f"Total count of the goods on the first warehouse: {only_first}")
only_second = first_and_second - only_first
print(f"Total count of the goods on the second warehouse: {only_second}")
only_third = second_and_third - only_second
print(f"Total count of the goods on the third warehouse: {only_third}")
sum_up_goods = only_first + only_second + only_third
if sum_up_goods != total_goods:
    print(f"Calculations are incorrect!\nTotal goods: {total_goods}\nCounted goods: {sum_up_goods}")

# task 06
loan_duration = 18
monthly_payment = 1179
pc_cost = monthly_payment * loan_duration
print(f"Price is: {pc_cost}")

# task 07
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(a, b, c, d, e, f)

# task 08
pizza_l_ttlcost = 274 * 4
pizza_m_ttlcost = 218 * 2
juice_ttlcost = 35 * 4
cake_ttlcost = 350 * 1
water_ttlcost = 21 * 3
ttal_cost = (pizza_l_ttlcost +
             pizza_m_ttlcost +
             juice_ttlcost +
             cake_ttlcost +
             water_ttlcost)
print(f"Total sum is: {ttal_cost} grn" )

# task 09
photo_count = 232
page_capacity = 8
pgs_to_fit_all_photos = photo_count // page_capacity
print(pgs_to_fit_all_photos)

# task 10
distance = 1600
fuel_for_hundrt_km = 9
total_fuel_needed = distance // 100 * fuel_for_hundrt_km
fuel_tank_capacity = 48
refuel_tank = total_fuel_needed // fuel_tank_capacity
print(f"Total fuel needed for the full trip: {total_fuel_needed}")
print(f"Family will need to stop at the gas station {refuel_tank - 1} times if the tank was full before the trip.\n"
      f"Family will need to stop at the gas station {refuel_tank} times if the tank was empty before the trip.")
