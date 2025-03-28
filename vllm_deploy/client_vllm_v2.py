import time
import concurrent.futures
import requests
import torch
from openai import OpenAI
import numpy as np

client = OpenAI(
    api_key="token-vulcan",  
    base_url="http://0.0.0.0:5115/v1"
)

query_input = "你是一个数据提取专家。帮助我提取出关键信息。严格禁止输出重复内容！## =========== Task =========== ##\n你现在的任务是从OCR文字识别的结果中提取我指定的关键信息。OCR的文字识别结果使用```符号包围，包含所识别出来的文字，\n顺序在原始图片中从左至右、从上至下。我指定的关键信息使用[]符号包围。请注意OCR的文字识别结果可能存在长句子换行被切断、不合理的分词、\n对应错位等问题，你需要结合上下文语义进行综合判断，以抽取准确的关键信息。\n在返回结果时使用Markdown的表格格式，包含多组数据，每组数据为一行，表头为我指定的关键信息，表格内容为所抽取的结果。\n如果认为OCR识别结果中没有关键信息或未提及关键信息，则将表格内容赋值为“”。 请只输出表格格式的结果，不要包含其它多余文字！下面正式开始：\nOCR文字：```\t 医疗机构哈尔滨医科大学附属第二医院\n\t\t\t\t\t\t\t （组织机构代码2\n\n   医疗付费方式全自费\n\t\t\t\t  住院病案首页\n\t\t\t\t\t\t次住院\t  病案号：0002537832\n\t\t\t\t\t\t\t\t  病案号：0002537832\n   健康卡号\t\t\t  第1次住院\t  病案号：0002537832\n   姓名徐春艳  性别21.男2.女 出生日期1971年2月20日年龄51岁国籍中国\n   （年龄不足1周岁的）年龄  月  新生儿出生体重二克  新生儿入院体重二克\n   出生地黑龙江省牡丹江市\t\t籍贯黑龙江省牡丹江市\t 民族汉族\n   身份证号231026197102203247   职业其他   婚姻21.未婚2.已婚3.丧偶4离婚9.其他\n   现住址黑龙江省哈尔滨市南岗区\t\t\t 电话15845332567邮编150000\n   户口地址黑龙江省哈尔滨市南岗区\t\t\t\t   邮编150000\n   工作单位及地址\t\t\t\t单位电话一\t 邮编一\n   联系人姓名\t关系其他  地址二\t\t\t 电话15845332567\n   入院途径21.急诊2.门诊3.其他医疗机构转入9.其他\n   入院时间2022年8月14日8时入院科别妇产科四病房 病房11009转科科别一\n   出院时间2022年8月16日9时出院科别妇产科四病房 病房11009实际住院2 天\n   门（急）诊诊断子宫内膜息肉\t\t\t\t  疾病编码N84.001\n\t\t出院诊断\t 疾病编码一院\t 出院诊断\t 疾病编码\n   门（急）诊诊断子宫内膜息肉\n   门（急）诊诊断子宫内膜息肉\t\t\t\t  疾病编码N84.001\n\t\t出院诊断\t 疾病编码金器   一院\t 出院诊断\t 疾病编码俞籍\n   主要诊断子宫内膜息肉\t  184.001 1其他诊断\n   其他诊断宫颈息肉\t\t84.100 1\n\t  子宫粘膜下平滑肌瘤\tD25.000x001\n\t  宫颈囊肿\t\tN88.803 1\n\t  宫颈炎性疾病\t  N72.x00 1\n\t  乳腺术后\t\tZ98.800x611\n\t  肺术后\t\tZ98.800x001\n   入院病情：1.有,2.临床未确定3.情况不明4.无\n   入院病情：1.有,2.临床未确定3.情况不明4.无\n\t\t\t\t\t\t\t\t 疾病编码\n\t\t\t\t\t\t\t\t 疾病编码\n\t\t\t\t\t\t\t\t 病理号\n   损伤、中毒的外部原因\n   病理诊断\t\t\t\t\t\t  疾病编码\n   诊断符合情况临床与病理一 (0.未做1符合2.不符合3.不确定）  病理号\n   药物过敏11.无2.有 过敏药物：一\t\t\t 死亡患者尸检 1.是2.否\n   血型11.A2.B3.04.AB5.不详6.未查Rh21.阴2.阳3.不详4.未查抢救0次成功0次\n   科主任乳家鑫主任（副主任）医师邱晓红主治医师陈秀惠 住院医师高住普\n   责任护士王迪\t 进修医师一\t实习医师\t 编码员\n   病案质量11.甲2.乙3.丙质控医师邱晓红  质控护士齐票  质控日期2022年8月16日\n\t\t\t\t\t\t\t\t   医疗等情编号```\n要抽取的关键信息：[诊断类型,疾病名称,疾病编码]。\n\n\n## =========== Rules =========== ##\n不要进行总结归纳，只提取原始内容\\\\n诊断类型有主要诊断、其他诊断等\\\n\n\n## =========== Few-shot =========== ##\n例如:OCR文字：序 中文名称  英文名称结果 1 外观 CLA 透明 2 颜色 COL 黄色，要抽取的关键信息：[序号,中文名称,英文名称]，结果：|序号|中文名|英文名称|\\n|-|-|-|\\n|1|外观|CLA|\\n|2|颜色|COL|\\\n\n"

