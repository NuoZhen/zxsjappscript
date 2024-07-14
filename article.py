"""
文章模块
"""
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# 文章评论
def article_comment(driver):
    # 收集文章标题元素并随机一个点击
    try:
        title_elements = article_titles(driver)
        if title_elements:
            selected_title = random.choice(title_elements)
            # 滚动到元素位置
            driver.execute_script("arguments[0].scrollIntoView(true);", selected_title)
            # 等待一点时间让页面响应
            time.sleep(0.5)
            # 使用JavaScript点击元素
            driver.execute_script("arguments[0].click();", selected_title)

            # 等待新窗口打开并切换
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            window_handles = driver.window_handles
            driver.switch_to.window(window_handles[-1])

            # 等待页面完全加载
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))

            # 使用CSS选择器找到文章标题并打印文章标题
            title_text = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.article-panel .title-panel'))).text
            print(f"当前文章标题：{title_text}")
            print(f"当前页面URL：{driver.current_url}")

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

            # 完成操作后关闭窗口并切回原窗口
            driver.close()  # 关闭当前窗口
            driver.switch_to.window(window_handles[0])  # 切回原窗口
        else:
            print("没有找到文章标题元素。")
    except TimeoutException as e:
        print(f"等待元素超时：{e}")
    except NoSuchElementException as e:
        print(f"未能找到页面上的元素：{e}")
    except Exception as e:
        print(f"发生了错误：{e}")


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
        if driver.find_element(By.ID, 'simple-text-prompt').find_element(By.TAG_NAME, 'p').text == "今日已打卡！":
            print("今日已打卡！")
        else:
            # 等待打卡面板可见
            keep_panel_text = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, '.page-container .left-board .quick-post-panel .keep-panel .title'))
            ).text

            # 使用 CSS 选择器找到 p 元素
            # p_element = driver.find_element(By.XPATH, '//p[@data-we-empty-p]')
            # 查找可输入的 p 元素
            # TODO: 测试下这个能否成功找到 p 元素，记得把点击注释掉
            p_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//p[@data-we-empty-p]'))
            )
            # 滚动到元素位置
            driver.execute_script("arguments[0].scrollIntoView(true);", p_element)
            # 等待一点时间让页面响应
            time.sleep(0.5)
            # 使用 send_keys 方法写入文本
            p_element.send_keys(keep_panel_text)
            # 等待一点时间让页面响应
            time.sleep(1)

            # 等待打卡按钮变为可点击状态
            post_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR,
                     '.page-container .left-board .quick-post-panel .post-operate-panel .post-btn.on'))
            )
            # 使用JavaScript点击元素
            driver.execute_script("arguments[0].click();", post_btn)
            print("动态发表成功！")
            article_delete(driver)
    except TimeoutException as e:
        print(f"等待元素超时：{e}")
    except NoSuchElementException as e:
        print(f"未能找到页面上的元素：{e}")
    except Exception as e:
        print(f"发生了错误：{e}")


def article_delete(driver):
    try:
        # 等待页面完全加载
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))
        print(f"当前页面URL：{driver.current_url}")

        # 使用CSS选择器找到菜单按钮
        menu_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.page-container .left-board .article-panel .nav-panel .more-menu-panel'))
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
                 '.page-container .left-board .article-panel .nav-panel .more-menu-panel .drop-panel .btn'))
        )
        # 滚动到元素位置
        driver.execute_script("arguments[0].scrollIntoView(true);", delete_btns[1])
        # 等待一点时间让页面响应
        time.sleep(0.5)
        # 使用JavaScript点击元素
        driver.execute_script("arguments[0].click();", delete_btns[1])

        time.sleep(1)
        # 使用CSS选择器找到确认按钮
        confirm_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 '.u-popup .popup-normal.confirm-popup .btn-box .confirm'))
        )
        # 滚动到元素位置
        driver.execute_script("arguments[0].scrollIntoView(true);", confirm_btn)
        # 等待一点时间让页面响应
        time.sleep(0.5)
        # 使用JavaScript点击元素
        driver.execute_script("arguments[0].click();", confirm_btn)
        print("文章删除成功！")
        # 删除后会跳转, 测试时为首页
    except TimeoutException as e:
        print(f"等待元素超时：{e}")
    except NoSuchElementException as e:
        print(f"未能找到页面上的元素：{e}")
    except Exception as e:
        print(f"发生了错误：{e}")


# 使用CSS选择器找到文章标题元素
def article_titles(driver):
    """ 返回页面上所有文章标题的元素列表 """
    return driver.find_elements(By.CSS_SELECTOR, '.post-card-panel .post-title')

