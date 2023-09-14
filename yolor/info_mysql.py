
import pymysql



class MySql():

    def __init__(self):
        pass
    def get_conn(self):
        #连接数据库
        conn = pymysql.connect(host='127.0.0.1',
                                user='root',
                                port=3306,
                                db = "fire_smog_info",
                                password='abc123',
                                charset='utf8'
                                )
        return conn
    def select_all(self):
        conn  = self.get_conn()
        cur=conn.cursor()   #创建游标对象
        sql='SELECT * from info_record'
        try:
            cur.execute(sql)    #执行sql语句
            data=cur.fetchall()
            #print(data)
            return data
        except:
            print("error")
        finally:
            cur.close()#关闭游标
            conn.close()#关闭连接
    #select conditional
    def search_record(self,lt):
        conn = self.get_conn()
        cur = conn.cursor()
        global sql
        sql = "select * from info_record where location ='%s' "%(lt[0])
        if lt[1]!='':
            sql+="and cam_id='%s' "%(lt[1])
        if lt[2]!='':
            sql+="and loc_pos = '%s' "%(lt[2])
        if lt[3]!='':
            sql+="and log_date = '%s'"%(lt[3])
        sql += " order by log_time"
        print(sql)
        try:
            cur.execute(sql)
            data = cur.fetchall()
            #print(data)
            return data
        except:
            print('print error!!')
        finally:
            cur.close()
            conn.close()
    #insert into table
    def insert_record(self,ls):
        
        conn = self.get_conn()
        cur = conn.cursor()
        sql = "insert into info_record(location,cam_id,loc_pos,`logs`,log_date,log_time)values('%s','%s','%s','%s','%s','%s')"%(ls[0],ls[1],ls[2],ls[3],ls[4],ls[5])
        # cur.execute(sql)
        # conn.commit()
        # cur.close()#关闭游标
        # conn.close()#关闭连接
        try:
            cur.execute(sql)
            conn.commit()
        except:
            print("Error")
        finally:
            cur.close()#关闭游标
            conn.close()#关闭连接

