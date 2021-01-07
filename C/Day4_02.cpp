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
	printf("학생 정보를 입력하시오..\n");
	printf(" 학     번 : ");
	gets_s(s1.id, sizeof(s1.id));
	printf(" 이     름 : ");
	gets_s(s1.name, sizeof(s1.name));
	printf(" 성별(M/F) : ");
	scanf_s("%c", &s1.gender);
	getchar();
	printf(" 연 락 처  : ");
	gets_s(s1.contact, sizeof(s1.contact));
	printf(" 전     공 : ");
	gets_s(s1.major, sizeof(s1.major));
	printf(" 생년월일(예: 2000/12/31) : ");
	scanf_s("%d%*c%d%*c%d", &s1.year, &s1.month, &s1.day);

	printf("\n");

	printf("학생 성적을 입력하시오..\n");
	printf(" 국     어 : ");
	scanf_s("%d", &s1.grade.kor);
	printf(" 영     어 : ");
	scanf_s("%d", &s1.grade.eng);
	printf(" 수     학 : ");
	scanf_s("%d", &s1.grade.mat);
	printf("\n");

	printf("\t ##### 학생 정보 #####\n");
	printf("학번 : %s\n", s1.id);
	printf("이름 : %s\n", s1.name);
	printf("성별 : %c\n", s1.gender);
	printf("연락처 : %s\n", s1.contact);
	printf("전공 : %s\n", s1.major);
	printf("생년월일 : %d-%d-%d\n", s1.year, s1.month, s1.day);

	
	printf("학생 성적 :   %d,    %d,    %d\n", s1.grade.kor, s1.grade.eng, s1.grade.mat);

}