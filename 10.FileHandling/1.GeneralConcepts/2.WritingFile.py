# It will overwrite the file if already exists
with open('example_1.txt', 'w') as f:
    f.write("Hello, World!\n")
# 'x' can be used to get a warning if the file already exists

# It will add content to existing file and create new if file doesn't exist
with open('example_1.txt', 'a') as f:
    f.write("Appending some more text.")

