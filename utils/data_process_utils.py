from utils import regular_utils, concatenate_utils
import asyncio
import queue
from sydney import SydneyClient
import time
from datetime import datetime

# 将 分割后的文件数据 清除答案部分
def process_answer(process_dict):
    keys_list = list(process_dict.keys())
    new_dict = {key: None for key in keys_list}
    for (k, v) in process_dict.items():
        for value in v:
            new_dict[k] = regular_utils.get_every_question_noans(value)
    return new_dict

# 将 分割后且清除答案的文件数据 嵌入选择题拼接模版中
def insert_select_question_prompt(process_dict):
    new_dict = {}  
    for key, value in process_dict.items():
        new_value = [concatenate_utils.select_question_prompt(v) for v in value ]
        new_dict[key] = new_value 
    return new_dict    

# 向 New Bing 发送请求，接受数据
async def ask_question_copilot(prompt: str, conversation_style: str) -> dict:
    start_time = time.time()
    start_formatted_time = datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S")
    send_message = "Prompt request sending time"
    print(f"{start_formatted_time} - {send_message}")
    async with SydneyClient() as sydney:
        await sydney.reset_conversation(style=conversation_style)
        response = await sydney.ask(prompt)
        end_time = time.time()
        end_formatted_time = datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")
        spend_time = end_time - start_time
        data_dict = {
            "send_start_time" : start_formatted_time,
            "accept_over_time" : end_formatted_time,
            "spend_time": spend_time,
            "response": response
        }
        receive_message = "Data reception completion time"
        print(f"{end_formatted_time} - {receive_message}")
        spend_time_message = "Time spent on data requests"
        print(f"{spend_time_message}:  {spend_time}s")
        return data_dict

# 将 字典中value 数据（list） 转化成队列（queue）
def list_transform_queue(data_dict: dict) -> dict:
    new_dict = {}
    for key, value in data_dict.items():
        q = queue.Queue()
        for item in value:
            q.put(item)
        new_dict[key] = q
    return new_dict