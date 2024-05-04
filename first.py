import asyncio

from sydney import SydneyClient

async def main() -> None:
    # 创建一个 Sydney Client 并初始化与 Copilot 的连接，从而开始对话
    async with SydneyClient(style="creative") as sydney:
        prompt = """下列题目的答案是什么？其他的答案为什么错？
1.在产品需求梳理阶段，为确保充分理解用户需求，以下哪项是最有效的方法？

A. 发送电子邮件给用户，详细询问他们的需求。

B. 召开会议，与跨部门团队一起讨论用户需求。

C. 阅读竞品分析报告，以获取市场趋势。

D. 编写用户故事，详细描述用户使用场景。
        """
        print("Sydney: ", end="", flush=True)
        async for response in sydney.ask_stream(prompt):
                print(response, end="", flush=True)
        print("\n")
        # 初始化一个空字符串用于收集响应
        
        # full_response = ""
        # async for response in sydney.ask_stream(prompt):
        #     # 将每个响应追加到字符串中
        #     full_response += response
        # # 所有响应接收完毕后打印
        # print("Sydney: ", end="")
        # print(full_response)






if __name__ == "__main__":
    asyncio.run(main())