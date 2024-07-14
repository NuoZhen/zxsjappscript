from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import like
import login
import random
import time


# 诛仙世界APP网页地址
url = 'https://zxsj.wanmei.com/zxworld/zxqsj-publish/circle.html'

# Cookie
cookie_str = ''

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option('detach', True)  # 设置浏览器不关闭
driver = webdriver.Edge(options=edge_options)  # 定义Edge浏览器


# chrome_options = webdriver.EdgeOptions()
# browse = webdriver.Chrome(options=chrome_options)     # 定义Chrome浏览器


# 打开URL
def open_url(url):
    driver.maximize_window()  # 最大化窗口
    driver.get(url)  # 获取URL
    driver.implicitly_wait(5)  # 等待加载完成


if __name__ == '__main__':
    open_url(url)
    # try:
    #     element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "login-btn"))
    #     )
    #     print("登录按钮已找到")
    # except:
    #     print("在规定的时间限制内，登录按钮未找到或不可见")

    time.sleep(random.randint(1, 3))
    login.login_by_cookies(driver, cookie_str)
    like.like_and_cancel(driver)

    # 请求一系列关于浏览器的信息, 包括窗口句柄、浏览器尺寸/位置、cookie、警报等
    title = driver.title
    print(title)
    print(driver.current_url)
    # 关闭浏览器
    # driver.close()
