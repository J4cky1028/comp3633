def decorator_function(original_function):
    def wrapper_function():
        print("Before the function execution")
        result = original_function()
        print("After the function execution")
        return result
    return wrapper_function

@decorator_function
def greet():
    print("Hello World!")

# myfunc = greet
# myfunc()
# output: Hello World!

# myfunc = decorator_function(myfunc)
# myfunc()
# output: 
# Before the function execution
# Hello World!
# After the function execution
