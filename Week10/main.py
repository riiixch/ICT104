# Selection sort in Python
def selectionSort(array, size):

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

data = [22, 80, 42, 44, 99, 11, 2, 18, 35, 60]
size = len(data)
selectionSort(data, size)
print("Sorted Array in Ascending Order (Selection):")
print(data)
print("65064435 สมภพ เอี่ยมสมบัติ")



# Bubble sort in Python
def bubbleSort(array):

    # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:

                # swapping elements if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

data = [22, 80, 42, 44, 99, 11, 2, 18, 35, 60]

bubbleSort(data)

print("Sorted Array in Ascending Order (Bubble):")
print(data)
print("65064435 สมภพ เอี่ยมสมบัติ")