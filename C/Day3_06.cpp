#include <stdio.h>
#include <string.h>

int my_strcmp(const char* left, const char* right);

int main()
{
	char left[100] = { 0 };
	char right[100] = { 0 };

	printf("���ڿ�1 �Է�(left) : ");
	gets_s(left, 100);
	printf("���ڿ�2 �Է�(right) : ");
	gets_s(right, 100);
	
	printf("���ڿ� �� : %d\n", my_strcmp(left, right));

}

int my_strcmp(const char* left, const char* right)
{
	const char* pLeft = left;
	const char* pRight = right;

	while (1) {	// ����� �Ǵµ� �ѱ��� �ȵǴµ�?

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