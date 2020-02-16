import pandas as pd
import pymysql
import numpy as np

df = pd.read_excel(r"D:\My\data\ex.xlsx",keep_default_na=False)
print(df)
# df['salary'] = df['salary'].replace('','Null')
# print(df)
conn = pymysql.connect('localhost', 'root', 'rock1204', 'student')
cursor = conn.cursor()

list = []
# sql = "insert into worker(id,name,salary,gender) values (%d,%s,%s,%s)" % (id,name,salary,gender)
for i in range(df.shape[0]):
    id = int(df.loc[i,'id'])
    name = df.loc[i,'name']
    gender = df.loc[i,'gender']
    salary = str(df.loc[i,'salary'])

    name = 'Null' if not name else  "'" + name + "'"
    gender = 'Null' if not gender else "'" + gender + "'"
    salary = 'Null' if not salary else "'" + salary + "'"
    t = ((id,name,salary,gender))
    list.append(t)
print(list)

sql = "insert into worker(id,name,salary,gender) values (%d,%s,%s,%s)"

try:
    # cursor.executemany(sql,list)
    cursor.executemany(sql,[(39, 'Null', 'Null', "'sa'"), (40, 'Null', "'12'", 'Null'), (41, "'ww'", 'Null', 'Null')])
    print(sql)
    conn.commit()
except Exception as e:
    conn.rollback()
    print("执行: %s,出错：%s" % (sql, e))


cursor.close()
conn.close()

print('just for test')
print('test aggin')


