#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{
	FILE* f1 = NULL;
	char file_name[100] = { 0 };
	char str[1024] = { 0 };
	int line = 1;


	if (argc != 2) {
		printf("���� : Project2 ���ϸ�\n");
		return 1;
	}

	strcpy_s(file_name, argv[1]);
	fopen_s(&f1, file_name, "r");	// ���� ����
	if (f1 == NULL) {
		printf("%s ������ �� �� �����ϴ�.\n", file_name);
		return 1;
	}

	
	while (fgets(str, sizeof(str), f1)) {
		printf("%03d ", line);
		fputs(str, stdout);
		line++;
	}

}