# number to string

decade = str(2000)
print(type(decade))         #   <class 'str'>

# string to number

zipcode = '10001'
zipValue = int(zipcode)
print(type(zipValue))       #   <class 'int'>

# Error if attempt to cast incorrect value
# zip = int("New York")       #   ValueError: invalid literal for int() with base 10: 'New York'
