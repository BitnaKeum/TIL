#include <stdio.h>

char* my_strstr(const char* str, const char* subStr);

int main()
{
	char str[100] = { 0 };
	char substr[100] = { 0 };
	char* result = NULL;

	printf("���ڿ� �Է�(str) : ");
	gets_s(str, sizeof(str));
	printf("�˻��� ���ڿ� �Է�(substr) : ");
	gets_s(substr, sizeof(substr));

	result = my_strstr(str, substr);
	if (result)
		printf("���ڿ� '%s'���� Ž���� ���ڿ� '%s'�� ���� ��ġ: %d\n", str, substr, result - str + 1);
	else
		printf("���ڿ� '%s'���� '%s'�� �������� �ʽ��ϴ�.\n", str, substr);

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
			if (i == sub_len)	// ���ڿ� ã�� ���
				return (char*)pStr;
		}

		pStr++;
	}
	return NULL;
}