file = open("example.txt","r")
content = file.read()  # Reads the entire content
line = file.readline()  # Reads a single line
lines = file.readlines()  # Reads all lines into a list
# Use print() for one each method above by commenting others
file.close()