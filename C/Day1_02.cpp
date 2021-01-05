#include <stdio.h>

int main()
{
	char a = 'A';
	void* p1 = &a;

	*(char*)p1 = *(char*)p1 + 1;

	printf("a : %c\n", a);
}
