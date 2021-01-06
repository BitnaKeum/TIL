#include <stdio.h>

int* MAX(int* pArr, int num);
int* MIN(int* pArr, int num);


int main()
{
	int arr[10] = { 0 };
	
	for (int i = 0; i <= 9; i++) {
		printf("arr[%d] : ", i);
		scanf_s("%d", &arr[i]);
	}

	printf("\n");
	for (int i = 0; i < 10; i++)
		printf("%d  ", arr[i]);
	printf("\n");

	int *pMax = NULL, *pMin = NULL;
	pMax = MAX(arr, sizeof(arr) / sizeof(int));	// 최대값의 주소
	pMin = MIN(arr, sizeof(arr) / sizeof(int));	// 최소값의 주소

	printf("최대값 : %d, 인덱스 : %d\n", *pMax, pMax - arr);
	printf("최소값 : %d, 인덱스 : %d\n", *pMin, pMin - arr);
}

int* MAX(int* pArr, int num) {
	int* pMax = pArr;
	for (int i = 1; i < num; i++) {
		if (*(pArr+i) > *pMax)
			pMax = pArr+i;
	}
	return pMax;
}

int* MIN(int* pArr, int num) {
	int* pMin = pArr;
	for (int i = 1; i < num; i++) {
		if (*(pArr+i) < * pMin)
			pMin = pArr+i;
	}
	return pMin;
}
