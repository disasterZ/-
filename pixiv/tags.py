from pixiver.pixiv import Pixiv
import openpyxl

#获取标签函数
def get_tag(id):
    #创建列表并写入id
    tags=[]
    tags.append(id)
    #pixiv操作
    p = Pixiv()
    print(id)
    pw = p.works(id)
    li=pw.view_tags()['tags']
    #添加标签
    for i in li:
        tags.append(i['tag '])
    print("%s finsh"%(tags))
    #写入xlsx
    wb = openpyxl.load_workbook('tags.xlsx')
    table = wb['Sheet1']
    table.append(tags)
    wb.save('tags.xlsx')
    wb.close()

if __name__=='__main__':
    wb=openpyxl.load_workbook('pixivHot.xlsx')
    table=wb['Sheet1']
    for i in range(1,len(table['A'])):
        print(i)
        get_tag(table['A'][i].value)
    wb.close()
