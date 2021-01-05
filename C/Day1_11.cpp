#include<stdio.h>

double roundTwo(double num);

int main(void)
{
	double num;

	printf("양의 부동소수점을 입력하시오 : ");
	scanf_s("%lf", &num);

	double result;
	result = roundTwo(num);

	printf("반올림 결과 : %lf\n", result);

	return 0;

}
double roundTwo(double num)
{
	num = (int)(num * 100.0 + 0.5) / 100.0;
	return num;
}
