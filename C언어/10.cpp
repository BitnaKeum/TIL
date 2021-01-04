#include <stdio.h>

int validateBinary(int num);
int binaryToDecimal(int num);

int main()
{
	int binary = 0;

	while (1)
	{
		printf("이진수 입력 (0 또는 1) : ");
		scanf_s("%d", &binary);

		if (validateBinary(binary) == -1)
		{
			printf("이진수가 아닙니다.\n");
			continue;
		}
		break;
	}

	printf("입력한 이진수 : %d\n", binary);
	printf("변환된 십진수 : %d\n", binaryToDecimal(binary));

}

int validateBinary(int num) 
{
	while (num != 0)
	{
		if (num % 10 != 0 && num % 10 != 1)
			return -1;
		num /= 10;
	}
	return 0;
}

int binaryToDecimal(int num)
{
	int remainder = 0;
	int cnt = 0;
	int decimal = 0;

	while (num != 0)
	{
		remainder = num % 10;
		
		for (int i = 0; i < cnt; i++)
			remainder *= 2;

		decimal += remainder;

		num /= 10;
		cnt++;
	}
	int n;
	double k;
	n = (int)(k + 1.1);

	
	return decimal;
}