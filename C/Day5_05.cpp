#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{
	FILE* f1 = NULL;
	char file_name[100] = { 0 };
	char ch;
	int line_num = 0;
	int word_num = 0;
	int ch_num = 0;


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

	
	while ((ch = (char)fgetc(f1)) != EOF) {
		if (ch == '\n')
			line_num++;

		if (ch == ' ' || ch == '\n')
			word_num++;

		if (ch != ' ' && ch != '\n')
			ch_num++;
	}
	line_num++;


	printf("���� �� : %d\n", line_num);
	printf("�ܾ� �� : %d\n", word_num);
	printf("���� �� : %d\n", ch_num);
}