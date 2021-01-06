#include <stdio.h>

char* my_strchr(const char* pStr, int ch);

int main()
{
	char str[100] = { 0 };
	char ch;
	char* result = NULL;
	
	printf("문자열 입력(str) : ");
	gets_s(str, 100);
	printf("검색 문자 입력: ");
	ch = getchar();

	result = my_strchr(str, ch);
	if (result == NULL)
		printf("문자열 '%s'에서 찾고자 하는 '%c'가 존재하지 않습니다.\n", str, ch);
	else
		printf("문자열 '%s'에서 검색된 '%c'의 위치: %d\n", str, ch, result - str + 1);
}

char* my_strchr(const char* pStr, int ch)
{
	const char* p1 = pStr;
	while(*p1 != NULL) {
		if (*p1 == ch)
			return (char*)p1;
		p1++;
	}
	return NULL;
}