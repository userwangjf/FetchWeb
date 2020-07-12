
import requests

def fetchHtml(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status() # 如果响应状态码不是200，就主动抛出异常
    except requests.RequestException as e:
        print("Fetch Html ERR: " + str(e))
    else:
        print("Fetch Html OK : " + url)
        return resp.content.decode("utf-8") #解码后返回字符串

#测试
if __name__ == "__main__":
    fetchHtml("https://www.runoob.com/python/python-basic-syntax.html")
    fetchHtml("//www.runoob.com/python/python-basic-syntax.html")
    fetchHtml("http://www.sina.com.cn/abcadfadsf")
    #fetchHtml("http://192.168.1.2")
