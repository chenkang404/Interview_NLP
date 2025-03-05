import sys
import os
sys.path.append("../")

from configs.config import prompt,prompt_v2

def fun(value):
    print(value)


if __name__ == "__main__":
    fun(prompt)