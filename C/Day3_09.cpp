#include <stdio.h>

int my_atoi(const char* pStr);

int main()
{
	char str[100] = { 0 };
	int result = 0;

	printf("정수로 변환할 문자열 입력 : ");
	gets_s(str, sizeof(str));

	printf("변환된 숫자(int) : %d\n", my_atoi(str));
}

int my_atoi(const char* pStr)
{
	int result = 0;
	const char* p1 = pStr;
	char sign = *p1;	// 첫번째 글자
	if (sign == '+' || sign == '-')
		p1++;
		
	while ('0' <= *p1 && *p1 <= '9') {
		result *= 10;
		result += *p1 - 48;

		p1++;
	}

	if (sign == '-')
		result *= -1;

	return result;
}