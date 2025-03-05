import sys
import os

#这种方式是结合__init__.py将tools,configs视做包，在tools.py中动态添加父目录到sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
print("current_dir:",current_dir)
# 父目录是当前目录的上两级？
parent_dir = os.path.dirname(current_dir)
print("parent_dir:",parent_dir)
# 将父目录添加到sys.path
sys.path.append(parent_dir)


from configs.config import prompt,prompt_v2

def fun(value):
    print(value)


if __name__ == "__main__":
    fun(prompt)