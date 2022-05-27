### Falls under Creational Pattern
1. No control over creation:  
TDD is not possible. As no fresh instance is available for each test.

2. Breaks Separation of Concern:  
As the class is controlling it's instance creating logic along with 
the required functionality, its breaking the single responsibility principle.
    
3. Breaks the dependency Injection principle:  
If dependency changed in one instance, it gets 
changed in all instances. 

#### How to implement:  
1. First Method:
    * Make the constructor private
    * Implement a method to get the object handle
     
2. Second Method
    * Create an inner class
    * from constructor, return the handle to the same 
    object of the inner class