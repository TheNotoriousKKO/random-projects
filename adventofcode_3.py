import re

def find_muls():
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    with open('input.txt', 'r') as file:
        text = file.read()
    matches = re.findall(pattern, text)
    numbers = [(int(num1), int(num2)) for num1, num2 in matches]
    results = [num1 * num2 for num1, num2 in numbers]
    print("Sum of results:", sum(results))

def find_dos():
    with open('input.txt', 'r') as file:
        text = file.read()
    parts = text.split("do()")
    processed_parts = []
    for part in parts:
        if "don't()" in part:
            processed_part = part.split("don't()")[0]
            processed_parts.append(processed_part)
        else:
            processed_parts.append(part)
    result = ''.join(processed_parts)
    pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
    matches = re.findall(pattern, result)
    numbers = [(int(num1), int(num2)) for num1, num2 in matches]
    results = [num1 * num2 for num1, num2 in numbers]
    print("Multiplication results:(with do's)", results)
    print("Sum of results:(with do's)", sum(results))

if __name__ == "__main__":
    find_muls()
    find_dos()