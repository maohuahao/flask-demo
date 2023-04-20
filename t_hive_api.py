from impala.dbapi import connect


class OperatorHive():

    # 初始化hive数据库连接
    def __init__(self, host, port, user, password, database=None):
        self.conn = connect(host=host, port=port, database=database, user=user, password=password, auth_mechanism="PLAIN")
        self.cur = self.conn.cursor()

    # 查看数据库
    def show_database(self):
        self.cur.execute("show databases")
        print(self.cur.fetchall())

    # 查看数据库中的表
    def show_table(self):
        self.cur.execute("show tables")
        print(self.cur.fetchall())

    # 从hdfs中导入数据到hive表中
    def load_hive_data(self, hdfs_path, hive_table):
        try:
            self.cur.execute(f"load data inpath '{hdfs_path}' into table {hive_table}")
            print("导入成功")
        except Exception as e:
            print(e)

    # 关闭连接
    def close(self):
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    ophive = OperatorHive('cdh99', 10000,'root', 'cqie', 'team5')
    ophive.show_table()
    ophive.close()