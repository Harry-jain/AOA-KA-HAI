# Python program for implementation of Selection
# Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
      
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                 min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    
    print("Original array: ", end="")
    print_array(arr)
    
    selection_sort(arr)
    
    print("Sorted array: ", end="")
    print_array(arr)



# #include <stdio.h>

#  int main() {
#      int a[]={3,4,1,5,6,2};
#  int n = sizeof(a)/sizeof(a[0]);
#  printf("Unsorted array is:");

#      for(int i=0; i<n; i++){
#  printf("%d",a[i]);

#  }
#  printf("\n");

#      for (int i=0; i<n-1; i++){
#  int min=i;
#  for (int j=i+1;j<n;j++){
#  if (a[j]<a[min]){
#  min=j;
#  }
#  }
#  int temp = a[min];
#  a[min]= a[i];
#  a[i]=temp;
#  }
#  printf("Sorted array is:");
#  for (int i=0;i<n;i++){
#  printf("%d",a[i]);

#  }
#  printf("\n");

#  return 0;
#  }







