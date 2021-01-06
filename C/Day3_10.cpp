#include <stdio.h>

double my_atof(const char* pStr);

int main()
{
	char str[100] = { 0 };
	int result = 0;

	printf("�Ǽ��� ��ȯ�� ���ڿ� �Է� : ");
	gets_s(str, sizeof(str));

	printf("��ȯ�� ����(double) : %.6f\n", my_atof(str));
}

double my_atof(const char* pStr)
{
	double result = 0;
	int cnt = 0, dot = 0;
	const char* p1 = pStr;
	char sign = *p1;	// ù��° ����

	while (*p1 != NULL) {
		if (*p1 == '.') {
			dot = cnt;
		}
		else if ('0' <= *p1 && *p1 <= '9')
			cnt++;	// pStr�� ����
		else
			break;

		p1++;
	}

	if (sign == '+' || sign == '-') {
		cnt--;
		p1 = pStr + 1;	// �ι�° ���� ����Ŵ
	}
	else {
		p1 = pStr;
	}
		 
		
	while (('0' <= *p1 && *p1 <= '9') || *p1 == '.') {
		if (*p1 == '.') {
			p1++;
			continue;
		}
		
			
		result *= 10;
		result += (double)*p1 - 48.0;

		p1++;
	}

	for (int i = 0; i < cnt - dot; i++) {
		result /= 10.0;
	}

	if (sign == '-')
		result *= -1.0;

	return result;
}