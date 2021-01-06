#include <stdio.h>

char* my_strcpy(char* dest, const char* src);

int main()
{
	char fromStr[100] = { 0 };
	char toStr[100] = { 0 };
	

	printf("문자열입력1 : ");
	gets_s(fromStr, 100);
	printf("문자열입력2 : ");
	gets_s(toStr, 100);

	printf("문자열1 : %s\n", my_strcpy(fromStr, toStr));
	printf("문자열2 : %s\n", toStr);
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