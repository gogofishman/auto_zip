# -*- coding: utf-8 -*-
import subprocess
import traceback
import os
import sys
import time
import configparser

version = '1.1.1'
file_pw = ''  # 密码
size = ''
words = []
config = configparser.ConfigParser()


def main(in_dir):
    print('version: ' + version)
    global file_pw
    global size
    global words
    file_path = os.path.dirname(in_dir) + "/"  # 文件路径
    file_name = os.path.basename(in_dir)  # 文件名带后缀
    _name, houzhui = os.path.splitext(file_name)

    # 敏感词替换
    if len(words) > 0:
        for w in words:
            if _name.find(w) >= 0:
                print('发现敏感词:', w, ",已替换")
                _name = _name.replace(w, 'O' * len(w))
    print('设置密码————————', file_pw)

    # 压缩内层
    print("正在压缩内层包。。。。。")
    command = 'HaoZipC a -tzip -p"{1}" "{2}{3}(内层).zip" "{0}" -mm=Copy'.format(
        in_dir, file_pw, file_path, _name)
    subprocess.run(command, shell=True, cwd="./HaoZip")

    # 压缩外层
    if size != '' or size != '0':
        # 有分卷压缩参数
        zip1_size = os.path.getsize("{0}{1}(内层).zip".format(file_path, _name))/1024/1024  # 获取内层压缩包大小
        if zip1_size >= int(size):
            print("正在压缩外层包，启用分卷压缩。。。。。")
            command2 = 'HaoZipC a -tzip -v{4}m "{2}{3}.zip" "{2}{3}(内层).zip" -mm=Copy'.format(
                in_dir, file_pw, file_path, _name, size)
        else:
            print("正在压缩外层包。。。。。")
            command2 = 'HaoZipC a -tzip -p"{1}" "{2}{3}.zip" "{2}{3}(内层).zip" -mm=Copy'.format(
                in_dir, file_pw, file_path, _name)
    else:
        # 无分卷压缩参数
        print("正在压缩外层包。。。。。")
        command2 = 'HaoZipC a -tzip -p"{1}" "{2}{3}.zip" "{2}{3}(内层).zip" -mm=Copy'.format(
            in_dir, file_pw, file_path, _name)
    subprocess.run(command2, shell=True, cwd="./HaoZip")
    os.remove('{0}{1}(内层).zip'.format(file_path, _name))


if __name__ == '__main__':
    params = sys.argv[1]
    if os.path.exists(params):  # 检查路径是否存在
        exe_path, exe_name = os.path.split(sys.argv[0])
        if exe_path:
            os.chdir(exe_path)  # 切换工作目录到程序同目录
        config.read('设置.ini', encoding='utf-8')
        file_pw = config['自定义']['压缩密码']
        size = config['自定义']['分卷压缩大小']
        words = config['自定义']['敏感词'].split('，')
        try:
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
