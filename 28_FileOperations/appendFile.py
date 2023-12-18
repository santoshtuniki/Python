# Append - creates the file if it doesn't exist

f = open('names.txt', 'a')
f.write('\nNeil')
f.close()

f = open('names.txt')
print(f.read())
f.close()