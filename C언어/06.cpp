#include <stdio.h>

int main()
{
	int num1 = 0, num2 = 0;
	char ch = 0;

	printf("���� �Է� (��: 10 + 20) : ");
	scanf_s("%d %c", &num1, &ch);
	getchar();	// ����Ű ����
	scanf_s("%d", &num2);
	printf("%d %c %d = %d\n", num1, ch, num2, num1 + num2);
}