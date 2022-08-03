'''
    Created by dl on 2022/8/3
    PROJECT_NAME：hogwarts 
'''
import pytest
import allure

@allure.feature('登录模块')
class TestLogin:
    @allure.story('登录成功')
    def test_login_success(self):
        print("这是登录： 测试用例，登录成功")
        pass

    @allure.story('登录失败')
    def test_login_fail(self):
        print("这是登录： 测试用例，登录失败")
        pass

    @allure.story('用户名缺失')
    def test_login_missuseradmin(self):
        print("用户名缺失")

    @allure.story('密码错误')
    def test_login_failure(self):
        with allure.step('点击用户名'):
            print("请输入用户名")
        with allure.step('点击'):
            print("请输入密码")
        print("点击登录")
        with allure.step('点击登录后登录失败'):
            assert '1' == 1
            print('密码错误')

    @allure.story("登录失败1")
    def test_login_failure_a(self):
        print("这是登录： 测试用例  登录失败")
        pass

if __name__ == '__main__':
    pytest.main()