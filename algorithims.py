def reverse_numbers(numbers):
    if not numbers:
        return []

    return numbers[::-1]  # This reverses the list using slicing


if __name__ == "__main__":
    sample_list = [10, 45, 2, 99, 23, 87]
    reversed_list = reverse_numbers(sample_list)
    print("Reversed list:", reversed_list)
