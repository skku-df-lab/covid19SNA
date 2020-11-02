## json2csv.py 

#### Add Modules
<pre><code>
import json
import csv  
</code>
</pre>

#### Import JSON file(LocationHistory.json)
<pre><code>
with open('LocationHistory.json') as json_file:  
    data = json.load(json_file)  
employee_data = data['locations']  
</code>
</pre>

#### Create CSV file(LocationHistory.csv)
<pre><code>
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

