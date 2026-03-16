def filter_numbers(numbers, threshold = 0, greater = True):
    if not numbers: #не пустое
        return []
    if greater:
        return[num for num in numbers if num > threshold]
    else:
        return[num for num in numbers if num < threshold]
print(filter_numbers([1, -5, 10, 0, 3], threshold = 0))
print(filter_numbers([-10, -50, 100, 18, 36], threshold = 10))
print(filter_numbers([1, 69, 101, 99, 400], threshold = 100))
ну типа еу
