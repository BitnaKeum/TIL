//#include <stdio.h>
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
//	int* pSm = arr;
//	int* pWalk = arr + 1;
//	int* pLast = arr + 9;
//
//	while (pWalk <= pLast) {
//		if (*pWalk < *pSm)
//			pSm = pWalk;
//		pWalk++;
//	}
//
//	printf("ÃÖ¼Ò°ª : %d\n", *pSm);
//}