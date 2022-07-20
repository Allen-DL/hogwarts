#!/usr/bin/env python
# -*- coding: utf-8 -*_
# Auhter: donglei
# File: test_demo.py
# CreateTime: 2022-07-20 22:28
import pytest
import yaml


# @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yaml")))
# class TestDemo:
#     def test_demo(self, env):
#         if "test" in env:
#             print(f"测试环境的ip是{env['test']}")
#             print("this is test env")
#         elif "dev" in env:
#             print(f"开发环境的ip是:{env['dev']}")
#             print(" this is dev env")
#         else:
#             print("nothing")

def test_yaml():
    print(yaml.safe_load(open("./env.yaml")))


# if __name__ == '__main__':
#     test_yaml()
