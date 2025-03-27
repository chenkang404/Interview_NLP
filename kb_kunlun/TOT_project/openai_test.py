from openai import OpenAI

# 初始化 OpenAI 客户端
client = OpenAI(
    api_key="token-vulcan",  # 输入你的 API Key
    base_url="http://219.147.99.170:50020/v1"
)

# 初始化消息列表，包含初始用户消息
messages = []
print('clean:清理记录\texit:退出')

while True:
    # 获取用户输入
    user_input = input("你: ")
    
    if user_input == 'clean':
        messages.clear()
        continue
    
    if user_input == 'exit':
        break
    
    # 添加用户输入到消息列表
    messages.append({"role": "user", "content": user_input})

    # 调用 API 获取响应
    completion = client.chat.completions.create(
        model="Qwen2-5-7B",
        messages=messages,
        logprobs=False,
        stream=True  # 开启流式输出
    )

    # 流式输出获取结果
    assistant_response = ""  # 存储助手的完整回复
    print('助手: ', end='', flush=True)
    for chunk in completion:
        # 在每个块中获取内容并输出
        content = chunk.choices[0].delta.content
        if content:
            print(content, end='', flush=True)
            assistant_response += content  # 将内容添加到助手的回复中
    
    print('')  # 输出换行

    # 将助手的完整回复添加到消息列表
    messages.append({"role": "assistant", "content": assistant_response})
