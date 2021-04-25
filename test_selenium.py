from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# 创建Chrome浏览器对象，并在电脑上打开一个浏览器窗口
browser = webdriver.Chrome(executable_path='H:\pyproject\chromedriver\chromedriver.exe')
# 通过浏览器向服务器发送URL请求
browser.get("https://www.baidu.com/")

"""
# sleep(3)
# 刷新浏览器
# browser.refresh()
# 设置浏览器的大小
#　browser.set_window_size(1400,800)
# 设置链接内容
# element = browser.find_element_by_link_text("新闻")
#　element.click()
"""

"""
browser.set_window_size(1920,1080)
sleep(3)
#　定位到要悬停的元素：设置
element = browser.find_element_by_id("s-usersetting-top")
# 对定位到的元素执行鼠标悬停操作
ActionChains(browser).move_to_element(element).perform()
# 找到链接
elem1 = browser.find_element_by_link_text("搜索设置")
elem1.click()
"""

"""
print('before search==========')
# 打印当前页面title
title = browser.title
print(title)
# 打印当前页面URL
now_url = browser.current_url
print(now_url)
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
sleep(1)
print('after search=========')
# 再次打印当前页面title
title = browser.title
print(title)
# 再次打印当前页面的URL
now_url = browser.current_url
print(now_url)
#获取结果数目
numss = browser.find_element_by_class_name('nums').text
print(numss)
"""

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
sleep(1)

# 定位一组元素
elements = browser.find_elements_by_xpath('//div/h3/a')
print(type(elements))
# 循环遍历出每一条搜索结果的标题
for t in elements:
    print(t.text)
    element = browser.find_element_by_link_text(t.text)
    element.click()
    sleep(3)

browser.quit()


