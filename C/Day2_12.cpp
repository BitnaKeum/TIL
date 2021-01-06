#include <stdio.h>

int binarySearch(int A[], int first, int last, int key);

int main()
{
	int arr[10] = { 0 };
	int search = 0;
	int key_idx = 0;

	printf("원시 데이터 : ");
	for (int i = 0; i < 10; i++) {
		scanf_s("%d", &arr[i]);
	}

	printf("검색 데이터 입력 : ");
	scanf_s("%d", &search);

	key_idx = binarySearch(arr, 0, sizeof(arr)/sizeof(int), search);

	if (key_idx != -1)
		printf("위치 : %d\n", key_idx);
	else
		printf("없다고!ㅁ!\n");
}

int binarySearch(int A[], int first, int last, int key)
{
	if (first > last)
		return -1;

	int mid = (first + last) / 2;

	if (key == A[mid]) 
		return mid;
	else if (key < A[mid])	
		binarySearch(A, first, mid-1, key);
	else 
		binarySearch(A, mid+1, last, key);
}
