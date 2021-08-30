import unittest
import os
from common.send_email import send_email
import time
from BeautifulReport import BeautifulReport

# 用例路径
case_path = os.path.join(os.getcwd(), "testcase")


# 报告存放路径
def get_report():
    report_dir = 'D:\\testinterfaceProject\\report\\'
    # os.listdir(path)方法返回该path路径下的所有文件以及文件夹
    lists = os.listdir(report_dir)
    lists.sort(key=lambda filename: os.path.getmtime(report_dir + filename))
    file_new = os.path.join(report_dir, lists[-1])
    return file_new


if __name__ == "__main__":
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="test*.py",
                                                   top_level_dir=None)

    report_path = os.getcwd() + '/report'
    now = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))

    BeautifulReport(discover).report(filename=now + 'reports', description='选品自动化测试接口', report_dir=report_path)
    new_report = get_report()
    send_email().send(new_report)
