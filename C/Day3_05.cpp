#include <stdio.h>

char* my_strcat(char* dest, const char* src);

int main()
{
	char dest[100] = { 0 };
	char src[100] = { 0 };

	printf("대상 문자열(dest) : ");
	gets_s(dest, 100);
	printf("원본 문자열(src)  : ");
	gets_s(src, 100);

	printf("대상 문자열(dest) : %s\n", my_strcat(dest, src));

}

char* my_strcat(char* dest, const char* src)
{
	char* pDest = dest;
	const char* pSrc = src;

	while (*pDest != NULL)
		pDest++;
	while (*pSrc != NULL) {
		*pDest = *pSrc;
		pDest++;
		pSrc++;
	}
	*pDest = '\0';

	return dest;
}