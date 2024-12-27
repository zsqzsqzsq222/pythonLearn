# -*- coding: gbk -*-
import time
import asyncio

def task1():
    print("����1��ʼ")
    time.sleep(2)  # ģ�� I/O ������������������
    print("����1����")

def task2():
    print("����2��ʼ")
    time.sleep(1)
    print("����2����")



async def asy_task1():
    print("����1��ʼ")
    await asyncio.sleep(2)  # ģ�� I/O ����������������
    print("����1����")

async def asy_task2():
    print("����2��ʼ")
    await asyncio.sleep(1)
    print("����2����")

task1()
task2()

# ʹ���¼�ѭ�������첽����
async def main():
    await asyncio.gather(asy_task1(), asy_task2())

# ִ���첽����
asyncio.run(main())



