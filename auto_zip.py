
# -*- coding: utf-8 -*-
import subprocess
import traceback
import os
import sys
import time
import configparser

version = '1.0.1'
file_pw = ''  # 密码
size = 0
config = configparser.ConfigParser()


def main(in_dir):
    print('version: ' + version)
    global file_pw
    global size
    file_path = os.path.dirname(in_dir) + "/"  # 文件路径
    file_name = os.path.basename(in_dir)  # 文件名带后缀
    _name, houzhui = os.path.splitext(file_name)

    command = 'HaoZipC a -tzip -p"{1}" "{2}{3}(内层).zip" "{0}" -mm=Copy'.format(
        in_dir, file_pw, file_path, _name)
    command2 = 'HaoZipC a -tzip -v{4}m "{2}{3}.zip" "{2}{3}(内层).zip" -mm=Copy'.format(
        in_dir, file_pw, file_path, _name, size)
    # 同路径下需要有压缩程序 HaoZipC
    print('开始压缩。。。')
    print('设置密码————————',file_pw)
    subprocess.run(command, shell=True, cwd=os.path.dirname(sys.executable) + "./HaoZip")
    subprocess.run(command2, shell=True, cwd=os.path.dirname(sys.executable) + "./HaoZip")
    os.remove('{0}{1}(内层).zip'.format(file_path, _name))


if __name__ == '__main__':
    params = sys.argv[1]
    if os.path.exists(params):  # 检查路径是否存在
        try:
            exe_path, exe_name = os.path.split(os.path.realpath(sys.argv[0]))
            config.read(exe_path + '/' + '设置.ini', encoding='utf-8')
            file_pw = config['自定义']['压缩密码']
            size = config['自定义']['分卷压缩大小']
            main(params)
        except Exception as e:
            traceback.print_exc()
        finally:
            print("3秒后自动退出")
            time.sleep(3)
            print('退出')
    else:
        print('找不到文件!')
        input('按回车键退出...')