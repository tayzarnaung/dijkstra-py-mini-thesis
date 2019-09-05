import pandas as pd
import csv
print(float('nan'))
conn= {}
with open('distance_csv/dist.csv', 'r') as readFile:
	reader = csv.reader(readFile)	
	for row in reader:
	    # data_rows.append([cell.value for cell in row])
		for column in row:
		    # if column is not None:
		    # 	print('hi');
		    print(column)	        
	    	# else: continue		

	# lines = list(reader)
	# lines[2] = row
# with open('distance_csv/people.csv', 'w') as writeFile:
#     writer = csv.writer(writeFile)
#     writer.writerows(lines)
readFile.close()
# writeFile.close()