
'''
调用logging.getLogger()函数创建Logger对象，出现日志打印重复，原因是往Logger中加载了多个handler，解决方法：
1）在添加handler对象前先判断有没有handler，如果没有才添加
2）在每次用完handler对象后就把它删除；


'''

import logging,time

class log:
    def Log_Maker(level,msg):
        #创建Logger对象
        logger_obj=logging.getLogger("crm_logger")
        #logger_obj=logging.Logger("crm_logger")
        logger_obj.setLevel(logging.DEBUG)

        #创建FileHandler对象  localhost.2019-11-08.log
        filehandler_obj=logging.FileHandler("crm.%s.log"%time.strftime("%Y-%m-%d", time.localtime()))

        #创建Formatter对象
        formatter_obj=logging.Formatter(fmt="%(asctime)s %(filename)s %(funcName)s %(levelname)s %(lineno)d %(module)s  %(name)s  %(pathname)s %(message)s")

        #将Formatter对象加载到filehandler对象中
        filehandler_obj.setFormatter(formatter_obj)

        #将filehandler对象加载到Logger对象中
        logger_obj.addHandler(filehandler_obj)

        #输出日志
        if level=="DEBUG":
            logger_obj.debug(msg)
        if level=="INFO":
            logger_obj.info(msg)
        if level=="WARNING":
            logger_obj.warning(msg)
        if level=="ERROR":
            logger_obj.error(msg)
        if level=="CRITICAL":
            logger_obj.critical(msg)

        logger_obj.removeHandler(filehandler_obj)

