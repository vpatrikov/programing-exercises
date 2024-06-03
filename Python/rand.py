from random import randint
def list_sort(list, choice):
    if choice == "asc":
        return sorted(list)
    elif choice == "dsc":
        return sorted(list, reverse=True);
    else:
        print("Invalid Choice\n")
        return False
    
rand_list = [randint(0,10) for x in range (10)]
def list_sort(list, choice):
    if choice == "asc":
        return sorted(list)
    elif choice == "dsc":
        return sorted(list, reverse=True);
    else:
        print("Invalid Choice\n")
        return False
    
rand_list = [randint for x in range(10)]

print(rand_list)
print(list_sort(rand_list, "asc"))

print(rand_list)
print(list_sort(rand_list, "asc"))