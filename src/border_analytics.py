import sys
import csv
import copy
import math

if __name__ == "__main__":
	input_file=sys.argv[1]
	output_file=sys.argv[2]
	groupBy_dict={}
	with open(input_file) as csv_file:
		next(csv_file)
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			border=row[3]
			date=row[4]
			measure=row[5]
			val=row[6]
			key_tuple=(border, date, measure)
			if key_tuple not in groupBy_dict.keys():
				groupBy_dict[key_tuple]= int(val)
			elif key_tuple in groupBy_dict.keys():
				groupBy_dict[key_tuple]=groupBy_dict[key_tuple]+int(val)
	
	answer=copy.deepcopy(groupBy_dict)
	for k, v in answer.items():
		answer[k]=[v]
	
	for k, v in groupBy_dict.items():
		border=k[0]
		date=k[1]
		year=int(date.split()[0].split('/')[2])
		month=int(date.split()[0].split('/')[0])
		measure=k[2]
		average=0
		preceding_total=0
		for key, val in groupBy_dict.items():
			key_year=int(key[1].split()[0].split('/')[2])
			key_month=int(key[1].split()[0].split('/')[0])
			
			if key[0]==border and key[2]==measure and key_year==year and key_month<month:
				preceding_total=preceding_total+val
		
		if month-1==0:
			average=0
		elif month-1>0:
			average=math.ceil(preceding_total/(month-1))
		
		if k in answer.keys():
			answer[k].append(average)
	
	arr=[]
	for k, v in answer.items():
		arr.append([k[0], k[1], k[2], v[0], v[1]])
	
	arr.sort(key=lambda k: (k[1],k[3], k[2], k[0]),reverse=True)
	header=['Border','Date','Measure','Value','Average']
	with open(output_file, "w", newline="") as f:
		writer = csv.writer(f)
		writer.writerow(i for i in header)
		writer.writerows(arr)
	input_file.close()
	output_file.close()
	