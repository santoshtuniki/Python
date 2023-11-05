### len()

    Length of the string


## MODIFY STRINGS

### lower()

    Converts string to lowercase

### upper()

    Converts string to uppercase

### capitalize()

    Converts the first character to upper case

### replace(previous, latest, count<Optional>)

    Return a copy with all occurrences of substring old replaced by new

        1. Replaces the word <previous> with <latest> in string

        2. If count = 1, replace only the firt occurence   
        
        3. By  default, count = -1 => Replace all

### title()

    Returns a string where the first character in every word is upper case.

        1. If the word contains a number or a symbol, the first letter after that will be converted to upper case.

        2. Note that the first letter after a non-alphabet letter is converted into a upper case letter:

### split([char])

    Returns a list where the text between the specified separator becomes the list items

        1. a = "Hello, World!"
        
           print(a.split(","))      #   returns ['Hello', ' World!']

### strip([chars])

    Return a copy of the string with the leading and trailing characters(if None, whitespaces) removed

        1. multiline.strip()   =>     Remove start and end whitespaces

        2. multiline.strip('cmowz.')     => Remove 'c', 'm', 'o', 'w', 'z', '.' characters from beginning and end

### lstrip([chars])

    Return a copy of the string with leading characters removed.

### rstrip([chars])

    Return a copy of the string with trailing characters removed.


### center(width, [fillchar])

    Return centered in a string of length width

        1. Padding is done using the specified fillchar, (if None, with whitespaces)

### ljust(width, [fillchar])

### rjust(width, [fillchar])


## INDEXING

### str[index]

    Returns character present at index

### str[-1]

    Returns character at end of the string


## SLICING

### str[a:b]

    Returns a str with characters including from index[a] to index[b] excluding index[b]

### str[a:]

    Returns a str with characters including from index[a] to end

### str[:b]

    Returns a str with characters including from start to index[b]



### startswith(prefix)

    Return True if string starts with the prefix, otherwise return False

### endswith(suffix)

    Return True if string ends with the suffix, otherwise return False
