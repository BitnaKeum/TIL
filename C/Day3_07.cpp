#include <stdio.h>

char* my_strchr(const char* pStr, int ch);

int main()
{
	char str[100] = { 0 };
	char ch;
	char* result = NULL;
	
	printf("���ڿ� �Է�(str) : ");
	gets_s(str, 100);
	printf("�˻� ���� �Է�: ");
	ch = getchar();

	result = my_strchr(str, ch);
	if (result == NULL)
		printf("���ڿ� '%s'���� ã���� �ϴ� '%c'�� �������� �ʽ��ϴ�.\n", str, ch);
	else
		printf("���ڿ� '%s'���� �˻��� '%c'�� ��ġ: %d\n", str, ch, result - str + 1);
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