import asyncio
from sydney import SydneyClient

async def main() -> None:
    async with SydneyClient() as sydney:
        while True:
            prompt = input("You: ")

            if prompt == "!reset":
                await sydney.reset_conversation()
                continue
            elif prompt == "!exit":
                break

            response = await sydney.ask(prompt)  # 假设这是获取完整响应的方法
            print(f"Sydney: {response}\n")

if __name__ == "__main__":
    asyncio.run(main())