messages = [{"role": "user", "content": query_input}]

NUM_REQUESTS = 50  # 并发请求数
CONCURRENT_THREADS = 10  # 并发线程数
results = []
latencies = []
error_count = 0

def send_request(index):
    global error_count
    start_time = time.time()
    try:
        completion = client.chat.completions.create(
            model="Qwen2-5-32B",
            messages=messages,
            logprobs=False
        )
        response_time = time.time() - start_time
        latencies.append(response_time)
        response_text = completion.choices[0].message.content
        return f"Request {index}:\n{response_text}\n{'='*50}\n"
    except requests.exceptions.RequestException as e:
        error_count += 1
        return f"Request {index}: ERROR\n{'='*50}\n"

if __name__ == "__main__":
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENT_THREADS) as executor:
        futures = {executor.submit(send_request, i): i for i in range(NUM_REQUESTS)}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                results.append(result)

    end_time = time.time()
    
    # 计算指标
    total_time = end_time - start_time
    throughput = NUM_REQUESTS / total_time
    latencies_np = np.array(latencies)
    latency_p50 = np.percentile(latencies_np, 50)
    latency_p90 = np.percentile(latencies_np, 90)
    latency_p99 = np.percentile(latencies_np, 99)
    error_rate = error_count / NUM_REQUESTS

    # GPU 资源占用
    gpu_memory_allocated = torch.cuda.memory_allocated() / (1024 ** 3)  # GB
    gpu_memory_reserved = torch.cuda.memory_reserved() / (1024 ** 3)  # GB
    gpu_utilization = torch.cuda.utilization(0) if torch.cuda.is_available() else "N/A"

    # 保存结果到文件
    with open("results.txt", "w", encoding="utf-8") as f:
        f.write("=== 压测结果 ===\n")
        f.write(f"Total Requests: {NUM_REQUESTS}\n")
        f.write(f"Total Time: {total_time:.2f}s\n")
        f.write(f"Throughput (TPS): {throughput:.2f}\n")
        f.write(f"Latency P50: {latency_p50:.3f}s\n")
        f.write(f"Latency P90: {latency_p90:.3f}s\n")
        f.write(f"Latency P99: {latency_p99:.3f}s\n")
        f.write(f"Error Rate: {error_rate:.2%}\n")
        f.write(f"GPU Memory Allocated: {gpu_memory_allocated:.2f} GB\n")
        f.write(f"GPU Memory Reserved: {gpu_memory_reserved:.2f} GB\n")
        f.write(f"GPU Utilization: {gpu_utilization}%\n\n")
        
        f.write("=== 模型返回内容 ===\n")
        f.writelines(results)

    print("压测完成，结果已保存到 results.txt")
