# with has built-in implicit exception handling
# close() will be automatically called

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
