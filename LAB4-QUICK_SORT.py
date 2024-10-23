# Partition function
def partition(arr, low, high):
    
    pivot = arr[high]
    i = low - 1
    

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1

# Swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# The QuickSort function implementation
def quickSort(arr, low, high):
    if low < high:
        
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)
        
        # Recursion calls for smaller elements
        # and greater or equals elements
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Main driver code
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    quickSort(arr, 0, n - 1)
    
    for val in arr:
        print(val, end=" ") 




# #include <stdio.h>
# int swap(int *x, int *y)
# {
#     int temp=*x;
#     *x=*y;
#     *y=temp;
# }

# int partition(int a[], int lb, int ub)
# {
#     int pivot = a[lb];
#     int i= lb;
# 	int j= ub;

#     while(i<j)
# 	{
#     while (a[i] <= pivot && i <= ub - 1) {
#         i++;
#     }
       
#         while (a[j]> pivot && j >= lb+1)
#         {
#     j--;
#         }

#     if(i<j)
# {
# swap(&a[i],&a[j]);
# }
#     }

# swap(&a[lb],&a[j]);
# return j;
# }

# int quicksort(int a[], int lb, int ub)
# {
# if(lb<ub)
# {
# int par_index = partition(a, lb, ub);

# quicksort(a, lb, par_index-1);
# quicksort(a, par_index+1, ub);
# }
# }

# int main()
# {
# 	int n=10,i,j,a[10];

# printf("Enter a Number Those Sort:-");
# for(i=0;i<n;i++)
# {
# scanf("%d",&a[i]);
# }
# for(i=0;i<n;i++)
# {
# printf("%d\t",a[i]);
# }

# quicksort(a, 0, n-1);

# printf("\nSorted Array\n ");
# for(i=0;i<n;i++)
# {
# printf("%d\t",a[i]);
# }

# return 0;
# }
