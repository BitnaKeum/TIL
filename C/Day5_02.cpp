#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE* fp = NULL;
	FILE* fp2 = NULL;
	char ch;

	fopen_s(&fp, "test.txt", "r");	// ���� ����
	if (fp == NULL) {
		printf("test.txt ������ �� �� �����ϴ�.\n");
		exit(1);
	}

	fopen_s(&fp2, "copy.txt", "w");	// ���� ����
	if (fp2 == NULL) {
		printf("copy.txt ������ �� �� �����ϴ�.\n");
		exit(1);
	}

	printf("���� ������...\n\n");
	while ((ch = fgetc(fp)) != EOF) {	// ���Ϸκ��� �ѱ��ھ� �о��
		fputc(ch, fp2);
	}
	printf("���� �Ϸ�!!!\n");
	fclose(fp);
	fclose(fp2);

}