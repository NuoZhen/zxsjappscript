"""
登录模块
"""

import cookies
import json
import logging
import utils

from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Cookie登录
def login_by_cookies(driver, filename='cookies.txt'):
    """使用提供的Cookie字符串或文件中的cookies进行登录"""

    # 尝试从文件中读取cookies
    try:
        cookies_loaded = cookies.read_cookies(driver, filename)
        if cookies_loaded:
            return True
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"读取Cookies时发生错误: {e}")
        return False

    # 如果没有从文件加载cookies成功，则尝试从用户输入获取
    if not cookies_loaded:
        cookie_str = input("请输入你的Cookie：")
        if not cookie_str:
            logger.error("请填写Cookie！")
            return False

        try:
            # 将Cookie字符串转换为json格式，并保存到指定文件
            json_cookies = utils.parse_cookie_string(cookie_str)
            with open(filename, 'w') as f:
                json.dump(json_cookies, f)
            # 从文件中读取cookies并登录
            cookies.read_cookies(driver, filename)
            if test_login(driver, filename):
                return True
        except Exception as e:
            logger.error(f"Cookie解析错误: {e}")
            return False


# 检查是否已经登录
def test_login(driver, filename):
    try:
        driver.find_element(By.CLASS_NAME, "login-btn")
        logger.error("登录失败，Cookie存在问题！")
        return False
    except NoSuchElementException:
        # 登录成功保存最新的cookies
        cookies.save_cookies(driver, filename)
        logger.info("登录成功！")
        # 此处其实应该访问用户的消息，判断是否完成任务
        logger.info("登录任务完成！")
        return True

