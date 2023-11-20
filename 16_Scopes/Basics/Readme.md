### Scope refers to limiting a variable to be available inside the region it is created.

### A variable created inside a function belongs to the ***local*** scope of that function, and can only be used inside that function.

### A variable created in the main body of the Python code is a ***global*** variable and belongs to the global scope.

### Global variables are available from within any scope, global and local.

### If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables:

    1.  one available in the global scope (outside the function) and 
    
    2.  one available in the local scope (inside the function)

### Inside a function local variables are prioritized over the global variables.

### We try to limit variables to local scope and minimized the use of global scope variables as far as it's possible.