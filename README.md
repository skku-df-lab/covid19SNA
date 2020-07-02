
구글 takeout에서 위치정보인 LocationHistory.json 파일을 다운받는 것으로부터 시작.

# JSON파일(LocationHistory.json)을 가져오는 작업
![01](https://user-images.githubusercontent.com/66988643/86301185-21d8b300-bc40-11ea-81b5-baf547e5b9a3.PNG)

# CSV파일(LocationHistory.csv)을 생성하는 작업

csv_writer = csv.writer(data_file)

count = 0

for emp in employee_data:
    if count == 0:   
        header = emp.keys()
        csv_writer.writerow(header)
        count += 1        
    csv_writer.writerow(emp.values())    
    
data_file.close()


