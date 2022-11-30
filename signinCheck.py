# -*- coding:utf-8 -*-
import csv
import os
import logging


def importStuNum():
    """
    importStuNum 获取学生学号与姓名
    :return: 二位列表，第一位学号，第二位姓名
    """
    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 设置学生学号与姓名文件地址
    stuIndex_path = './stu_num/stu_num.csv'

    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 开始读取学生信息
    stuInfo_list = []
    try:
        with open(stuIndex_path, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            index = 0
            for row in csv_reader:
                if index == 0:
                    logging.warning("This is table header")
                    index = index + 1
                else:
                    stuId = row[0].replace(" ", "")
                    stuName = row[1].replace(" ", "")
                    tempInfo = [stuId, stuName]
                    stuInfo_list.append(tempInfo)
                    index = index + 1
        logging.warning(stuInfo_list)
    except:
        with open(stuIndex_path, encoding='gbk') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            index = 0
            for row in csv_reader:
                if index == 0:
                    logging.warning("This is table header")
                    index = index + 1
                else:
                    stuId = row[0].replace(" ", "")
                    stuName = row[1].replace(" ", "")
                    tempInfo = [stuId, stuName]
                    stuInfo_list.append(tempInfo)
                    index = index + 1
        logging.warning(stuInfo_list)
    return stuInfo_list


def importSignin():
    """
    importSignin 获取签到信息
    :return: 二位列表，第一位签到姓名，第二位签到时间
    """
    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 设置学生学号与姓名文件地址
    signinIndex_path = './file/signin.csv'

    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 开始读取学生信息
    signinInfo_list = []
    try:
        with open(signinIndex_path, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            index = 0
            for row in csv_reader:
                if index == 0:
                    logging.warning("This is table header")
                    index = index + 1
                else:
                    signinName = row[0].replace(" ", "")
                    signinTime = row[2]
                    tempInfo = [signinName, signinTime]
                    signinInfo_list.append(tempInfo)
                    index = index + 1
        logging.warning(signinInfo_list)
    except:
        with open(signinIndex_path, encoding='gbk') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            index = 0
            for row in csv_reader:
                if index == 0:
                    logging.warning("This is table header")
                    index = index + 1
                else:
                    signinName = row[0].replace(" ", "")
                    signinTime = row[2].replace(" ", "")
                    tempInfo = [signinName, signinTime]
                    signinInfo_list.append(tempInfo)
                    index = index + 1
        logging.warning(signinInfo_list)
    return signinInfo_list


def blurSearch(id, str, array):
    """
    向文件名列表查询学生姓名，返回一个[学号,姓名,结果]
    :param id: 学号
    :param str: 姓名
    :param array: 签到信息 [签到姓名, 签到时间]
    :return: [学号,姓名,结果] 结果有则为 √ ，没有则为空格
    """
    TempResult = []
    for index in range(len(array)):
        item = array[index]
        if str in item[0]:
            TempResult = [id, str, item[1], "√"]
            return TempResult
    TempResult = [id, str, " ", " "]
    return TempResult


def writeCSV(array):
    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 创建写入地址文件和表头
    file_path = './result/result.csv'
    header = ['ID','NAME', 'SIGN_IN_TIME', 'RESULT']

    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 写入信息
    with open(file_path, 'w', encoding='gbk', newline='') as write_csv:
        # 1:创建writer对
        writer = csv.writer(write_csv)
        # 2:写表头
        writer.writerow(header)
        # 3:遍历列表，将每一行的数据写入csv
        for line in array:
            writer.writerow(line)


def signinCheck():
    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 加载学生信息
    StuInfo_list = importStuNum()

    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 加载签到信息
    SigninInfo_list = importSignin()

    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 开始处理数据
    index = 0
    result = []
    for index in range(len(StuInfo_list)):
        TempStu = StuInfo_list[index]
        stuId = TempStu[0]
        stuName = TempStu[1]
        TempResult = blurSearch(stuId, stuName, SigninInfo_list)
        result.append(TempResult)

    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 写入数据
    writeCSV(result)
