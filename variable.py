a = b = 2  # This is called a "chained assignment".
# It assigns the value 2 to variables "a" and "b".
print("a = " + str(a))
# We'll explain the expression str(a) later in the course.
# For now it is used to convert the  variable "a" to a string.
print("b = " + str(b))

greetings = "greetings"
print("greetings = " + str(greetings))
greetings = "bom dia"
print("greetings = " + str(greetings))
print("a = ", a)
print("b = ", b)
greet = 200
print("str = ", str(greetings))
print("str = ", str(greet))

variable = 1
print(a)


## Variable types

number = 9
print(type(number))   # print type of variable "number"

float_number = 9.0
print(type(float_number))


number = 9
print(type(number))   # print type of variable "number"

float_number = 9.0
print(float_number)
print(int(float_number))


number = 9.0        # float number
result = number/2.0
remainder = number%2.0
print("result = " + str(result))
print("remainder = " + str(remainder))


number = 9.0
print("number = " + str(number))

number -= 2
print("number = " + str(number))

number += 5

print("number = " + str(number))



two = 2
three = 3

is_equal = two == three

print(is_equal)


one = 1
two = 2
three = 3

print(one < two < three)  # This chained comparison means that the (one < two) and (two < three) comparisons are performed at the same time.

is_greater = three > two
print(is_greater)



