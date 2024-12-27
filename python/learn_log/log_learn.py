import logging

# 配置日志记录器
logging.basicConfig(filename='app.log',  # 日志输出文件
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(filename)s - %(lineno)d - %(levelname)s - %(message)s')
# 示例日志
logging.debug("这是一个调试信息")
logging.info("这是一个信息")
logging.warning("这是一个警告")
logging.error("这是一个错误")
logging.critical("这是一个严重错误")



