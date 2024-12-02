def distance():
    list1 = []
    list2 = []

    with open('input.txt', 'r') as file:
        for line in file:
            elements = line.split()
            list1.append(int(elements[0]))
            list2.append(int(elements[1]))

    list1.sort()
    list2.sort()

    total_difference = sum(abs(a - b) for a, b in zip(list1, list2))

    print("Total Absolute Difference:", total_difference)

def frequency():
    list1 = []
    list2 = []

    with open('input.txt', 'r') as file:
        for line in file:
            elements = line.split()
            list1.append(int(elements[0]))
            list2.append(int(elements[1]))

    frequency_dict = {}
    for num in list1:
        if num in frequency_dict:
            frequency_dict[num][0] += 1
        else:
            frequency_dict[num] = [1, 0]
    for num in list2:
        if num in frequency_dict:
            frequency_dict[num][1] += 1

    product_sum = sum(key * value[0] * value[1] for key, value in frequency_dict.items())

    print("Sum of Products:", product_sum)


def main():

    distance()
    frequency()


if __name__ == "__main__":
    main()