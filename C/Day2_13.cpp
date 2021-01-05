#include <stdio.h>
#define arr_size 10

int* binarySearch(int A[], int* first, int* last, int key);

int main()
{
	int arr[arr_size] = { 0 };
	int search = 0;
	int* pKey = NULL;

	printf("���� ������ : ");
	for (int i = 0; i < arr_size; i++) {
		scanf_s("%d", &arr[i]);
	}

	printf("�˻� ������ �Է� : ");
	scanf_s("%d", &search);

	pKey = binarySearch(arr, arr, arr+arr_size-1, search);

	if (pKey != NULL)
		printf("��: %d, ��ġ : %d\n", *pKey, pKey-arr);
	else
		printf("���ٰ�!��!\n");
}

int* binarySearch(int A[], int* first, int* last, int key)
{
	while (first <= last)
	{
		int mid = (last - first) / 2; // first�� last�� �߰� �ε���
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