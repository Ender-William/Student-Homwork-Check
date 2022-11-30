# -*- coding:utf-8 -*-
import homeworkCheck
import signinCheck

def main():
    while True:
        # -~-~-~-~-~-~-~-~-~-~-~-~-
        # 选择需要执行的程序
        print()
        print("------アルトリアのAvalon------")
        print("---------可执行的程序---------")
        print("A. 检查作业提交情况")
        print("B. 检查腾讯会议等签到情况")
        print("----------------------------")
        print("H. 帮助")
        print("----------------------------")
        Choose = input("请输入要执行的程序：").replace(" ","")

        if Choose == "a" or Choose == "A":
            # 执行作业检查
            homeworkCheck.homeworkCheck()

        if Choose == "b" or Choose == "B":
            # 执行签到检查
            signinCheck.signinCheck()

        if Choose == "h" or Choose == "H":
            print("A.检查作业提交情况")
            print("通过对比学生学号名单与作业文件名单，得出作业提交情况表")
            print()
            print("B. 检查腾讯会议等签到情况")
            print("通过对比学生学号名单与会议软件签到名单，得出签到情况")
            input("按下任意按键以继续")
            print()


if __name__ == "__main__":
    main()












