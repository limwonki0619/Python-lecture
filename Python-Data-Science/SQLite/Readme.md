## 1. SQLite란?

- 경량 DBMS
	- 별도의 서버가 필요 없음.
	- 모바일 기기에서 많이 활용되고 있음
	- 파이썬3에 기본 내장되어 있음
	- 파일 또는 메모리에 DB 생성
	- 참고자료: [SQLite로 가볍게 배우는 데이터베이스](https://wikidocs.net/book/1530)

- 데이터 타입
	- 동적 데이터 타입 
	- Null, Integer, Real, Text, Blob 유형이 있음 (Boolean, Date, Time 없음) 
	-  다른 유형 데이터를 삽입해도 컬럼에 맞게 알아서 들어감. 
	-  다른 DB에서 사용하는 데이터유형 이름 그대로 사용해도 무방

- DBMS 관리 툴 
	- [SQLite Expert](http://www.sqliteexpert.com/download.html)
	- Personal version은 freeware 이므로 사용할 수 있음

<br>

## **2. 파이썬과 함께 사용하기**

### 2.1 데이터베이스 접속 

#### 2.1.1 기본적인 방법 

```{.python}  
import sqlite3 
conn = sqlite3.connect(':memory:') # 메모리 DB 접속(일회성) 
# conn = sqlite3.connect(‘./test.db') # 파일 DB 접속(일회성)
```
```
...
쿼리수행
...
```

```{.python}
conn.commit() # 변경사항 저장
conn.close()
```


#### 2.1.2 with문 이용해 close 생략하는방법 

```{.python}
import sqlite3 
conn = sqlite3.connect(‘./test.db')

with conn: 
	cur = conn.cursor() 
	cur.execute(“SELECT * FROM test_table") 
	rows = cur.fetchall() 
	for row in rows: 
		print(row)
```

<br>

### 2.2 테이블 생성

```{.python}
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS Eagles \
    (back_no INT NOT NULL, \
     name TEXT, \
     position TEXT, \
     hands TEXT, \
     highschool TEXT, \
     height INT, \
     PRIMARY KEY(back_no));')
```

<br>

### 2.3 테이블 추가 

```{.python
cur = conn.cursor()
cur.execute("INSERT INTO Eagles VALUES \
    (1, '하주석', '내야수', '우투좌타', '신일고', 184), \
    (28, '양성우', '외야수', '우투좌타', '충암고', 177);")

# INSERT INTO table_name (fiel1, file2, ...) VALUES ( data );
```

<br>

### 2.4 테이블 삭제 방법 (삭제할 필요가 있을 때 사용)
```{.python}
cur.execute(‘DROP TABLE Eagles’)
```

<br>

### 2.5 테이블 변경사항 저장 
```{.python}
conn.commit()
```

<br>

### 2.6 파이썬으로 csv 파일을 읽은 후 데이터베이스에 추가 

#### 2.6.1 파이썬으로 csv 파일 읽기 

```{.python}
import pandas as pd

players = pd.read_csv('./players.csv', encoding='EUC-KR')  # 인코딩, 경로 주의 
players  # 데이터 타입이 모두 문자열 
```

#### 2.6.2 읽은 파일을 데이터베이스에 저장 

```{.python}
cur = conn.cursor()
sql = 'INSERT INTO Eagles VALUES (?, ?, ?, ?, ?, ?);'
for i in range(10):
    cur.execute(sql, (int(players.iloc[i,0]), # 데이터 타입 주의
                      players.iloc[i,1], players.iloc[i,2], 
                      players.iloc[i,3], players.iloc[i,4], 
                      int(players.iloc[i,5])))
		      
conn.commit() # 변경사항 저장 
```

<br>

## **3. 데이터 조작 언어(Data Manipulation Language, DML)**

### **1. 데이터 조회** 

```{.python}

# 1.1 순회 조회

cur = conn.cursor()
cur.execute('SELECT * FROM Eagles')
for row in cur:
    print(row)
    
# 1.2 단건 조회

cur=conn.cursor()
cur.execute('SELECT * FROM Eagles')
row = cur.fetchone()
print(row)

# 1.3 다건 조회

rows = cur.fetchmany(2)
for row in rows:
    print(row)


# 1.4 모두 조회

rows = cur.fetchall()
for row in rows:
    print(row)

# 1.5 필요한 column만 조회

# 1.5.1
cur = conn.cursor()
cur.execute('SELECT name FROM Eagles WHERE back_no > 10')  # back_no가 10 초과인 야구선수의 이름 조회
rows = cur.fetchall()

for row in rows:
    print(row)

# 1.5.2
cur = conn.cursor()
cur.execute("SELECT * FROM Eagles WHERE position like '내야수'")  # 포지션이 내야수인 야구선수 조회 
rows = cur.fetchall()

for row in rows:
    print(row)


# 1.6 원하는 순서 및 개수

# 1.6.1
cur.execute('SELECT * FROM Eagles ORDER BY height DESC')  # 키에 따른 내림차순 정렬 
rows = cur.fetchall()

for row in rows:
    print(row)

# 1.6.2
cur.execute('SELECT * FROM Eagles ORDER BY height DESC LIMIT 5')  # 키에 따른 내림차순 정렬 top5 
rows = cur.fetchall()

for row in rows:
    print(row)

# 1.7 집계 함수

# 1.7.1 카운팅
cur.execute('SELECT count(*) FROM Eagles')
count = cur.fetchall()
print(count)


# 1.7.2 그룹핑, 집계 함수 

cur = conn.cursor()
cur.execute('SELECT position, count(*), avg(height) FROM Eagles GROUP BY position')  # 포지션별 수, 평균키
rows = cur.fetchall()

for row in rows:
    print(row)

# 1.8 Placeholder
cur = con.cursor() 
back_no = 50 
cur.execute('SELECT * FROM Eagles WHERE back_no=?;‘, (back_no,)) 
player = cur.fetchone() 
print(player[0]) # 50

```
<br>

### **2. 데이터 변경** 

- UPDATE table SET field1 = value1, ... WHERE 조건;

```{.python}
cur = conn.cursor()
cur.execute("UPDATE Eagles SET hands ='우투좌타', highschool='미국고', \
            height = 190 WHERE back_no = 30;")
conn.commit()
```

### **3. 데이터 삭제**

- DELETE FROM table WHERE 조건;

```{.python}
cur = con.cursor() 
cur.execute(‘DELETE FROM Eagles WHERE back_no=1);’)
```

### **4. 종료하기** 

```{.python}
conn.close()
```
