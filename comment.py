"""
评论模块
"""
import logging
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException, NoSuchElementException

import utils
from article import article_titles

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# 发表文章评论
def comment_post(driver):
    # 收集文章标题元素并随机一个点击
    try:
        title_elements = article_titles(driver)
        if title_elements:
            element = random.choice(title_elements)
            comment_element(driver, element)

            # 使用CSS选择器找到文章标题并打印文章标题
            title_text = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.article-panel .title-panel'))).text
            logger.info(f"当前文章标题：{title_text}")
            utils.url_info(driver)

            # 使用CSS选择器找到一键评论元素
            btn_like = driver.find_element(By.CSS_SELECTOR, '.comment-input-panel .header-panel .btn.like.null')
            # 滚动到元素位置
            driver.execute_script("arguments[0].scrollIntoView(true);", btn_like)
            # 等待一点时间让页面响应
            time.sleep(0.5)
            # 使用JavaScript点击元素
            driver.execute_script("arguments[0].click();", btn_like)

            # 使用CSS选择器找到评论按钮元素
            post_btn = driver.find_element(By.CSS_SELECTOR, '.comment-input-panel .post-operate-panel .post-btn.on')
            # 滚动到元素位置
            driver.execute_script("arguments[0].scrollIntoView(true);", post_btn)
            # 等待一点时间让页面响应
            time.sleep(0.5)
            # 使用JavaScript点击元素
            driver.execute_script("arguments[0].click();", post_btn)
            # 等待一点时间让页面响应
            time.sleep(2)
            logger.info("评论发表成功！")

            # 完成操作后关闭窗口并切回原窗口
            driver.close()  # 关闭当前窗口
            driver.switch_to.window(driver.window_handles[0])  # 切回原窗口
        else:
            logger.error("没有找到文章标题元素。")
    except TimeoutException as e:
        logger.error(f"等待元素超时：{e}")
    except NoSuchElementException as e:
        logger.error(f"未能找到页面上的元素：{e}")
    except Exception as e:
        logger.error(f"发生了错误：{e}")


# 删除文章评论
def comment_delete(driver):
    try:
        # 等待页面完全加载
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))
        utils.url_info(driver)

        # 使用CSS选择器找到用户主页按钮
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.page-container .right-board .userinfo-panel .avatar'))
        )
        comment_element(driver, element)
        logger.info("进入用户主页！")

        # 使用CSS选择器找到评论列表按钮
        comment_list_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn[data-type='btn'][data-name='comment']"))
        )
        # 滚动到元素位置
        driver.execute_script("arguments[0].scrollIntoView(true);", comment_list_btn)
        # 等待一点时间让页面响应
        time.sleep(0.5)
        # 使用JavaScript点击元素
        driver.execute_script("arguments[0].click();", comment_list_btn)

        # 使用CSS选择器找到菜单按钮
        menu_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.page-container .left-board .list-panel-board .list-panel .comment-card-panel .more-menu-panel'))
        )
        # 滚动到元素位置
        driver.execute_script("arguments[0].scrollIntoView(true);", menu_btn)
        # 等待一点时间让页面响应
        time.sleep(0.5)
        # 点击元素, 使用JS好像不行
        menu_btn.click()

        # 等待所有 .btn 类的元素变得可点击
        delete_btns = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR,
                 '.page-container .left-board .list-panel-board .list-panel .comment-card-panel .more-menu-panel .drop-panel .btn'))
        )
        # 滚动到元素位置
        driver.execute_script("arguments[0].scrollIntoView(true);", delete_btns[0])
        # 等待一点时间让页面响应
        time.sleep(0.5)
        # 使用JavaScript点击元素
        driver.execute_script("arguments[0].click();", delete_btns[0])

        utils.find_confirm_btn(driver)
        logger.info("评论删除成功！")
        # 删除后不会跳转，且需要刷新，暂时先关闭，然后切回主页标签
        time.sleep(2)   # 等待一点时间让页面响应
        driver.close()  # 关闭当前窗口
        driver.switch_to.window(driver.window_handles[0])  # 切回原窗口
        utils.url_info(driver)
    except TimeoutException as e:
        logger.error(f"等待元素超时：{e}")
    except NoSuchElementException as e:
        logger.error(f"未能找到页面上的元素：{e}")
    except Exception as e:
        logger.error(f"发生了错误：{e}")


def comment_element(driver, element):
    # 滚动到元素位置
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    # 等待一点时间让页面响应
    time.sleep(0.5)
    # 使用JavaScript点击元素
    driver.execute_script("arguments[0].click();", element)

    # 等待新窗口打开并切换
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[-1])

    # 等待页面完全加载
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))
    utils.url_info(driver)

