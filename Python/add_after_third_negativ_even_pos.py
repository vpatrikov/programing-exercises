def add_after_third_neg_even_pos(lst):
    negative_count = 0
    i = 0 # index for iterating over list

    while i < len(lst):
        if i % 2 == 0 and lst[i] < 0: # ako e na chetna poz i otricatelno chislo
            negative_count += 1 # counter for comleted

            if negative_count == 3:
                lst.insert(i+1, lst[i] / 2) #dobavqme na tretiq otricatelen element na chetna poziciq polovinata na tekushtiq element
                negative_count = 0 # reset counter
                i += 1 # skip newly added element

        i += 1 # go onto next element

    return lst

input_list = [1, -5, 2, -10, 3, -15, 4, -20, 5, -25, -30]
print("Initial list:")
print(input_list)

output_list = add_after_third_neg_even_pos(input_list)
print("Sorted list:")
print(output_list)