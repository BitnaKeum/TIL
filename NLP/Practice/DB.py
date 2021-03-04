import pymysql
import pandas as pd

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
    # sql = '''
    #     CREATE TABLE tb_student (
    #         id int primary key auto_increment not null,
    #         name varchar(32),
    #         age int,
    #         address varchar(32)
    #     ) ENGINE=InnoDB DEFAULT CHARSET=utf8
    # '''

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

    # # 데이터 추가
    # students = [
    #     {'name': 'Kei', 'age': 36, 'address': 'PUSAN'},
    #     {'name': 'Tony', 'age': 34, 'address': 'PUSAN'},
    #     {'name': 'Jaeyoo', 'age': 39, 'address': 'GWANGJU'},
    #     {'name': 'Grace', 'age': 28, 'address': 'SEOUL'},
    #     {'name': 'Jenny', 'age': 27, 'address': 'SEOUL'},
    # ]
    # for s in students:
    #     with db.cursor() as cursor:
    #         sql = '''
    #             INSERT tb_student(name, age, address) values("%s","%d","%s")
    #         ''' % (s['name'], s['age'], s['address'])
    #         cursor.execute(sql)
    # db.commit()

    # 30대 학생만 조회
    cond_age = 30
    with db.cursor() as cursor:
        sql = '''
            SELECT * FROM tb_student where age > %d
        ''' % cond_age
        cursor.execute(sql)
        results = cursor.fetchall()   # SQL문 수행 결과 여러 개 가져옴
    print(results)

    # 이름 검색
    cond_name = 'Grace'
    with db.cursor() as cursor:
        sql = '''
            SELECT * FROM tb_student where name="%s"
        ''' % cond_name
        cursor.execute(sql)
        result = cursor.fetchone()  # SQL문 수행 결과 하나 가져옴
    print(result)

    # pandas 데이터프레임으로 표현
    df = pd.DataFrame(results)
    print(df)
    

except Exception as e:
    print(e)    # DB 연결 실패

finally:
    if db is not None:
        db.close()
        print("DB 닫았음")
