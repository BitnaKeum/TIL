
### 파일 입출력
<br>

1. 파일 열기
```
FILE *fp = NULL;
fopen_s(&fp, "text.txt", "r");  // 읽기 모드로 열기
if(fp==NULL) {
   // 에러 메시지 출력
}

fclose(fp);
```
<br>

2. 파일로부터 한 글자 읽기
```
char ch;
ch = fgetc(fp);
```
<br>

3. 파일로부터 한 줄(한 문자열) 읽기
```
char str[100] = {0};
fgets(str, sizeof(str), fp);
```
<br>

4. 파일에 한 글자 쓰기
```
fputc(ch, fp);
```
<br>

5. 파일에 문자열 쓰기
```
fputs(str, fp);
```
<br><br>


### 응용 예제
<br>

1. 파일로부터 한 글자씩 읽어 콘솔에 출력하기
```
while((ch=fgetc(fp)) != EOF) {
  putchar(ch);
}
```
<br>

2. 파일로부터 한 글자씩 읽어 다른 파일에 출력하기
```
FILE* fp2 = NULL;
fopen_s(&fp2, "text2.txt", "r");

while((ch=fgetc(fp)) != EOF) {
 fputc(ch, fp2);
}
```
<br>

3. 파일로부터 한 줄씩 읽어 콘솔에 출력하기
```
while(fgets(str, sizeof(str), fp) {
  fputs(str, stdout);
}
```
<br>

4. 파일로부터 한 줄씩 읽어 다른 파일에 출력하기
```
while(fgets(str, sizeof(str), fp) {
  fputs(str, fp2);
}
```
<br>

5. 콘솔로부터 한 글자씩 입력해 파일에 출력하기
```
while((ch=getchar()) != EOF) {  // ctrl+Z 누르면 입력 종료
  fputc(ch, fp);
}
```
<br>

6. 콘솔로부터 한 줄(한 문자열)씩 입력해 파일에 출력하기
```
while(fgets(str, sizeof(str), stdin)) {
  fputs(str, fp);
}
```
<br><br>
