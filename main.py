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
cookie_str = 'puclic_hg_flag2=true; wmCurrGame=%7B%22id%22%3A61%2C%22name%22%3A%22%E8%AF%9B%E4%BB%99%E4%B8%96%E7%95%8C%22%2C%22icon%22%3A%22https%3A%2F%2Fimg.games.wanmei.com%2Frms%2Fsta%2F20220906%2Fe9a4ca5bcdd7460ea457a6b11afd70b9.png%22%2C%22type%22%3A%22mobile%22%2C%22hot%22%3A0%2C%22wanmei_login%22%3A0%2C%22qq_login%22%3A0%2C%22wechat_login%22%3A0%2C%22weibo_login%22%3A0%2C%22services%22%3A0%2C%22hide%22%3A0%2C%22bg%22%3A%22https%3A%2F%2Fimg.games.wanmei.com%2Frms%2Fsta%2F20220809%2Fda146e48dd574120a1d9845494caf417.jpg%22%7D; __mtxud=bd4eb373451a4ebb.1694517992760.1720456750478.1720699938209.51; __mtxsr=csr:games.wanmei.com|cdt:/m/|advt:(none)|camp:(none); Hm_lvt_18c8ee3fe6e688791a70d49c29a803d4=1719070007,1719228902,1720700178; relogon=MTI1ODE4MDE4%7C6K%2B66Ie7%7CMWIwMTI4M2FjNmMyNDA3NTgwNDYyYWVmNTAwYWE3ZTg%3D%7C953efcd4595f556f1be1b2095b3e3c0c; settime=1720850959626; logon=MTI1ODE4MDE4%7C6K%2B66Ie7%7CMWIwMTI4M2FjNmMyNDA3NTgwNDYyYWVmNTAwYWE3ZTg%3D%7C953efcd4595f556f1be1b2095b3e3c0c; showLogon=MTI1ODE4MDE4%7C6K%2B66Ie7%7CMWIwMTI4M2FjNmMyNDA3NTgwNDYyYWVmNTAwYWE3ZTg%3D%7C953efcd4595f556f1be1b2095b3e3c0c; headImg=https://safestatic.games.laohu.com/i/headimg/pc/1_60_60.png; wmLogon=MTI1ODE4MDE4%7C6K%2B66Ie7%7CMWIwMTI4M2FjNmMyNDA3NTgwNDYyYWVmNTAwYWE3ZTg%3D%7C953efcd4595f556f1be1b2095b3e3c0c; wmHeadImg=https://safestatic.games.laohu.com/i/headimg/pc/1_60_60.png; nickname=%E8%AF%BA%E8%87%BB; avatar=https%3A%2F%2Fxinzhuxianapp-1251008858.file.myqcloud.com%2Fimg%2Fuser%2Favatar%2F20231121%2F125818018%2F652337a6d6c8330e8572579b73de9c361700554571796.jpg; uid=125818018; Hm_lvt_132102418c9639c7122592f507661f29=1720769082,1720847689,1720861601,1720925802; HMACCOUNT=A4827A322F2D9C90; Hm_lpvt_132102418c9639c7122592f507661f29=1720940495; credential=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXlsb2FkIjoiMTI1ODE4MDE4IiwiZXhwIjoxNzIxNTQ1Mjk2fQ.6UHwJZiWsdXckuu2bCKX5XuYlqTgxKNjMqqmbMQEHmo'

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
    comment.comment_delete(driver)

    # article.article_delete(driver)
    # like.like_and_cancel(driver)
    # article.article_comment(driver)
    # url_info()
    # article.article_post(driver)
    # 关闭浏览器
    # driver.close()
