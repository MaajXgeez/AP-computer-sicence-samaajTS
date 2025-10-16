def find_largest_number(numbers):  
    if not numbers:
        return None  # or raise an exception, or handle it however you like

    max_num = numbers[0]  # Step 2
    for num in numbers[1:]:  # Step 3
        if num > max_num:  # Step 4
            max_num = num
    return max_num  # Step 5 (moved outside the loop)

if __name__ == "__main__":
    sample_list = [10, 45, 2, 99, 23, 87]
    print("The largest number is:", find_largest_number(sample_list))
