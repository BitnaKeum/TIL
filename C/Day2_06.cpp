//#include <stdio.h>
//
//int* MAX(int* pArr, int num);
//int* MIN(int* pArr, int num);
//
//
//int main()
//{
//	int arr[10] = { 0 };
//	
//	for (int i = 0; i <= 9; i++) {
//		printf("arr[%d] : ", i);
//		scanf_s("%d", &arr[i]);
//	}
//
//	printf("\n");
//	for (int i = 0; i < 10; i++)
//		printf("%d  ", arr[i]);
//	printf("\n");
//
//	int *pMax = NULL, *pMin = NULL;
//	pMax = MAX(arr, sizeof(arr) / sizeof(int));	// �ִ밪�� �ּ�
//	pMin = MIN(arr, sizeof(arr) / sizeof(int));	// �ּҰ��� �ּ�
//
//	printf("�ִ밪 : %d, �ε��� : %d\n", *pMax, pMax - arr);
//	printf("�ּҰ� : %d, �ε��� : %d\n", *pMin, pMin - arr);
//}
//
//int* MAX(int* pArr, int num) {
//	int* pMax = pArr;
//	for (int i = 1; i < num; i++) {
//		if (*(pArr+i) > *pMax)
//			pMax = pArr+i;
//	}
//	return pMax;
//}
//
//int* MIN(int* pArr, int num) {
//	int* pMin = pArr;
//	for (int i = 1; i < num; i++) {
//		if (*(pArr+i) < * pMin)
//			pMin = pArr+i;
//	}
//	return pMin;
//}