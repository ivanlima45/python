print("Hello, world! My name is Ivan")
print("Eu vou ficar muito bom em python!!!")

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
print("###################################")
print("str = ", greet)
print("str = " + str(greet) + "  for you all")
print("str = ", greet,  "  for you all")

cost = 3.40
tax = 0.40
print("The price is $",cost, " but I payed $" , cost + tax, " due to taxes ")
name = "Jane"
state = "fine"
local = "website"
print("Hello folks! Welcome to my {}. I hope you are doing just {}!".format(local, state))
f"Hello {name} welcome to my {local}" # does not work
##user_name = input("What's your name, please? ")
user_name = "Maria"
print(f"Hello {user_name}! welcome to my {local}!")
print(f"Hello {user_name.upper()}! welcome to my {local}!")
print(format(2.9999,"f"))
print(format(2.3451,"e"))
print(format(0.42,"%"))
print(format(2.9999,".2f"))
print(format(2.3451,".2e"))
print(format(0.42,".1%"))
print(format(23,'d'))
print(format(23000000000,',d'))

