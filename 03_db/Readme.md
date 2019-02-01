# 03_project

1. 테이블 구성하기 (파일명 : 01_create_table.sql )

  * 아래의 순서에 맞춰 쿼리문을 작성 해주세요.

  1. 아래와 같은 스키마를 가진 movies 테이블을 만드세요.

```sql
CREATE TABLE movies (
    '영화코드' INTEGER PRIMARY KEY,
    '영화이름' TEXT,
    '관람등급' TEXT,
    '감독' TEXT,
    '개봉연도' DATE,
    '누적관객수' INTEGER,
    '상영시간' INTEGER,
    '제작국가' TEXT,
    '장르' TEXT
);
```

​	2. header와 mode 설정을 적절하게 하세요.

```sql
-- import boxoffice csv
.mode csv
.import boxoffice.csv movies

.headers on
.mode column

```

​	3. 전체 데이터를 출력하세요.

```sql
SELECT * FROM movies;
```



```bash
ls
---
sqlite3 pjt.sqlite3
.read 01_create_table.sql
```

*쿼리문 : 질문을 통하여 문장을 작성하여 호출하는 방법.



2. 기본 CRUD 조작하기 (파일명: 02_crud.sql )

  * 아래의 순서에 맞춰 쿼리문을 작성 해주세요.

  1. 최근 영화 극한직업이 누락되어 있습니다. 영진위 API에서 얻은 정보에 따르면, 위와 같습니
    다. 해당 레코드를 테이블에 추가 해주세요.

```sql
INSERT INTO movies('영화코드', '영 화이름', '관람등급', '감독', '개봉연도', ' 
누적관객수', '상영시간', '제작국가', '장르')VALUES(20182530, '극한직업', '15세이상관람
가', '이병헌', '20190123', '3138467', '111'
, '한국', '코미디');                 
```



​	2. 데이터 수집과정에서 실수로 과거의 데이터가 포함되었습니다. 영화코드가 20040521인 데
이터를 출력하세요. 그리고, 해당 데이터를 삭제하세요. 

```sql
SELECT * FROM movies WHERE 영화코드=20040521;

DELETE FROM movies WHERE 영화코드=20040521;
```



   	3. 영화코드 20185124인 데이터를 출력하세요. 공란으로 되어 있는 컬럼에 값을 '없음'으로 수
       정하세요. 그리고 해당 데이터의 감독이 변경되었는지 확인하세요.

```SQL
SELECT * FROM movies WHERE 영화코드=20185124;

UPDATE movies SET 감독='없음' WHERE 영화코드=20185124;
```



3. 원하는 데이터 찾기 (파일명: 03_select.sql )

  * 아래의 순서에 맞춰 쿼리문을 작성 해주세요.

  1. 상영시간이 150분 이상인 영화이름만 출력하세요.

     ```sql
     SELECT 영화이름 FROM movies WHERE 상영시간>=150;
     ```

     

  2. 장르가 애니메이션인 영화코드와 영화이름를 출력하세요.

     ```sql
     SELECT 영화코드, 영화이름 FROM movies WHERE 장르='애니메이션;
     ```

     

  3. 제작국가가 덴마크이고 장르가 애니메이션인 영화이름을 출력하세요.

     ```SQL
     SELECT 영화이름 FROM movies WHERE 제작국가='덴마크' AND 장르='애니메이션';
     ```

     

     

  4. 누적관객수가 백만이 넘고, 관람등급이 청소년관람불가인 영화이름과 누적관객수를 출력하세
    요.

    ```SQL
    SELECT 영화이름, 누적관객수 FROM movies WHERE 누적관객수>1000000 AND 관람등급='청소년관람불가';
    ```

    

  5. 개봉연도가 2000년 1월 1일 ~ 2009년 12월 31일 사이인 영화를 출력하세요.

     ```SQL
     SELECT * FROM movies WHERE 개봉연도>=20000101 AND 개봉연도<20100000;
     ```

     

  6. 장르를 중복 없이 출력하세요.

     ```sql
     SELECT distinct 장르 FROM movies;   
     
     ※select * from 테이블명 where index in (select max(index) from 테이블명 group by 제목)
     [출처] https://hooni.net/1566
     
     
     ```

4. Expression 활용하기 (파일명: 04_expression.sql )

  * 아래의 순서에 맞춰 쿼리문을 작성 해주세요.

  1. 모든 영화의 총 누적관객수를 출력하세요.

     ```sql
     SELECT SUM (누적관객수) FROM movies;
     ```

     

  2. 가장 많은 누적관객수인 영화이름과 누적관객수를 출력하세요.

     ```sql
     SELECT 영화이름, MAX(누적관객수) FROM movies;
     ```

     

  3. 가장 상영시간이 짧은 영화의 장르와 상영시간을 출력하세요.

     ```sql
     SELECT 장르, MIN(상영시간) FROM movies;
     ```

     

  4. 제작국가가 한국인 영화의 평균 누적관객수를 출력하세요.

     ```sql
     SELECT AVG(누적관객수) FROM movies WHERE 제작국가='한국';
     ```

     

  5. 관람등급이 청소년관람불가인 영화의 개수를 출력하세요.

     ```sql
     SELECT COUNT(*) FROM movies WHERE 관람등급='청소년관람불가';
     ```

     

  6. 상영시간이 100분 이상이고 장르가 애니메이션인 영화의 개수를 출력하세요.

     ```sql
     SELECT COUNT(*) FROM movies WHERE 상영시간>=100 AND 장르='애니메이션';
     ```



5. 정렬하기 (파일명: 05_order.sql )

  * 아래의 순서에 맞춰 쿼리문을 작성 해주세요.

  1. 누적관객수 상위 5개 영화의 모든 데이터를 출력하세요.

      ```SQL
     SELECT * FROM movies ORDER BY 누적관객수 DESC LIMIT 5;
      ```

     

  2. 장르가 애니메이션인 영화를 제작국가(오름차순), 누적관객수(내림차순)순으로 정렬하여 10개
    만 출력하세요.

    ```SQL
    SELECT * FROM movies WHERE 장르='애니메이션' ORDER BY 누적관객수 DESC, 제작국가 ASC LIMIT 10;
    ```

    

  3. 상영시간이 긴 영화를 만든 감독의 이름을 10개만 출력하세요.

     ```SQL
     SELECT 감독 FROM movies ORDER BY 상영시간 DESC LIMIT 10;
     ```

     