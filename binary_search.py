# #include <stdio.h>
# int binarySearch(int a[], int item, int low, int high)
# {
# 	if (high <= low)
# 		return (item > a[low]) ? (low + 1) : low;

# 	int mid = (low + high) / 2;
	
# 	if (item == a[mid])
# 		return mid + 1;

# 	if (item > a[mid])
# 		return binarySearch(a, item, mid + 1, high);
# 	return binarySearch(a, item, low, mid - 1);
# }
# void insertionSort(int a[], int n)
# {
# 	int i, loc, j, k, selected;

# 	for (i = 1; i < n; ++i) {
# 		j = i - 1;
# 		selected = a[i];
# 		loc = binarySearch(a, selected, 0, j);
# 		while (j >= loc) {
# 			a[j + 1] = a[j];
# 			j--;
# 		}
# 		a[j + 1] = selected;
# 	}
# }
# int main()
# {
# 	int a[]= { 37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54 };
# 	int n = sizeof(a) / sizeof(a[0]), i;

# 	insertionSort(a, n);

# 	printf("Sorted array: \n");
# 	for (i = 0; i < n; i++)
# 		printf("%d ", a[i]);

# 	return 0;
# }




def binarySearch(arr, low, high, x):

    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
