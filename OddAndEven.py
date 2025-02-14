#Drake Pierce-Demski
#

def find_missing_numbers(numbers):
    if not numbers:
        return []
    
    smallest = min(numbers)
    largest = max(numbers)
    full_range = set(range(smallest, largest + 1))
    missing_numbers = full_range - set(numbers)
    
    return sorted(list(missing_numbers))

# Example usage
numbers = [1, 3, 4, 7]
result = find_missing_numbers(numbers)
print("Missing numbers:", result)  # Output: Missing numbers: [2, 5, 6]

def extract_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = extract_even_numbers(numbers)
print("Even numbers:", result)  # Output: Even numbers: [2, 4, 6, 8]