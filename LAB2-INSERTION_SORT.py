
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertionSort(arr)
    printArray(arr)



# #include <stdio.h>

#  int main() {
#      int a[]={3,4,1,5,6,2};
#  int n = sizeof(a)/sizeof(a[0]);
#  printf("Unsorted array is:");

#      for(int i=0; i<n; i++){
#  printf("%d",a[i]);

#  }
#  printf("\n");

#     for (int i=1;i<n;i++){
#         int key=a[i];
#         int j=i-1;
#      while(j>=0 && a[j]>key){
#          a[j+1]=a[j];
#          j=j-1;
#      }
#      a[j+1]=key;
#     }
#     printf("Sorted array:");
#      for(int i=0; i<n; i++){
#  printf("%d",a[i]);

#  }
#  printf("\n");
#  return 0;
#  }




