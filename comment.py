"""
评论模块
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException, NoSuchElementException


def comment_delete(driver):
    try:
        # 等待页面完全加载
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))
        print(f"当前页面URL：{driver.current_url}")

        # 使用CSS选择器找到用户主页按钮
        user_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.page-container .right-board .userinfo-panel .avatar'))
        )
        # 滚动到元素位置
        driver.execute_script("arguments[0].scrollIntoView(true);", user_btn)
        # 等待一点时间让页面响应
        time.sleep(0.5)
        # 使用JavaScript点击元素
        driver.execute_script("arguments[0].click();", user_btn)

        # 等待新窗口打开并切换
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])

        # 等待页面完全加载
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))
        print("进入用户主页！")

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
        # 删除后不会跳转，且需要刷新
    except TimeoutException as e:
        print(f"等待元素超时：{e}")
    except NoSuchElementException as e:
        print(f"未能找到页面上的元素：{e}")
    except Exception as e:
        print(f"发生了错误：{e}")
