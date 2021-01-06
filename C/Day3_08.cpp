#include <stdio.h>

char* my_strstr(const char* str, const char* subStr);

int main()
{
	char str[100] = { 0 };
	char substr[100] = { 0 };
	char* result = NULL;

	printf("문자열 입력(str) : ");
	gets_s(str, sizeof(str));
	printf("검색할 문자열 입력(substr) : ");
	gets_s(substr, sizeof(substr));

	result = my_strstr(str, substr);
	if (result)
		printf("문자열 '%s'에서 탐색된 문자열 '%s'의 시작 위치: %d\n", str, substr, result - str + 1);
	else
		printf("문자열 '%s'에서 '%s'가 존재하지 않습니다.\n", str, substr);

}

char* my_strstr(const char* str, const char* subStr)
{
	const char* pStr = str;
	const char* pSub = subStr;
	int sub_len = 0;
	int i;

	while (*(pSub++) != NULL) 
		sub_len++;
	pSub = subStr;

	while (*pStr != NULL) {
		if (*pStr == *subStr) {
			for (i = 1; i < sub_len; i++) {
				if (*(pStr + i) != *(subStr + i))
					break;
			}
			if (i == sub_len)	// 문자열 찾은 경우
				return (char*)pStr;
		}

		pStr++;
	}
	return NULL;
}