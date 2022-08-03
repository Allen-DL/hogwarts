'''
    Created by dl on 2022/8/3
    PROJECT_NAME：hogwarts 
'''
import allure

@allure.link("http://www.baidu.com", name="BUG")
def test_with_link():
    print("这是一条添加了链接的测试用例")


TEST_CASE_LINK = 'https://navinfo.feishu.cn/wiki/wikcnV4WvOZaB1aX6J1DN5TijNc#'
@allure.testcase(TEST_CASE_LINK, '登录用例')
def test_with_testcase():
    print("这是一条测试用例的链接，链接到测试用例里面")


# 执行命令时加入参数  --allure-link-pattern=issue:http://10.60.145.248/zentao/bug-view-{}.html
@allure.issue('11053', "这是一个issue")
def test_with_issue():
    print("这是一个链接")