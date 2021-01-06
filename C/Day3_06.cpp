#include <stdio.h>
#include <string.h>

int my_strcmp(const char* left, const char* right);

int main()
{
	char left[100] = { 0 };
	char right[100] = { 0 };

	printf("문자열1 입력(left) : ");
	gets_s(left, 100);
	printf("문자열2 입력(right) : ");
	gets_s(right, 100);
	
	printf("문자열 비교 : %d\n", my_strcmp(left, right));

}

int my_strcmp(const char* left, const char* right)
{
	const char* pLeft = left;
	const char* pRight = right;

	while (1) {	// 영어는 되는데 한글이 안되는듯?

		if (*pLeft == *pRight) {
			if(*(pLeft+1)==NULL && *(pRight+1)==NULL)
				return 0;
		}
		else if (*pLeft > *pRight) return 1;
		else return -1;

		pLeft++;
		pRight++;
	}
}