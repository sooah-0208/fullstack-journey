# pandas에서 sql 실행하기
```
import pandas as pd
result = pd.read_sql_query("select * from edu.`melon` where genre = 'GN0600'",engine_mariadb)
```
# jupyter로 data 저장하기
```
result.columns = ["id","img","title", "album", "cnt", "genre","regDate","modDate"]
result.head()
# 값 잘 불러오는지 확인용(result.컬럼명)
result.title

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Study02Sooah").master("spark://master:7077").getOrCreate()

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Study02Sooah").master("spark://master:7077").getOrCreate()

sDf = spark.createDataFrame(result)
sDf.show()
sDf.coalesce(1).write.format("com.databricks.spark.csv").option("header","true").save(path="/opt/spark2/data/study2_sooah.csv",format="csv",mode="overwrite")
```

- `sDf.coalesce(1).write.format("com.databricks.spark.csv").option("header","true").save(path="/opt/spark2/data/study2_sooah.csv",format="csv",mode="overwrite")
`:  앞의 format은 고정, 옵션도 고정, save의 path경로 확인잘하기, 뒤의 format은 확장자명, mode는 설정옵션
- mode 예시:
| 설정값 (mode) | 설명 | 비유 💡 |
| :--- | :--- | :--- |
| **`"overwrite"`** | 기존 데이터를 **모두 지우고** 새로 덮어씁니다. | 기존 책을 다 버리고 새 책을 꽂음 🗑️ |
| **`"append"`** | 기존 데이터 끝에 **새 데이터를 추가**합니다. | 기존 책 옆에 새 책을 꽂음 ➕ |
| **`"ignore"`** | 데이터가 이미 있으면 **아무 작업도 하지 않습니다.** | 책이 이미 있네? 그냥 돌아감 🤷‍♂️ |
| **`"error"`** | 데이터가 이미 있으면 **에러를 발생**시킵니다. (기본값) | "책이 이미 있어!"라고 소리침 ⚠️ |