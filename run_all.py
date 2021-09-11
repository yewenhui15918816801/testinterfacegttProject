import unittest
import os
from common.send_email import send_email
import time
from BeautifulReport import BeautifulReport

# from common.logger import get_log


# 用例路径
case_path = os.path.join(os.getcwd(), "testcase")


# logger = get_log('run_all')


# 获取最新的测试报告
def get_report():
    report_dir = 'D:\\testinterfaceProject\\report\\'
    # os.listdir(path)方法返回该path路径下的所有文件以及文件夹
    lists = os.listdir(report_dir)
    lists.sort(key=lambda filename: os.path.getmtime(report_dir + filename))
    file_new = os.path.join(report_dir, lists[-1])
    return file_new


# 对比今天定期删除前一天的测试报告
def del_report():
    report_dir = 'D:\\testinterfaceProject\\report\\'
    lists = os.listdir(report_dir)
    for i in lists:
        data = i[0:14]
        now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        if int(now) - int(data) > 235959:
            file = report_dir + data + '_reports.html'
            print("删除昨天的自动化测试报告文件%s" % file)
            os.remove(file)
        else:
            pass


if __name__ == "__main__":
    del_report()
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="test*.py",
                                                   top_level_dir=None)

    # time.time()获取当前时间的时间戳

    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    BeautifulReport(discover).report(description='选品自动化测试接口', filename=now + '_reports', log_path="report")
    new_report = get_report()
    send_email().send(new_report)
