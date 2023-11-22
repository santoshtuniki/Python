##### Function

    1.  A function is a block of code which only runs when it is called.

    2.  We can pass data, known as parameters, into a function.

    3.  function can return data as a result.

##  In Python a function is defined using the **def** keyword


##### Arguments

    1.  Information can be passed into functions as arguments.

    2.  Arguments are specified after the function name, inside the parentheses. 

    3.  We can add as many arguments as we want, just separate them with a comma

##### From a function's perspective:

    A parameter is the variable listed inside the parentheses in the function **definition**.

    An argument is the value that is sent to the function when it is **called**.

## The main difference is that "parameters" never change, but "arguments" vary.


##### If a function name is a combination of two/more words, they need to be separated with an underscore_

    Ex: hello_world(), my_function()

##### We could give **default** values in parameters, to avoid error in case if insufficient arguments are sent during function call

    Ex: sum(num1 = 0, num2 = 0)

##### Keyword Arguments

    We can send arguments with the key = value syntax.

    EX: family(child1 = "Emily", child2 = "Tobi", child3 = "Lin")

##### Arbitary Arguments

    1.  If we don't know how many arguments that will be passed into your function, add a (*) before the parameter name in the function definition

    2.  This way the function will receive a "tuple" of arguments

        Ex: sum(*args)

##### Arbitrary Keyword Arguments

    1.  If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

    2.  This way the function will receive a "dictionary" of arguments

        Ex: sum(**args)



## Arbitrary Arguments are often shortened to (*args) in Python documentations.

## Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

#####  function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the "pass" statement to avoid getting an error