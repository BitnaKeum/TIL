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
		printf("사용법 : Project2 파일명\n");
		return 1;
	}

	strcpy_s(file_name, argv[1]);
	fopen_s(&f1, file_name, "r");	// 파일 열기
	if (f1 == NULL) {
		printf("%s 파일을 열 수 없습니다.\n", file_name);
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


	printf("라인 수 : %d\n", line_num);
	printf("단어 수 : %d\n", word_num);
	printf("문자 수 : %d\n", ch_num);
}