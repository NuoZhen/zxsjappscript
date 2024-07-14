"""
登录模块
"""

import cookies
import json
import utils

from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException


# Cookie登录
def login_by_cookies(driver, cookie_str, filename='cookiestest.txt'):
    """使用提供的Cookie字符串或文件中的cookies进行登录"""
    if not cookie_str:
        if not cookies.read_cookies(driver, filename):
            print("请填写Cookie！")
            return
    else:
        try:
            # 将Cookie字符串转换为json格式，并保存到指定文件
            json_cookies = utils.parse_cookie_string(cookie_str)
            with open(filename, 'w') as f:
                json.dump(json_cookies, f)
            # 从文件中读取cookies并登录
            cookies.read_cookies(driver, filename)
        except Exception as e:
            print(f"Cookie解析错误: {e}")
            return

    # 检查是否已经登录
    try:
        driver.find_element(By.CLASS_NAME, "login-btn")
        print("登录失败，Cookie存在问题！")
    except NoSuchElementException:
        # 登录成功保存最新的cookies
        cookies.save_cookies(driver, filename)
        print("登录成功！")

