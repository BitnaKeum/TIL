#include <stdio.h>

typedef struct _grade {
	int kor;
	int eng;
	int mat;
}Grade;

typedef struct _student {
	char id[11];
	char name[10];
	char gender;
	char contact[14];
	char major[30];
	int year;
	int month;
	int day;
	Grade grade;
}Student;

int main()
{
	Student s1;
	printf("�л� ������ �Է��Ͻÿ�..\n");
	printf(" ��     �� : ");
	gets_s(s1.id, sizeof(s1.id));
	printf(" ��     �� : ");
	gets_s(s1.name, sizeof(s1.name));
	printf(" ����(M/F) : ");
	scanf_s("%c", &s1.gender);
	getchar();
	printf(" �� �� ó  : ");
	gets_s(s1.contact, sizeof(s1.contact));
	printf(" ��     �� : ");
	gets_s(s1.major, sizeof(s1.major));
	printf(" �������(��: 2000/12/31) : ");
	scanf_s("%d%*c%d%*c%d", &s1.year, &s1.month, &s1.day);

	printf("\n");

	printf("�л� ������ �Է��Ͻÿ�..\n");
	printf(" ��     �� : ");
	scanf_s("%d", &s1.grade.kor);
	printf(" ��     �� : ");
	scanf_s("%d", &s1.grade.eng);
	printf(" ��     �� : ");
	scanf_s("%d", &s1.grade.mat);
	printf("\n");

	printf("\t ##### �л� ���� #####\n");
	printf("�й� : %s\n", s1.id);
	printf("�̸� : %s\n", s1.name);
	printf("���� : %c\n", s1.gender);
	printf("����ó : %s\n", s1.contact);
	printf("���� : %s\n", s1.major);
	printf("������� : %d-%d-%d\n", s1.year, s1.month, s1.day);

	
	printf("�л� ���� :   %d,    %d,    %d\n", s1.grade.kor, s1.grade.eng, s1.grade.mat);

}