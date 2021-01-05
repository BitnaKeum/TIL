#include <stdio.h>
#define arr_size 10

int* binarySearch(int A[], int* first, int* last, int key);

int main()
{
	int arr[arr_size] = { 0 };
	int search = 0;
	int* pKey = NULL;

	printf("원시 데이터 : ");
	for (int i = 0; i < arr_size; i++) {
		scanf_s("%d", &arr[i]);
	}

	printf("검색 데이터 입력 : ");
	scanf_s("%d", &search);

	pKey = binarySearch(arr, arr, arr+arr_size-1, search);

	if (pKey != NULL)
		printf("값: %d, 위치 : %d\n", *pKey, pKey-arr);
	else
		printf("없다고!ㅁ!\n");
}

int* binarySearch(int A[], int* first, int* last, int key)
{
	while (first <= last)
	{
		int mid = (last - first) / 2; // first와 last의 중간 인덱스
		mid += (first - A);

		if (key == A[mid])
			return A + mid;
		else if (key < A[mid])
			last = A + mid - 1;
		else
			first = A + mid + 1;
	}
	return NULL;
}