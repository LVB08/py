import  pymysql
import re
import mySQLop


def test_creTable():
    """测试创建数据库表格"""
    if not (mySQLop.table_exists('test_info')):
        cre_sql = """create table test_info(num int unsigned auto_increment,
                      name char(100),
                      primary key (`num`)
                      )engine=InnoDB DEFAULT CHARSET=utf8
                      """
        mySQLop.connection_creTable(cre_sql)
    print(mySQLop.table_exists('test_info'))

def test_update():
    """测试更新数据库表数据"""
    sql = 'UPDATE test_info SET name=%s WHERE name = %s;'
    args = ('zhangsan', 'ddd')
    mySQLop.update_table(sql, args)


def test_delete():
    """测试删除数据库表数据"""
    sql = 'DELETE FROM test_info WHERE num = %s;'
    args = [1]
    mySQLop.delete_table(sql, args)


def test_query():
    """测试查询操作"""
    sql = 'select * from test_info;'
    print(mySQLop.query_table(sql, None))


if __name__ == '__main__':
    pass