import pymysql
import re

def get_conn():
    conn = pymysql.connect(host="localhost", user="root", password="1234", database="test")
    return conn

def connection_insert(insert_sql,data):
    """批量插入数据"""
    db = get_conn()
    db_curs = db.cursor()
    try:
        db_curs.executemany(insert_sql, data)
        db.commit()
        print('ok')
    except:
        db.rollback()
        print('insert error')
    db.close()


def connection_creTable(cre_sql):
    """创建表"""
    db = get_conn()
    db_curs = db.cursor()
    db_curs.execute(cre_sql)
    db.commit()
    db.close()
    db_curs.close()


def table_exists(table_name):
    """判断表是否存在"""
    db = get_conn()
    db_curs = db.cursor()
    db_curs.execute('show tables;')
    tables = [db_curs.fetchall()]
    table_list = re.findall('(\'.*?\')', str(tables))
    table_list = [re.sub("'", '', each) for each in table_list]
    if table_name in table_list:
        return True
    else:
        return False


def update_table(sql,args):
    """
    更新操作，示例如下：
    sql = 'UPDATE test_student_table SET NAME=%s WHERE id = %s;'
    args = ('zhangsan', 1)
    update_table(sql, args)
    """
    conn = get_conn()
    cur = conn.cursor()
    result = cur.execute(sql,args)
    print(result)
    conn.commit()
    cur.close()
    conn.close()


def delete_table(sql,args):
    """
    删除操作，示例如下：
    sql = 'DELETE FROM test_student_table WHERE id = %s;'
    args = [1]
    delete_table(sql, args)
    """
    conn = get_conn()
    cur = conn.cursor()
    result = cur.execute(sql,args)
    print(result)
    conn.commit()
    cur.close()
    conn.close()


def query_table(sql,args):
    """
    查询操作，示例如下：
    sql = 'SELECT  * FROM test_student_table;'
    query(sql,None)
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql,args)
    results = cur.fetchall()
    # print(type(results))  # 返回<class 'tuple'> tuple元组类型
    # print(results)
    conn.commit()
    cur.close()
    conn.close()
    return results


if __name__ == '__main__':
    pass



