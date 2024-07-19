from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import article
import comment
import cookies
import like
import login
import logging
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

# 配置日志
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# 打开URL
def open_url(url):
    driver.maximize_window()  # 最大化窗口
    driver.get(url)  # 获取URL
    driver.implicitly_wait(5)  # 等待加载完成


if __name__ == '__main__':
    # 程序开始
    logger.info("程序开始执行...")

    open_url(url)
    time.sleep(random.randint(1, 3))

    if login.login_by_cookies(driver):
        # 点赞
        like.like_and_cancel(driver)

        # 发表评论
        article.article_comment(driver)

        # 发表文章
        article.article_post(driver)

        # 删除文章测试
        # open_url('https://zxsj.wanmei.com/zxworld/zxqsj-publish/article-detail.html?aid=')
        # article.article_delete(driver)

        # 删除评论
        comment.comment_delete(driver)

        # 关闭浏览器
        driver.close()
    else:
        logger.error("请重新启动程序！")

    logger.info("程序完成,退出成功！")
