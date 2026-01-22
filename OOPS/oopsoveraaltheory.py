# Object-Oriented Programming in Python is based on Class, Object, Encapsulation, Inheritance, Polymorphism, and Abstraction.
#
# A class is a blueprint that defines variables and methods, and an object is an instance of that class.
# In automation, for example, a LoginPage class contains locators and actions, and the test creates an object of that class to perform login.
#
# Encapsulation means wrapping data and methods inside a class and restricting direct access to data.
# In automation, sensitive data like passwords or tokens are kept as private variables, and accessed only through methods to avoid misuse.
#
# Inheritance allows one class to reuse methods of another class.
# In automation, a BaseTest class contains browser setup and teardown, and test classes inherit it instead of duplicating code.
#
# Polymorphism allows the same method or function to behave differently based on the object or data type.
# In automation, the same click() method works for buttons, links, or icons, and functions like len() work for strings, lists, or collections.
#
# Abstraction hides implementation details and exposes only required functionality.
# In automation, test cases call methods like login() without knowing how elements are located internally. This improves readability and maintainability.
#
# Method overriding is when a child class provides its own implementation of a parent method.
# In automation, different browsers can override a common launch_browser() method.
#
# Overall, OOPS helps make automation frameworks reusable, maintainable, scalable, and easy to understand.