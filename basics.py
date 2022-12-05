"""
    Python is both a functional and an object-oriented programming language. Functions define its
    functional nature while classes an objects constitute of its object nature
"""

if __name__ == '__main__':
    my_name = 'charles'  # Strings are denoted using double, single or triple quotations
    my_age = 11  # integers are denoted as plain numbers
    my_salary = 1000000
    """
        Python consists of 5 known data types
            1. Numbers - These are numeric values and are further categorised into four, - Integers, long, float and complex
                        - Integers store whole numbers either negative or positive
                        - Long has more bytes compared to an integer. Integers store 32 bits while long stores 64 bits. 
                          Denoted with a capital L to distinguish it from an integer.
                        - Float stores decimal numbers.
            2.Strings - A sequence of characters enclosed in double or single quotations
            3.Tuples - Store multiple elements together enclosed in parenthesis. It is ussually read Only. Once created can't 
            4. List - Stores multiple elements together enclosed in square brackets. The elements can be of different data type.
            5. Dictionary - Stores key value elements
    """

    my_names = ['charles', 'muvaka', 'kata']  # This is a list of items
    first_name = my_names[0]
    middle_name = my_names[1]
    last_name = my_names[2]

    print(first_name)
    print(middle_name)
    print(last_name)

    my_languages = ('java', 'C#', 'python', 'kotlin')  # This is a tuple.. Read only. Cannot be altered

    priority = {  # this is a dictionary, used in storing key value pairs, We access this elements using their keys
        1: my_languages[0],
        2: my_languages[3],
        3: my_languages[1],
        4: my_languages[2]
    }

    print(priority[1])
