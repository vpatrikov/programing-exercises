def zad_1():
    vowels = ["a", "o", "u", "e", "i"]
    string = input()
    new_string = "".join([letter for letter in string if letter.lower() not in vowels])
    print(new_string)


def zad_2():
    class InvalidCommand(Exception):
        "Raised when invalid command is entered."
        pass

    class InvalidCommandLength(Exception):
        "Raised when command has too many or less paramethers."
        pass

    while True:
        try:
            n = int(input())
            train = [0 for x in range(n)]
            break
        except ValueError:
            print("ERROR: Input should be int.\n")

    commands_list = ["add", "insert", "leave"]

    while True:
        command = input().split(" ")
        try:
            if command[0] == "End":
                break

            if (command[0] in ["insert", "leave"] and len(command) != 3) or (
                command[0] == "add" and len(command) != 2
            ):
                raise InvalidCommandLength

            if command[0] not in commands_list:
                raise InvalidCommand

            if command[0] == "add":
                train[-1] += int(command[1])
            elif command[0] == "insert":
                index = int(command[1])
                value = int(command[2])
                train[index] += value
            elif command[0] == "leave":
                index = int(command[1])
                value = int(command[2])
                train[index] -= value
                if train[index] < 0:
                    train[index] = 0

        except InvalidCommand:
            print(f"ERROR: {command[0]} is not a valid command.")
        except InvalidCommandLength:
            print("ERROR: Invalid command length")

    print(train)


zad_2()
