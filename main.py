# -*- coding:utf-8 -*-
import csv
import os
import logging


def fileCheck():
    """
    fileCheck 用来获取指定目录内的所有文件名称并形成列表
    :return: list 文件名列表
    """
    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 获取指定路径下的全部文件名称
    file_path = './file'

    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 开始遍历所有子目录
    file_list = []
    file_list = os.listdir(file_path)

    # logging.warning(file_list)
    logging.warning("Finish index")
    return file_list


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
    with open(stuIndex_path,encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        index = 0
        for row in csv_reader:
            if index == 0:
                logging.warning("This is table header")
                index = index + 1
            else:
                stuId = row[0].replace(" ","")
                stuName = row[1].replace(" ","")
                tempInfo = [stuId,stuName]
                stuInfo_list.append(tempInfo)
                index = index + 1
    logging.warning(stuInfo_list)
    return stuInfo_list


def blurSearch(id, str, array):
    """
    向文件名列表查询学生姓名，返回一个[学号,姓名,结果]
    :param id: 学号
    :param str: 姓名
    :param array: 文件列表
    :return: [学号,姓名,结果] 结果有则为 √ ，没有则为空格
    """
    TempResult = []
    result = [s for s in array if str in s]
    logging.warning(result)
    if len(result) != 0:
        # 如果结果不为空则说明查询到了
        TempResult = [id, str, "√"]
    else:
        # 如果结果为空则说明没有找到
        TempResult = [id, str, " "]

    return TempResult


def writeCSV(array):
    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 创建写入地址文件和表头
    file_path = './result/result.csv'
    header = ['id', 'name', 'result']

    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 写入信息
    with open(file_path, 'w', encoding='gbk', newline='') as write_csv:
        # 1:创建writer对象
        writer = csv.writer(write_csv)
        # 2:写表头
        writer.writerow(header)
        # 3:遍历列表，将每一行的数据写入csv
        for line in array:
            writer.writerow(line)


def main():
    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 加载目标文件列表
    AllFile_list = fileCheck()

    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 加载学生信息
    StuInfo_list = importStuNum()

    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 开始处理数据
    index = 0
    result = []
    for index in range(len(StuInfo_list)):
        TempStu = StuInfo_list[index]
        stuId = TempStu[0]
        stuName = TempStu[1]
        TempResult = blurSearch(stuId, stuName, AllFile_list)
        result.append(TempResult)

    # -~-~-~-~-~-~-~-~-~-~-~-~-
    # 写入数据
    writeCSV(result)


if __name__ == "__main__":
    main()












