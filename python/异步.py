# -*- coding: gbk -*-
import time
import asyncio

def task1():
    print("任务1开始")
    time.sleep(2)  # 模拟 I/O 操作（例如网络请求）
    print("任务1结束")

def task2():
    print("任务2开始")
    time.sleep(1)
    print("任务2结束")



async def asy_task1():
    print("任务1开始")
    await asyncio.sleep(2)  # 模拟 I/O 操作（如网络请求）
    print("任务1结束")

async def asy_task2():
    print("任务2开始")
    await asyncio.sleep(1)
    print("任务2结束")

task1()
task2()

# 使用事件循环运行异步任务
async def main():
    await asyncio.gather(asy_task1(), asy_task2())

# 执行异步任务
asyncio.run(main())



