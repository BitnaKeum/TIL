//#include <stdio.h>
//
//void selectionSort(int arr[], int n);
//
//int main()
//{
//	int arr[10] = { 0 };
//	for (int i = 0; i < 10; i++) 
//		scanf_s("%d", &arr[i]);
//
//	selectionSort(arr, 10);
//
//	for (int i = 0; i < 10; i++)
//		printf("%d ", arr[i]);
//	printf("\n");
//}
//
//void selectionSort(int arr[], int n)
//{
//	int smallest = 0;
//	int temp = 0;
//
//	for (int i = 0; i < n-1; i++) {
//		smallest = i;
//
//		for (int j = i + 1; j < n; j++) {
//			if (arr[j] < arr[smallest]) 
//				smallest = j;
//		}
//		temp = arr[i];
//		arr[i] = arr[smallest];
//		arr[smallest] = temp;
//	}
//}