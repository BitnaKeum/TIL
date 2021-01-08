#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{
	char origin[100] = { 0 }, target[100] = { 0 };
	FILE* fOrigin = NULL, * fTarget = NULL;
	char ch;


	if (argc != 3) {
		printf("���� : Project2 �������ϸ� ������ϸ�\n");
		return 1;
	}

	strcpy_s(origin, argv[1]);
	strcpy_s(target, argv[2]);


	fopen_s(&fOrigin, origin, "r");
	fopen_s(&fTarget, target, "w");
	if (fOrigin == NULL || fTarget == NULL) {
		printf("������ �� �� �����ϴ�.\n");
		return 1;
	}

	printf("���� ������...\n\n");
	while ((ch = fgetc(fOrigin)) != EOF) {
		fputc(ch, fTarget);
	}
	printf("���� �Ϸ�!!!\n\n");


	fclose(fOrigin);
	fclose(fTarget);
}