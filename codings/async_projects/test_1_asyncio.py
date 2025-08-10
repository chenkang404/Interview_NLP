import asyncio
import aiohttp
from bs4 import BeautifulSoup  # 需要安装：pip install beautifulsoup4
import time
import random

# 要爬取的URL列表
URLS = [
    "https://www.python.org  ",
    "https://www.github.com  ",
    "https://www.stackoverflow.com  ",
    "https://www.reddit.com  ",
    "https://www.wikipedia.org  ",
    "https://www.mozilla.org  ",
    "https://www.tensorflow.org  ",
    "https://www.pytorch.org  "
]

# 模拟不同的用户代理，避免被简单反爬
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
]

async def fetch(session, url):
    """异步获取网页内容并解析标题"""
    try:
        # 设置随机请求头，模拟不同浏览器
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5"
        }
        
        # 随机延迟，避免请求过于频繁
        await asyncio.sleep(random.uniform(0.5, 1.5))
        
        # 发送异步请求
        async with session.get(url, headers=headers, timeout=10) as response:
            print(f"爬取 {url} - 状态码: {response.status}")
            
            # 解析HTML获取标题
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                title = soup.title.string.strip() if soup.title else "无标题"
                return {"url": url, "title": title, "status": response.status}
            else:
                return {"url": url, "title": f"获取失败，状态码: {response.status}", "status": response.status}
                
    except Exception as e:
        return {"url": url, "title": f"爬取出错: {str(e)}", "status": -1}

async def main():
    """主函数，协调所有爬取任务"""
    start_time = time.time()
    
    # 创建异步会话
    async with aiohttp.ClientSession() as session:
        # 创建所有爬取任务
        tasks = [fetch(session, url) for url in URLS]
        
        # 并发执行所有任务并等待结果
        results = await asyncio.gather(*tasks)
        
        # 打印结果
        print("\n" + "="*50)
        print("爬取结果:")
        print("="*50)
        for result in results:
            print(f"URL: {result['url']}")
            print(f"标题: {result['title']}")
            print("-"*50)
    
    end_time = time.time()
    print(f"\n总耗时: {end_time - start_time:.2f} 秒")
    print(f"爬取数量: {len(URLS)} 个")

if __name__ == "__main__":
    # 运行异步主函数
    asyncio.run(main())
    