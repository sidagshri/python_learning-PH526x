filename = "input.txt"

for line in open(filename):
    print(line)

# without extra new line
for line in open(filename):
    print(line.rstrip())

# with optional assignment to retain resulted immutable string
for line in open(filename):
    line = line.rstrip()
    print(line)

# splitting each line around white spaces
for line in open(filename):
    line = line.rstrip().split(" ")
    print(line)

f = open("output.txt", "w")
f.write("Python")
f.close()

# writing to file without newline character
f = open("output_01.txt", "w")
for x in range(10):
    line = "line " + str(x)
    f.write(line)
f.close()

# writing to file with newline character
f = open("output_02.txt", "w")
for x in range(10):
    line = "line " + str(x) + "\n"
    f.write(line)
f.close()
