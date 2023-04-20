from hdfs import *

# 创建hdfs连接客户端
client = InsecureClient("http://cdh99:9870", root="/", user='root')


# 获取目录列表
def get_hdfs_list(dst_path: str) -> None:
    print(client.list(dst_path))


# 上传本地文件
def put(hdfs_path: str, local_path: str) -> None:
    try:
        put_hdfs_path = client.upload(hdfs_path, local_path)
        print(hdfs_path)
    except HdfsError as e:
        print(e)
        print("文件以存在")

# 下载hdfs的文件到本地
def get(hdfs_path: str, local_path: str, overwrite=False):
    try:
        get_local_path = client.download(hdfs_path, local_path, overwrite=overwrite)
        print(get_local_path)
    except HdfsError as e:
        print(e)
        print("文件已存在")

# 删除hdfs上的文件或文件件
def delete(hdfs_path: str, recursive=False):
    try:
        client.delete(hdfs_path, recursive=recursive)
    except HdfsError as e:
        print(e)
        print("文件夹不为空")


if __name__ == '__main__':
    # 获取hdfs更路径下的所有目录或文件
    get_hdfs_list("/")

    # 上传文件
    # put("/mhh", 'superset.py')

    # 删除文件
    # delete('/mhh', recursive=True)

    # 下载hdfs上的文件
    # get("/tmp/superset.py", './')
