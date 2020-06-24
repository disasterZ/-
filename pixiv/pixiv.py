from pixiver.pixiv import Pixiv
import openpyxl
from datetime import datetime
from datetime import timedelta

#获取函数 按日期排序
def GetData(start_date,end_date,date):
    #打开excel
    wb=openpyxl.load_workbook('pixivHot.xlsx')
    table=wb['Sheet1']
    # pixiv无脑操作
    p = Pixiv()
    for c_date in range(start_date,end_date):
        print('现在是%d'%(c_date))
        pr = p.rank(c_date)
        for i in range(0,30):
            # 获取数据
            pro = pr.one()
            # 创建列表
            data = []
            # 作品id
            id = pro['illust_attrs'].illust_id()
            data.append(id)
            # 标题
            title = pro['illust_attrs'].illust_title()
            data.append(title)
            # 昵称
            author = pro['illust_attrs'].author_name()
            data.append(author)
            # 作品创建日期
            create_date = pro['illust_attrs'].create_date()
            data.append(create_date)
            # 作品上传日期
            upload_date = pro['illust_attrs'].upload_date()
            data.append(upload_date)
            # 作品浏览数
            view_count = pro['illust_attrs'].view_count()
            data.append(view_count)
            # 点赞数
            like_count = pro['illust_attrs'].like_count()
            data.append(like_count)
            # 收藏数
            mark_count = pro['illust_attrs'].mark_count()
            data.append(mark_count)
            # 评论数
            comment_count = pro['illust_attrs'].comment_count()
            data.append(comment_count)
            #上榜日期
            data.append(date)
            table.append(data)
            wb.save('pixivHot.xlsx')
    date=date + timedelta(days=1)
    print("finsh")
    wb.close()


if __name__ == '__main__':
    s = datetime(2020, 2, 28)
    GetData(20200501,20200532,s)








