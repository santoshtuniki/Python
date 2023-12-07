##### Python is an object oriented programming language.

##### A Class is like an object constructor, or a "blueprint" for creating objects.

#### self

    1.  A reference to the current instance of the class
    
    2.  Used to access variables that belongs to the class.

    3.  Does not have to be named 'self' , you can call it whatever you like.
    
    4.  But it has to be the "first parameter" of any function in the class

#### __init__()

    1.  Executed on initiation of every class.

    2.  Called automatically every time the class is being used to create a new object.

    3.  Used to assign values to object properties, when the object is being created.

##### __str__()

    1.  Controls what should be returned when the class object is represented as a string

    2.  If not set, the string representation of the object is returned

##### Delete properties on objects by using the 'del' keyword

        del car.make

##### Delete objects by using the del keyword

        del car

##### pass

    1.  class definitions cannot be empty.
    
    2.  But if you for some reason have a class definition with no content, put in the "pass" statement to avoid getting an error
