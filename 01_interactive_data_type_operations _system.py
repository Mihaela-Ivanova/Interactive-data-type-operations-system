while True:
    # Prompt the user to choose a data type to perform operations on
    print("Choose a data type to perform operations on:")
    print("1. Strings")
    print("2. Numbers")
    print("3. Booleans")
    print("4. Additional Data Types (List, Tuple, Dictionary)")

    # Get the user's choice and store it in a variable
    choice = input("Enter the number of your choice (1-4): ")

    # If the user chooses Strings (choice == '1'):
    if choice == '1':
        # Declare a string variable, e.g., sentence = "Learning Python is fun!"
        sentence = "Learning Python is fun!"
        # Extract and print a substring, such as the word "Python" from the sentence.
        sub_sent = sentence[9:15]
        print(sub_sent)
        # Convert the entire sentence to uppercase and print it.
        print(sentence.upper())
        # Replace a word in the sentence (e.g., replace "fun" with "awesome") and print the modified sentence.
        print(sentence.replace('fun', 'awesome'))

    # If the user chooses Numbers (choice == '2'):
    elif choice == '2':
        # Prompt the user to input two numbers, e.g., num1 and num2.
        print("Please enter two numbers:")
        first_number = input('Please enter to first number: ')
        second_number = input('Please enter to second number: ')
        # Perform and print the results of addition, subtraction, multiplication, and division.
        print(f'The addition of the two equals: {float(first_number) + float(second_number)}')
        print(f'Subtrackting them equals: {float(first_number) - float(second_number)}')
        print(f'If you multiply them you will get: {float(first_number) * float(second_number)}')
        if second_number != '0':
            print(f'If you divide them the result is: {float(first_number) / float(second_number)}')
        # Handle division by zero (e.g., print an error message if num2 is zero).
        else:
            print('Would show you division but yous second num is 0, sorry')
        # Perform a power operation, raising num1 to the power of num2, and print the result.
        print(
            f'And now here is {float(first_number)} to the power of {float(second_number)}: {float(first_number) ** float(second_number)}')

    # If the user chooses Booleans (choice == '3'):
    elif choice == '3':
        # Declare two boolean variables, e.g., is_python_fun = True, is_sunny = False.
        is_python_fun = True
        is_sunny = False
        a = 10
        b = 5
        # Perform and print the results of logical operations: AND, OR, NOT.
        if is_python_fun == True and is_sunny == False:
            print("Python do be fun, but it's not that sunny outside")
        if is_python_fun == True or is_sunny == True:
            print('Python might be funny, might be not, who knows')
        if not is_sunny:
            print("It's cloudy boy")
        # Perform and print the results of comparison operations (e.g., 10 > 5 and 5 == 5).
        if a > b:
            print(is_python_fun)
        else:
            print(is_sunny)

    # If the user chooses Additional Data Types (choice == '4'):
    elif choice == '4':
        # ### List Operations ###
        # Create a list with mixed data types (e.g., numbers, strings, booleans).
        text = [4, '100', True, False]
        print(text)
        # Append a new element to the list and print the updated list.
        text.append("apple")
        print(text)
        # Access and print the 4th element in the list.
        print(text[3])

        # ### Tuple Operations ###
        # Create a tuple with some string elements (e.g., fruits).
        fruits = ('apple', 'banana', 'grape')
        print(fruits)
        # Print the length of the tuple.
        print(len(fruits))
        # Try to modify one element in the tuple and handle the resulting TypeError.
        try:
            fruits[0] = 'pear'
        except TypeError:
            print('Тuple content cannot be modified, sorry')

        # ### Dictionary Operations ###
        # Create a dictionary with some key-value pairs (e.g., name, age, city).
        book = {'name': 'Pesho', 'age': '17', 'sity': 'Sofia'}
        print(book)
        # Access and print the value for one of the keys (e.g., "age").
        print(book.get('age'))
        # Add a new key-value pair to the dictionary and print the updated dictionary.
        book.update({"apple": "fruit"})
        print(book)

    # If the user enters an invalid choice:
    else:
        # Print an error message indicating an invalid selection.
        print('Тhe choice is only from 1 to 4')

    a = input('Wanna try again(Y/N): ')
    if a.upper() == 'Y':
        continue
    elif a.upper() == 'N':
        break
    else:
        while a != 'Y' or a != 'N':
            print('Incorrect choice!')
            a = input('Wanna try again(Y/N): ')
            continue
