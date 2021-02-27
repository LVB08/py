import pymysql


def connection_sql(singer_data):
    db = pymysql.connect(host="localhost", user="root", password="1234", database="test")
    db_curs = db.cursor()
    insert_sql = """insert into singer_info (type,name,gender,area,initials) 
                    values (%s,%s,%s,%s,%s)"""
# singer_data = [['歌手','邓紫棋1','女','大陆','D'],['歌手','邓紫棋2','女','大陆','D'],['歌手','邓紫棋3','女','大陆','D']]
    try:
        db_curs.executemany(insert_sql, singer_data)
        db.commit()
        print('ok')
    except:
        db.rollback()
        print('insert error')
    db.close()


