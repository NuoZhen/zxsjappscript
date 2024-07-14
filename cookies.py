"""
Cookie模块
"""

import json


# 保存Cookie
def save_cookies(driver, filename):
    """保存当前浏览器的cookies到指定文件"""
    with open(filename, 'w') as f:
        json.dump(driver.get_cookies(), f)


# 读取Cookie
def read_cookies(driver, filename):
    """从文件中读取cookies并添加到浏览器"""
    try:
        with open(filename, 'r') as f:
            cookies_list = json.load(f)
            for cookie in cookies_list:
                driver.add_cookie(cookie)
            driver.refresh()
    except FileNotFoundError:
        print("Cookie文件未找到，请先登录保存Cookie。")
        return False
    except json.JSONDecodeError:
        print("Cookie文件格式错误，请检查文件内容。")
        return False
    return True

