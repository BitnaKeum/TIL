#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE* fp = NULL;
	FILE* fp2 = NULL;
	char ch;

	fopen_s(&fp, "test.txt", "r");	// 파일 열기
	if (fp == NULL) {
		printf("test.txt 파일을 열 수 없습니다.\n");
		exit(1);
	}

	fopen_s(&fp2, "copy.txt", "w");	// 파일 열기
	if (fp2 == NULL) {
		printf("copy.txt 파일을 열 수 없습니다.\n");
		exit(1);
	}

	printf("파일 복사중...\n\n");
	while ((ch = fgetc(fp)) != EOF) {	// 파일로부터 한글자씩 읽어옴
		fputc(ch, fp2);
	}
	printf("복사 완료!!!\n");
	fclose(fp);
	fclose(fp2);

}