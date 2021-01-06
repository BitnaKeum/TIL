#include <stdio.h>

size_t my_strlen(const char* pStr);

int main()
{
	char str[100] = { 0 };
	printf("문자열 입력: ");
	gets_s(str, 100);
	printf("문자열의 문자 개수 : %d\n", my_strlen(str));

}

size_t my_strlen(const char* pStr) {
	const char* p1 = pStr;
	int len = 0;
	while (*p1 != NULL) {
		len++;
		p1++;
	}

	return len;
}