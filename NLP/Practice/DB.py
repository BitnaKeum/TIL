import pymysql

db = None
try:
    # DB 연결
    db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='password1!',
        db='study_db',
        charset='utf8'
    )
    print("DB 연결 성공")

    # SQL 구문

    # 테이블 생성
    sql = '''
        CREATE TABLE tb_student (
            id int primary key auto_increment not null,
            name varchar(32),
            age int,
            address varchar(32)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    '''

    # 데이터 추가
    # sql = '''
    #     INSERT tb_student(name, age, address) values('Kei', 35, 'Korea')
    # '''

    # 데이터 변경
    # id = 1
    # sql = '''
    #     UPDATE tb_student set name="케이", age=36 where id=%d
    # ''' % id

    # # 데이터 삭제
    # id = 1
    # sql = '''
    #     DELETE from tb_student where id=%d
    # ''' % id


    with db.cursor() as cursor: # 사용 후 자동으로 메모리 해제
        cursor.execute(sql) # SQL 구문 실행
    db.commit()

except Exception as e:
    print(e)    # DB 연결 실패

finally:
    if db is not None:
        db.close()
        print("DB 닫았음")
