def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")


# #include <stdio.h>

# void bubbleSortTwoForLoops(int arr[], int n) {
#     int i, j, temp;
#     for (i = 0; i < n-1; i++) {
#         for (j = 0; j < n-i-1; j++) {
#             if (arr[j] > arr[j+1]) {
#                 temp = arr[j];
#                 arr[j] = arr[j+1];
#                 arr[j+1] = temp;
                
               
#                 printf("Array after swap: ");
#                 for (int k = 0; k < n; k++) {
#                     printf("%d ", arr[k]);
#                 }
#                 printf("\n");
#             }
#         }
#     }
# }

# int main() {
#     int n;
    

#     printf("Enter the number of elements in the array: ");
#     scanf("%d", &n);
    
#     int arr[n];
    

#     printf("Enter the elements of the array:\n");
#     for (int i = 0; i < n; i++) {
#         scanf("%d", &arr[i]);
#     }
    
#     printf("Unsorted array: \n");
#     for (int i = 0; i < n; i++) {
#         printf("%d ", arr[i]);
#     }
#     printf("\n");


#     bubbleSortTwoForLoops(arr, n);

#     printf("Sorted array: \n");
#     for (int i = 0; i < n; i++) {
#         printf("%d ", arr[i]);
#     }
#     printf("\n");

#     return 0;
# }
