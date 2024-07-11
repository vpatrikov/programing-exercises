def zad_1():
    list_1 = input().split(", ")
    list_2 = input().split(", ")

    list_3 = []

    for item in list_1:
        for item_1 in list_2:
            if item in item_1 and item not in list_3:
                list_3.append(item)

    print(list_3)


def zad_2():
    version = input()
    version_list = [int(number) for number in version.split(".")]

    for i in range(len(version_list) - 1, -1, -1):
        if version_list[i] < 9:
            version_list[i] += 1
            break
        else:
            version_list[i] = 0

    version_list = [str(number) for number in version_list]
    print(".".join(version_list))


def zad_3():
    list_1 = input().split(" ")

    list_2 = [word for word in list_1 if len(word) % 2 == 0]

    for item in list_2:
        print(item)


def zad_4():
    list_1 = [int(number) for number in input().split(", ")]

    print(f"Positive: {", ".join([str(number) for number in list_1 if number >= 0])}")
    print(f"Negative: {", ".join([str(number) for number in list_1 if number < 0])}")
    print(f"Even: {", ".join([str(number) for number in list_1 if number % 2 == 0])}")
    print(f"Odd: {", ".join([str(number) for number in list_1 if number % 2 != 0])}")


def zad_5():
    while True:
        try:
            n = int(input())
            break
        except ValueError:
            print("ERROR: Input should be int.")

    dict_1 = {}
    for i in range(n):
        chairs, people = input().split()
        dict_1[chairs] = int(people)

    free_chairs = 0
    need_more = False

    for index, (chairs, people) in enumerate(dict_1.items(), start=1):
        num_chairs = len(chairs)
        if num_chairs >= people:
            free_chairs += num_chairs - people
        else:
            print(f"{people - num_chairs} more chairs needed in room {index}")
            need_more = True

    if not need_more:
        print(f"Game On, {free_chairs} free chairs left")


def zad_6():
    num_elect = int(input())
    shells = []
    remaining_elect = num_elect
    n = 1

    while remaining_elect > 0:
        max_elect = 2 * n * n
        elect_in_shell = min(remaining_elect, max_elect)
        shells.append(elect_in_shell)
        remaining_elect -= elect_in_shell
        n += 1

    print(shells)


def zad_7():
    list_1 = [int(number) for number in input().split(", ")]

    def print_group(group_num, list_per):
        print(
            f"Group of {group_num}'s: {[num for num in list_per if num > group_num - 10 and num <= group_num]}"
        )

    tens = int(round(max(list_1) / 10))

    for i in range(1, tens + 1):
        print_group(i * 10, list_1)


def zad_8():
    text = input()

    num = []
    current_num = ""

    for char in text:
        if char.isdigit():
            current_num += char
        elif current_num:
            num.append(int(current_num))
            current_num = ""

    for i in range(len(num)):
        text = text.replace(f"{num[i]}", f"{chr(num[i])}")

    num = [chr(x) for x in num]
    text_list = text.split()

    for i in range(len(text_list)):
        temp = num[i] + text_list[i][-1] + text_list[i][2:-1] + text_list[i][1]
        text_list[i] = temp

    print(" ".join(text_list))


def zad_9():
    class InvalidCommandException(Exception):
        "Raised when entered command is invalid"
        pass

    class IndexOutOfRangeCmd(Exception):
        "Raised when start or end index of the command are out of range"
        pass
    
    inp_list = input().split(" ")

    while True:
        command = input().split(" ")

        if command[0] == "3:1":
            print(" ".join(inp_list))
            break

        try:
            if len(command) != 3:
                raise InvalidCommandException()
            
            if command[0] not in ["merge", "divide"]:
                raise InvalidCommandException()
            
            start_idx = int(command[1])
            end_idx = int(command[2])
            
            if command[0] == "merge":
                start_idx = max(0, start_idx)
                end_idx = min(len(inp_list) - 1, end_idx)
                
                if start_idx <= end_idx:
                    merged = "".join(inp_list[start_idx:end_idx+1])
                    inp_list = inp_list[:start_idx] + [merged] + inp_list[end_idx+1:]
            
            elif command[0] == "divide":
                if start_idx >= len(inp_list) or start_idx < 0:
                    raise IndexOutOfRangeCmd()
                
                element = inp_list[start_idx]
                partitions = end_idx
                
                if partitions <= 0:
                    raise InvalidCommandException()
                
                part_len = len(element) // partitions
                remainder = len(element) % partitions
                divided = []
                
                index = 0
                for i in range(partitions):
                    if remainder > 0:
                        divided.append(element[index:index + part_len + 1])
                        index += part_len + 1
                        remainder -= 1
                    else:
                        divided.append(element[index:index + part_len])
                        index += part_len
                
                inp_list = inp_list[:start_idx] + divided + inp_list[start_idx+1:]

        except InvalidCommandException:
            print(f"ERR: Invalid command: {' '.join(command)}")
        except IndexOutOfRangeCmd:
            print(f"ERR: Start or end index out of range.")

zad_9()
