"""
文章模块
"""
import logging
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import utils

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def article_post(driver):
    # 找到打卡按钮
    try:
        # 使用CSS选择器找到打卡按钮
        btn_keep = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        '.page-container .left-board .quick-post-panel .post-operate-panel .operate-panel .btn.keep'))
        )
        # 滚动到元素位置
        driver.execute_script("arguments[0].scrollIntoView(true);", btn_keep)
        # 等待一点时间让页面响应
        time.sleep(0.5)
        # 使用JavaScript点击元素
        driver.execute_script("arguments[0].click();", btn_keep)

        # 判断今日是否已打卡
        # 使用ID找到 <div> 进行操作，获取内部的文本
        try:
            test_prompt = driver.find_element(By.ID, 'simple-text-prompt').find_element(By.TAG_NAME, 'p')
            if test_prompt.text == "今日已打卡！":
                logger.info("今日已打卡！")
        except Exception:
            # 等待打卡面板可见
            keep_panel_text = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, '.page-container .left-board .quick-post-panel .keep-panel .title'))
            ).text
            # 查找可输入的 p 元素
            p_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//p[@data-we-empty-p]'))
            )
            # 滚动到元素位置
            driver.execute_script("arguments[0].scrollIntoView(true);", p_element)
            # 等待一点时间让页面响应
            time.sleep(0.5)
            # 删除 <br> 标签
            driver.execute_script("""
                var p = arguments[0];
                p.innerHTML = p.innerHTML.replace(/<br>/g, '');
            """, p_element)
            # 插入文本
            driver.execute_script("""
                var p = arguments[0];
                var text = arguments[1];
                p.innerHTML = text + p.innerHTML;
            """, p_element, keep_panel_text)

            # 等待打卡按钮变为可点击状态
            post_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR,
                     '.page-container .left-board .quick-post-panel .post-operate-panel .post-btn.on'))
            )
            # 使用JavaScript点击元素
            driver.execute_script("arguments[0].click();", post_btn)
            logger.info("动态发表成功！")
            article_delete(driver)
    except TimeoutException as e:
        logger.error(f"等待元素超时：{e}")
    except NoSuchElementException as e:
        logger.error(f"未能找到页面上的元素：{e}")
    except Exception as e:
        logger.error(f"发生了错误：{e}")


def article_delete(driver):
    try:
        # 等待页面完全加载
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))
        logger.info(f"当前页面URL：{driver.current_url}")

        # 将页面滚动到顶部
        driver.execute_script("window.scrollTo(0, 0);")
        # 使用CSS选择器找到菜单按钮
        menu_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.page-container .left-board .article-panel .nav-panel .more-menu-panel'))
        )
        # 等待一点时间让页面响应
        time.sleep(0.5)
        # 点击元素, 使用JS好像不行
        menu_btn.click()

        # 等待所有 .btn 类的元素变得可点击
        delete_btns = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR,
                 '.page-container .left-board .article-panel .nav-panel .more-menu-panel .drop-panel .btn'))
        )
        # 滚动到元素位置
        driver.execute_script("arguments[0].scrollIntoView(true);", delete_btns[1])
        # 等待一点时间让页面响应
        time.sleep(0.5)
        # 使用JavaScript点击元素
        driver.execute_script("arguments[0].click();", delete_btns[1])

        utils.find_confirm_btn(driver)
        logger.info("文章删除成功！")
        # 删除后会跳转, 测试时为首页
    except TimeoutException as e:
        logger.error(f"等待元素超时：{e}")
    except NoSuchElementException as e:
        logger.error(f"未能找到页面上的元素：{e}")
    except Exception as e:
        logger.error(f"发生了错误：{e}")


# 使用CSS选择器找到文章标题元素
def article_titles(driver):
    """ 返回页面上所有文章标题的元素列表 """
    return driver.find_elements(By.CSS_SELECTOR, '.post-card-panel .post-title')

