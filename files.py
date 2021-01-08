f = open("input.txt", "r")   # here we open file "input.txt". Second argument used to identify that we want to read file
                             # Note: if you want to write to the file use "w" as second argument

for line in f.readlines():   # read lines
    print(line)

f.close()                    # It's important to close the file to free up any system resources.

print("########################################")

print("Now I will print only the first line of the input file")

f = open("input.txt", "r") 

print(f.readline())
f.close() 