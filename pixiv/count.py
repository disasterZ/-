from collections import Counter
import openpyxl

tags=[]
#获取所有tags
wb=openpyxl.load_workbook('tags.xlsx')
sheet=wb['Sheet1']
for i in sheet.rows:
    for k in i:
        if(k.value!=None):
            tags.append(k.value)
wb.close()
result=Counter(tags)
wb1=openpyxl.load_workbook('tagCount.xlsx')
table=wb1['Sheet1']
count=1
for i in result:
    list=[]
    list.append(i)
    list.append(result[i])
    table.append(list)
    wb1.save('tagCount.xlsx')
    print(count)
    count=count+1
wb1.close()