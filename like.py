"""
点赞模块
"""
import logging
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# 点赞+取消
def like_and_cancel(driver):
    # 等待所有点赞按钮和标题加载完毕
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '.post-card-panel .classify-operate-panel .operate-panel .btn.like'))
    )
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, '.post-card-panel .post-title'))
    )

    # 滚动到底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # 等待新帖子加载

    # 一次性收集所有点赞按钮
    css_like_buttons = '.post-card-panel .classify-operate-panel .operate-panel .btn.like'
    like_buttons = driver.find_elements(By.CSS_SELECTOR, css_like_buttons)

    # 一次性收集所有文章标题
    css_titles = '.post-card-panel .post-title'
    titles = driver.find_elements(By.CSS_SELECTOR, css_titles)

    # 遍历并处理所有点赞按钮
    for index in range(min(len(like_buttons), len(titles))):
        try:
            # 点赞
            safe_toggle_like(driver, like_buttons[index])
            # 输出文章标题
            logger.info(f"点赞文章：{titles[index].text}")
        except StaleElementReferenceException:
            logger.error("元素已过期，尝试重新查找元素。")
            # 重新获取点赞按钮
            like_buttons = driver.find_elements(By.CSS_SELECTOR, css_like_buttons)
            # 重新获取文章标题
            titles = driver.find_elements(By.CSS_SELECTOR, css_titles)
            if index < len(like_buttons) and index < len(titles):
                safe_toggle_like(driver, like_buttons[index])
                logger.info(f"点赞文章：{titles[index].text}")
            else:
                logger.error("点赞按钮和文章标题数量不匹配，跳过剩余操作。")
                break
        except IndexError:
            logger.error("点赞按钮和文章标题数量不匹配，跳过剩余操作。")
            break

    time.sleep(2)  # 等待按钮加载

    # 收集所有已点赞按钮
    css_liked_buttons = '.post-card-panel .classify-operate-panel .operate-panel .btn.like.on'
    liked_buttons = driver.find_elements(By.CSS_SELECTOR, css_liked_buttons)

    # 遍历并处理所有已点赞按钮
    for index in range(min(len(liked_buttons), len(titles))):
        try:
            # 取消点赞
            safe_toggle_like(driver, liked_buttons[index])
            # 输出文章标题
            logger.info(f"取消点赞文章：{titles[index].text}")
        except StaleElementReferenceException:
            logger.error("元素已过期，尝试重新查找元素。")
            # 重新获取已点赞按钮
            liked_buttons = driver.find_elements(By.CSS_SELECTOR, css_liked_buttons)
            # 重新获取文章标题
            titles = driver.find_elements(By.CSS_SELECTOR, css_titles)
            if index < len(liked_buttons) and index < len(titles):
                safe_toggle_like(driver, liked_buttons[index])
                logger.info(f"取消点赞文章：{titles[index].text}")
            else:
                logger.error("点赞按钮和文章标题数量不匹配，跳过剩余操作。")
                break
        except IndexError:
            logger.error("点赞按钮和文章标题数量不匹配，跳过剩余操作。")
            break


def safe_toggle_like(driver, element):
    try:
        # 滚动到元素位置
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        # 等待一点时间让页面响应
        time.sleep(0.5)
        # 使用JavaScript点击元素
        driver.execute_script("arguments[0].click();", element)
        # 避免触发速率限制
        time.sleep(random.randint(1, 2))
    except Exception as e:
        logger.error(f"点赞操作时发生错误: {e}")

