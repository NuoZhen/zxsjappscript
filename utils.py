"""
工具模块
"""

import json
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# 字符串转字典
def parse_cookie_string(cookie_str):
    output = []
    # 使用分号和空格分割字符串，然后遍历每一项
    for item in cookie_str.split("; "):
        # 使用等号分割每一对键值
        parts = item.split('=', 1)
        # 确保我们有至少一个键值对
        if len(parts) != 2:
            continue
        name, value = parts
        # 根据值确定domain
        if value in ['Hm_lpvt_132102418c9639c7122592f507661f29',
                     'Hm_lvt_132102418c9639c7122592f507661f29',
                     'HMACCOUNT']:
            domain = '.zxsj.wanmei.com'
        else:
            domain = '.wanmei.com'
        # 构建cookie字典，并将字典添加到output列表
        output.append({
            'domain': domain,
            'name': name,
            'path': '/',
            'value': value,
        })
    # 将字典转换为JSON格式的字符串并返回
    return json.loads(json.dumps(output))


def url_info(driver):
    # 请求一系列关于浏览器的信息, 包括窗口句柄、浏览器尺寸/位置、cookie、警报等
    logger.info(f"当前页面标题：{driver.title}")
    logger.info(f"当前页面URL：{driver.current_url}")
