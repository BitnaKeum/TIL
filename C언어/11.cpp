#include<stdio.h>

double roundTwo(double num);

int main(void)
{
	double num;

	printf("���� �ε��Ҽ����� �Է��Ͻÿ� : ");
	scanf_s("%lf", &num);

	double result;
	result = roundTwo(num);

	printf("�ݿø� ��� : %lf\n", result);

	return 0;

}
double roundTwo(double num)
{
	num = (int)(num * 100.0 + 0.5) / 100.0;
	return num;
}
