#include <stdio.h>

int main()
{
	char a = 'A';
	char* p1 = &a;

	*p1 = *p1 + 1;

	printf("a: %c\n", a);
}
