#include <stdio.h>

int main()
{
	char arr[26] = { 0 };
	for (int i = 0; i < 26; i++)
		arr[i] = 65 + i;

	for (int i = 0; i < 26; i++) {
		for (int j = 0; j < 26; j++) {
			printf("%c ", arr[(i+j)%26]);
		}
		printf("\n");
	}

}