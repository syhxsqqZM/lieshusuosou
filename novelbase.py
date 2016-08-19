# coding:UTF-8
import MySQLdb
import sys
from novelcrawler import get_obj_list

def database(keywords, search_url):
    # connect( “主机名”， “用户名”， “登陆密码”， “数据库名” )
    # 重要，默认使用UTF-8编码：charset="utf8"
    db = MySQLdb.connect("localhost","root","","test",charset="utf8")
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    
    # 如果数据表已经存在使用 execute() 方法删除表。
    # cursor.execute("DROP TABLE IF EXISTS SEARCH__RESULT")
    
    # SQL 删除语句
    sql = "DELETE FROM BOOK WHERE i<100"
    
    # 执行SQL语句
    cursor.execute(sql)
    db.commit()

    # 获取所有记录列表
    
        # 执行sql语句
    obj_list = []
    obj_list += get_obj_list(search_url[0])
    obj_list += get_obj_list(search_url[1])
    obj_list += get_obj_list(search_url[2])
    obj_list += get_obj_list(search_url[3])
    obj_list += get_obj_list(search_url[4])
    obj_list += get_obj_list(search_url[5])
    
    for i, obj in enumerate(obj_list):
        # print obj
        title = obj['title']
        img = obj['img']
        url = obj['url']
        author = obj['author']
        content = obj['content']
        status=obj['status']
        
            # Python格式化字符串为：格式标记字符串 % 要输出的值组
            # /为Python中的续行符
        sql = 'INSERT INTO BOOK VALUES("%s", "%d", "%s", "%s", "%s", "%s", "%s","%s")'  \
            % (keywords, i, title, img, url, author, content,status)
        cursor.execute(sql)
            # 提交到数据库执行
        db.commit()
    sql = "SELECT * FROM BOOK WHERE KEYWORDS = '%s'" % (keywords)
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    db.close() 
    
    
    
if __name__ == '__main__':
    keywords = sys.argv[1].decode('GBK').encode('UTF-8')
    search_url = [  "http://xiaoshuo.sogou.com/search/?key=" + keywords + "&page=1",
                    "http://xiaoshuo.sogou.com/search/?key=" + keywords + "&page=2",
                    "http://xiaoshuo.sogou.com/search/?key=" + keywords + "&page=3",
                    "http://www.yuncheng.com/search?q=" + keywords + "&pn=1",
                    "http://www.yuncheng.com/search?q=" + keywords + "&pn=2",
                    "http://www.yuncheng.com/search?q=" + keywords + "&pn=3"]
                   
    database(keywords, search_url)

