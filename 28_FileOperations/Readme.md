##### There are four different methods (modes) for opening a file:

    1.  "r"     -->     Read    -->     Default value. Opens a file for reading, error if the file does not exist

    2.  "a"     -->     Append  -->     Opens a file for appending, creates the file if it does not exist

    3.  "w"     -->     Write   -->     Opens a file for writing, creates the file if it does not exist

    4.  "x"     -->     Create  -->     Creates the specified file, returns an error if the file exists

##### In addition, we can specify if the file should be handled as binary or text mode

    1.  "t"     -->     Text    -->      Default value. Text mode

    2.  "b"     -->     Binary  -->      Binary mode (e.g. images)

##### "r" for read, and "t" for text are the default values, we do not need to specify them.

##### read()

    1.  By default the read() method returns the whole text
    
    2.  But we can also specify how many characters we want to return

##### readline()

    By looping through the lines of the file, you can read the whole file, line by line

##### close()

    Always close the file after performing operations

##### remove()

    delete the file