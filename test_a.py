'''
    Created by dl on 2022/7/20
    PROJECT_NAME：hogwarts 
'''
import pytest
import yaml


def func(x):
    return x + 1


# @pytest.mark.parametrize('a,b', [
#     (1, 2),
#     (10, 20),
#     ('a', 'a1')
#                                  ])

@pytest.mark.parametrize('a,b', yaml.safe_load(open('./data.yaml')))
def test_answer(a, b):
    assert func(a) == b


def test_answer1():
    assert func(4) == 5


@pytest.fixture()
def login():
    print("登录操作")
    username = "donglei"
    return username


# test_a1需要登录 test_b1 不需要登录  test_c 需要登录
class TestDemo():
    def test_a1(self, login):
        print(f'a username = {login}')
        print("a1")

    def test_b1(self):
        print("b1")

    def test_c(self, login):
        print(f'c username = {login}')
        print("c")


if __name__ == '__main__':
    pytest.main(['test_a.py::TestDemo', '-v'])
