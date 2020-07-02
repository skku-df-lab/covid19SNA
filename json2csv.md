
### 구글 takeout에서 위치정보인 LocationHistory.json 파일을 다운받는 것으로부터 시작

## json2csv.py 

#### 필요한 함수 추가
<pre>
<code>
import json
import csv
</code>
</pre>

#### JSON파일(LocationHistory.json)을 가져오는 작업
<pre>
<code>
with open('LocationHistory.json') as json_file:  
    data = json.load(json_file)  
employee_data = data['locations']  
</code>
</pre>

#### CSV파일(LocationHistory.csv)을 생성하는 작업
<pre>
<code>
csv_writer = csv.writer(data_file)

count = 0

for emp in employee_data:
  if count == 0:
    header = emp.keys()
    csv_writer.writerow(header)
    count += 1
  csv_writer.writerow(emp.values())

data_file.close()
</code>
</pre>

