
#SEARCHING ALGORITHM

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):  #Loop through the array from start to end
        if arr[i] == target:   #Check if current element matches the target
            return i           #If found, return the index
    return -1                  #If not found, return -1 (not in array)

# Binary Search
def binary_search(array, key):
    low, high = 0, len(array) - 1   #Define the search boundaries (start and end index)
    while low <= high:              #Repeat until search space is exhausted
        mid = (low + high) // 2     #Find the middle index
        if array[mid] == key:       #If middle element matches the key
            return mid              #Return index (found)
        elif array[mid] < key:      #If key is greater, search right half
            low = mid + 1           #Move the lower bound up
        else:                       #If key is smaller, search left half
            high = mid - 1          #Move the upper bound down
    return -1                       #If not found, return -1

#SORTING ALGORITHM

# Selection Sort
def selection_sort(array):
    n = len(array)                          #Get the length of array
    for i in range(n):                      #Outer loop: position where the next minimum will be placed
        min_index = i                       #Assuming that the current index is the minimum
        for j in range(i+1, n):             #Inner loop: find the actual minimum in the unsorted part
            if array[j] < array[min_index]: #Compare each element with the current min
                min_index = j               #Update min_index if smaller element is found
                                            #Then swap the found minimum with the element at position i
        array[i], array[min_index] = array[min_index], array[i] #Selection sort swaps only once per outer loop

# Insertion Sort
def insertion_sort(array): 
    for i in range(1, len(array)):          #Start from 2nd element, treating the 1st as "sorted"
        key = array[i]                      #The element we want to insert into the sorted portion
        j = i - 1                           #Start comparing with the element just before key
        while j >= 0 and array[j] > key:    #Shift larger elements one step to the right
            array[j+1] = array[j]           #Move array[j] forward
            j -= 1                          #Move left to check the next element
        array[j+1] = key                    #Place key in its correct sorted position
         #Insertion sort shifts multiple times per element (not just one swap) like the lesson said

# MENU
def main():
    array = [10, 63, 1, 9, 7, 5, 23]

    while True:
        print("\n====== MENU ======")
        print("Original Array:", array)
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Selection Sort")
        print("4. Insertion Sort")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            try:
                key = int(input("Enter number to search: ").strip())
            except ValueError:
                print("Please enter a valid integer.")
                continue
            result = linear_search(array, key)
            if result != -1:
                print(f"{key} found at index {result} (Linear Search on original array)")
            else:
                print(f"{key} not found in array")

        elif choice == "2":
            try:
                key = int(input("Enter number to search: ").strip())
            except ValueError:
                print("Please enter a valid integer.")
                continue
            sorted_arr = sorted(array)
            result = binary_search(sorted_arr, key)
            print("Sorted Array (for Binary Search):", sorted_arr)
            if result != -1:
                original_index = array.index(key)
                print(f"{key} found at index {result} in the sorted array")
                print(f"The same value is at index {original_index} in the original array")
            else:
                print(f"{key} not found in array")

        elif choice == "3":
            arr_copy = array.copy()
            print("Original before Selection Sort:", arr_copy)
            selection_sort(arr_copy)
            print("Array after Selection Sort:", arr_copy)

        elif choice == "4":
            arr_copy = array.copy()
            print("Original before Insertion Sort:", arr_copy)
            insertion_sort(arr_copy)
            print("Array after Insertion Sort:", arr_copy)

        elif choice == "5":
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
