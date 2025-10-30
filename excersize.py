def pdCheck():
    print("Please enter a number (or 'q' to quit)")
    number = input()
    values = []

    while number != 'q':
        values.append(int(number))
        print(values)
        print("Please enter a number (or 'q' to quit)")
        number = input()
    else:
        print("doing calculation...")
        total = sum(values)
        print("Total:", total)


# 3. Which team has the best home point differential this season?
# The best home PD is...

# 4. Which team has the best away point differential this season?
# The best away PD is...

# Uncomment to run
# pdCheck()
