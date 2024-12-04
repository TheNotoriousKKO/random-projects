def safe_reports():
    total_safe = 0

    with open('input.txt', 'r') as file:
        for line in file:
            report = line.split()
            report = list(map(int, report))
            previous = report[0]
            is_ascending = previous < report[-1]
            is_unsafe = False

            for element in report[1:]:
                if is_ascending:
                    if element - previous not in (1, 2, 3):
                        is_unsafe = True
                        break
                else:
                    if previous - element not in (1, 2, 3):
                        is_unsafe = True
                        break
                previous = element
            if previous == report[-1] and not is_unsafe:
                total_safe += 1

    print("Total reports safe: ", total_safe)

def safe_reports_dampened():
    total_safe = 0
    def checkreport(report, is_ascending):
        for i in range(1, len(report)):
            if is_ascending:
                if report[i] - report[i - 1] not in (1, 2, 3):
                    return i
            else:
                if report[i - 1] - report[i] not in (1, 2, 3):
                    return i
        return -1



    with open('input.txt', 'r') as file:
        for line in file:
            report = line.split()
            report = list(map(int, report))
            rising = 0
            falling = 0
            # Compare first element against last
            if report[0] < report[-1]:
                rising += 1
            else:
                falling += 1

            # Compare first element against penultimate
            if report[0] < report[-2]:
                rising += 1
            else:
                falling += 1

            # Compare second element against last
            if report[1] < report[-1]:
                rising += 1
            else:
                falling += 1

            # Compare second element against penultimate
            if report[1] < report[-2]:
                rising += 1
            else:
                falling += 1

            is_ascending = rising > falling
            first_try = checkreport(report, is_ascending)
            if first_try == -1:
                total_safe += 1
            else:
                report_a = report[:first_try] + report[first_try+1:]
                print(report_a)
                report_b = report[:first_try-1] + report[first_try:]
                print(report_b )
                if checkreport(report_a, is_ascending) == -1 or checkreport(report_b, is_ascending) == -1:
                    total_safe += 1


            

    print("Total reports safe (with dampening): ", total_safe)



def main():
    safe_reports()
    safe_reports_dampened()


if __name__ == "__main__":
    main()
