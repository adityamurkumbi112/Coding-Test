#3. Write a Python function to count the occurrences of a specific element in a list.

def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Example usage
sample_list = [1, 2, 3, 4, 2, 2, 5, 2]
element_to_count = 2
occurrences = count_occurrences(sample_list, element_to_count)
print(occurrences)

# Output: 4
