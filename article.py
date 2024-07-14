"""
文章模块
"""
from selenium.webdriver.common.by import By


def article():
    print(1)


# 使用CSS选择器找到文章标题元素
def article_title(driver):
    title_elements = driver.find_elements(By.CSS_SELECTOR, '.post-card-panel .post-title')
    return title_elements
