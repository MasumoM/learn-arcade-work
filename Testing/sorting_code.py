import random


def selection_sort(my_list):

    # Loop through the entire array
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos

        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(my_list)):

            # Is this position smallest?
            if my_list[scan_pos] < my_list[min_pos]:
                # It is, mark this position as the smallest
                min_pos = scan_pos

        # Swap the two values
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp


def insertion_sort(my_list):

    for key_pos in range(1, len(my_list)):

        key_value = my_list[key_pos]
        scan_pos = key_pos - 1

        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1

        my_list[scan_pos + 1] = key_value

def print_list(my_list):
    for item in my_list:
        print(f"{item:3}", end="")
    print()


def main():
    list_for_selection_sort = []
    list_for_insertion_sort = []
    list_size = 10
    for i in range(list_size):
        new_number = random.randrange(100)
        list_for_selection_sort.append(new_number)
        list_for_insertion_sort.append(new_number)

    print("Original List")
    print_list(list_for_selection_sort)

    print("Selection Sort")
    selection_sort(list_for_selection_sort)
    print_list(list_for_selection_sort)

    print("Insertion Sort")
    insertion_sort(list_for_insertion_sort)
    print_list(list_for_insertion_sort)


main()

