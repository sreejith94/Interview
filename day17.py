def reverse_string(text):
    return text[::-1]
def filter_list(lst):
    result = []

    for item in lst:
        if type(item) == int:
            result.append(item)

    return result
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1

    for i in range(n - 1):
        temp = a + b
        a = b
        b = temp

    return b
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True
def merge_dicts(dict1, dict2):
    result = dict1.copy()

    for key in dict2:
        result[key] = dict2[key]

    return result
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
def aggregate_data(data):

    result = {}

    for dictionary in data:

        for key in dictionary:

            if key not in result:
                result[key] = 0

            result[key] += dictionary[key]

    return result
def is_palindrome(text):

    cleaned = ""

    for char in text:

        if char.isalnum():
            cleaned += char.lower()

    return cleaned == cleaned[::-1]
def sort_by_character_count(strings):
    return sorted(strings, key=lambda word: (len(word), word))