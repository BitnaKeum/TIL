#include <stdio.h>

char* my_strcpy(char* dest, const char* src);

int main()
{
	char fromStr[100] = { 0 };
	char toStr[100] = { 0 };
	

	printf("���ڿ��Է�1 : ");
	gets_s(fromStr, 100);
	printf("���ڿ��Է�2 : ");
	gets_s(toStr, 100);

	printf("���ڿ�1 : %s\n", my_strcpy(fromStr, toStr));
	printf("���ڿ�2 : %s\n", toStr);
}

char* my_strcpy(char* dest, const char* src)
{
	char* pDest = dest;
	const char* pSrc = src;

	while(*pSrc != NULL)
	{
		*pDest = *pSrc;
		pDest++;
		pSrc++;
	}
	*pDest = '\0';
	return dest;
}