'''
    Created by dl on 2022/8/3
    PROJECT_NAME：hogwarts 
'''
'''
Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作) 
Critical级别：临界缺陷（功能点缺失） 
Normal级别：普通缺陷（数值计算错误） 
Minor级别：次要缺陷（界面错误与U需求不符) 
Trivial级别：轻微缺陷（必输项无提示，或者提示不规范)
'''

import allure
import pytest

def test_with_no_servenrity_lable():
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_Trivial_servenrity():
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_Normal_servenrity():
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalServenrity():

    def test_inside_the_normal_servenrity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_servenrity_test_class_with_overriding_critical_servenrity(self):
        pass


if __name__ == '__main__':
    pytest.main()


