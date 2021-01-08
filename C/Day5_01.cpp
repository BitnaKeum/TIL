#include <stdio.h>
#define MAX(a,b) ((a)>(b)?(a):(b))
int main()
{
	int a = 3;
	int b = 5;
	printf("max: %d\n", MAX(a, b));
}