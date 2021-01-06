#include <stdio.h>

int my_atoi(const char* pStr);

int main()
{
	char str[100] = { 0 };
	int result = 0;

	printf("������ ��ȯ�� ���ڿ� �Է� : ");
	gets_s(str, sizeof(str));

	printf("��ȯ�� ����(int) : %d\n", my_atoi(str));
}

int my_atoi(const char* pStr)
{
	int result = 0;
	const char* p1 = pStr;
	char sign = *p1;	// ù��° ����
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