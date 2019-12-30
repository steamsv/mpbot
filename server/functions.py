import datetime
import psutil
from process import Process
import pymysql
from settings import Settings


def get_all_process():
    ps = []
    pids = psutil.pids()
    for pid in pids:
        try:
            process = psutil.Process(pid)
        except psutil.NoSuchProcess as e:
            print(e)
        else:
            p = Process(pid, process.name(), process.status())
            ps.append(p)
    return ps


# 该函数根据进程名来查找进程，返回第一个找到的pid，没找到返回-1
def get_pid_by_name(name):
    ps = get_all_process()
    for p in ps:
        if p.name == name:
            return p.pid
    return -1


# 将进程数据插入表
def insert_into(p: Process):
    connection = pymysql.connect(
        host=Settings.HOST,
        port=Settings.PORT,
        user=Settings.USERNAME,
        password=Settings.PASSWORD,
        database=Settings.DB,
        charset=Settings.CHARSET
    )
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO " + Settings.TABLE + \
                  " (sid, pid, pname, status, time) " \
                  "VALUES (%s, %s, %s, %s, %s)"
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute(sql, (Settings.SID, p.pid, p.name, p.status, dt))
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    finally:
        connection.close()
