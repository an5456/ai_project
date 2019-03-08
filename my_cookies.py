from selenium import webdriver
import time
import os
import json

driver = webdriver.Chrome("/home/an5456/下载/chromedriver")


# 获取并且保存cookies
def save_cookies():
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    # 保存cookies到文件中
    cookies = driver.get_cookies()
    with open(file_path + 'jd.cookies', 'w') as c:
        c.write(json.dumps(cookies))
        # json.dumps(cookies,c)
    print(cookies)


def get_url_with_cookie():
    # 首先获取项目路径,进而获取cookies文件存储的路径
    prject_path = os.path.dirname(os.getcwd())
    file_path = prject_path + "/cookies/"
    cookies_file = file_path + "jd.cookies"

    # 读取cookies信息
    jd_cookies_file = open(cookies_file, "r")
    jd_cookies_str = jd_cookies_file.readline()

    # 加载cookies信息
    jd_cookies_dict = json.loads(jd_cookies_str)

    # 这个地方必须先访问一下网站,然后把旧的cookies删除,再把我们保存的cookies添加进去
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()

    for cookie in jd_cookies_dict:
        print(cookie)
        driver.add_cookie(cookie)

    driver.get("https://order.jd.com/center/list.action")




def login():
    driver.get("http://www.jd.com")
    # 浏览器最大化
    # driver.maximize_window()
    # 设置固定的浏览器的大小
    # driver.set_window_size(1920,1080)
    driver.find_element_by_class_name("link-login").click()
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_id("loginname").send_keys("an5456")
    driver.find_element_by_id("nloginpwd").send_keys("dong19871103")
    driver.find_element_by_id("loginsubmit").click()
    save_cookies()


if __name__ == '__main__':
    login()
    # get_url_with_cookie()
