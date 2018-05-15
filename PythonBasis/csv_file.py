#encoding=utf-8
import csv
csv_file=csv.reader(open('stu_info.csv','r'))
print(csv_file)

for stu in csv_file:
    print(stu[2])


stu=['Marry',28,'shanghai']
stu1=['Rom',23,'chengdu']
out=open('stu_info.csv','a',newline='')
csv_write=csv.writer(out,dialect='excel')
csv_write.writerow(stu)
csv_write.writerow(stu1)
print("写入完毕!")
