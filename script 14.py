# Conversions

integer = 5
print(integer)
f = float(integer)
print(f)

float_1 = 10.6
integer_1 = int(float_1)
print(float_1)
print(integer_1)
float_2 = -1 * float_1
integer_2 = int(float_2)
print(float_2)
print(integer_2)

# Strings only compatible values
string_value = '2.5'
float_of_string = float(string_value)
print(string_value)
print(float_of_string)

# Vise versa
integer_3 = 25
string_of_integer = str(integer_3)
print(integer_3)
print(string_of_integer)

# But non compatible generates error
string = '1p'
print("ERROR: integer_of_string = int(string)")
print(string)

# Converting sequences
list_1 = [1, 2, 3]
print(list_1)
set_1 = set(list_1)
print(set_1)
tuple_1 = tuple(set_1)
print(tuple_1)
tuple_2 = tuple(list_1)
print(tuple_2)
string_3 = 'hello'
list_3 = list(string_3)
print(string_3)
print(list_3)

# Converting dictionaries only with sequence within sequence
list_a = [1, 2]
list_b = [3, 4]
list_ab = [list_a, list_b]
print(list_a, list_b, list_ab)
dict_ab = dict(list_ab)
print(dict_ab)
tuple_a = (5, 6)
tuple_b = (7, 8)
list_t = [tuple_a, tuple_b]
print(list_t)
dict_lt = dict(list_t)
print(dict_lt)
