from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import article
import comment
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


def url_info():
    # 请求一系列关于浏览器的信息, 包括窗口句柄、浏览器尺寸/位置、cookie、警报等
    print(f"当前页面标题：{driver.title}")
    print(f"当前页面URL：{driver.current_url}")


if __name__ == '__main__':
    open_url(url)
    time.sleep(random.randint(1, 3))
    login.login_by_cookies(driver, cookie_str)

    like.like_and_cancel(driver)

    article.article_comment(driver)

    article.article_post(driver)

    comment.comment_delete(driver)

    # url_info()

    # 关闭浏览器
    driver.close()
    print("程序完成,退出成功！")
