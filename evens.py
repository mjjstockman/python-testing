def even_number_of_evens(numbers):
    """
    Should Raise a TypeError if a list in not passed into the function
    error message: "A list was not passed into the function"
    if the list is empty it will return False
    if the number of even numbers is odd - return False
    if the numner of even numbers is even - return True
    """
    return True

# only run if file is named __main__ (). Python names any file it runs directly
# as __main__. therefore below code will only run when this file is run, and
# not when the test file is run
if __name__ == '__main__':
    print(even_number_of_evens(5))