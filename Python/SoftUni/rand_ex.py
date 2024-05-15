def zad_2():
    try:
        age = int(input())
    except ValueError:
        print("Input should be int.")

    if age <= 14:
        print("drink toddy")
    elif 14 < age <= 18:
        print("drink coke")
    elif 18 < age <= 21:
        print("drink beer")
    else:
        print("drink whisky")



def zad_3():
    for _ in range(int(input())):
        try:
            number = int(input())
        except ValueError:
            print("Input should be int.")
            continue

    if number == 88:
        print("Hello")
    elif number == 86:
        print("How are you?")
    elif number < 88:
        print("GREAT!")
    else:
        print("Bye.")

def remove_vowels():
    word_list= list(input())

    new_list =  [x for x in word_list if x.lower() not in {'a', 'o', 'u', 'e', 'i'}]

    return_str = ''.join(new_list)

    if ''.join(word_list).istitle():
        return_str = return_str.capitalize()
    print(return_str)

def zad_train():
    try:
        n = int(input())
    except ValueError:
        print("Value should be int")

    train = [0] * n

    while True:
        choice = input()
        if choice == "End":
            break
        
        choice_lst = choice.split()
        
        if choice_lst[0] == "add":
            train[-1] += int(choice_lst[1])
        elif choice_lst[0] == "insert":
            index = int(choice_lst[1])
            people = int(choice_lst[2])
            train[index] += people
        elif choice_lst[0] == "leave":
            index = int(choice_lst[1])
            people = int(choice_lst[2])
            train[index] -= people
        else:
            print("Invalid Input")

    print(train)

def to_do():
    notes = [0] * 10

    while True:
        command = input()
        if command == "End":
            break
        tokens = command.split("-")
        try:
            priority = int(tokens[0]) - 1
            note = tokens[1]
            notes.pop(priority)
            notes.insert(priority, note)
        except IndexError:
            print("Out of index. Note was not added")

    new_notes = [x for x in notes if x != 0]

    print(new_notes)

string = input().split(" ")
searched_palindrome = input()
palindrome_lst = []
for i in range(len(string)):
    reversed_str = "".join(reversed(str(string[i])))
    
    if string[i] == reversed_str:
        palindrome_lst.append(string[i])

print(palindrome_lst)

count = 0

for word in string:
    if word == searched_palindrome:
        count += 1
print(f"Found palindrome {count} times.")