#include <stdio.h>
#include <string.h>

int main(int argc, char* argv[])
{
	char origin[100] = { 0 }, target[100] = { 0 };
	FILE* fOrigin = NULL, * fTarget = NULL;
	char ch;


	if (argc != 3) {
		printf("사용법 : Project2 원본파일명 대상파일명\n");
		return 1;
	}

	strcpy_s(origin, argv[1]);
	strcpy_s(target, argv[2]);


	fopen_s(&fOrigin, origin, "r");
	fopen_s(&fTarget, target, "w");
	if (fOrigin == NULL || fTarget == NULL) {
		printf("파일을 열 수 없습니다.\n");
		return 1;
	}

	printf("파일 복사중...\n\n");
	while ((ch = fgetc(fOrigin)) != EOF) {
		fputc(ch, fTarget);
	}
	printf("복사 완료!!!\n\n");


	fclose(fOrigin);
	fclose(fTarget);
}