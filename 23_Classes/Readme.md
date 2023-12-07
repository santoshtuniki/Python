##### Inheritance allows us to define a class that inherits all the methods and properties from another class.

##### **Parent** class is the class being inherited from, also called "base" class.

##### **Child** class is the class that inherits from another class, also called "derived" class.

##### To create a class that inherits the functionality from another class, send the "parent class as a parameter" when creating the child class.

##### super()

    1.  When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

    2.  The child's __init__() function overrides the inheritance of the parent's __init__() function.

    3.  super() makes the child class inherit all the methods and properties from its parent.

##### 
