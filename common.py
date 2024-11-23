#!C:\Users\pypy2\AppData\Local\Programs\Python\Python311\python.exe
import os.path
from datetime import datetime as datetime
import time
import json as js
import threading
import re


g_log_file_name = ''
g_log_file = None
start = 0.


def time_stamp():
    now = datetime.now()
    stamp = datetime.strftime(now, '%Y%m%d%H%M%S.%f')
    return stamp


def time_str():
    now = datetime.now()
    stamp = datetime.strftime(now, '%Y-%m-%d %H:%M:%S.%f')
    return stamp[:-3]


def start_timer():
    global start
    start = time.time()
    return start


def get_start_time():
    start_time = datetime.fromtimestamp(start)
    return datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S.%f')


def time_elapse():
    elapse = time.time() - start
    elapse_seconds = elapse
    days = int(elapse // (24 * 3600))
    elapse %= 24 * 3600
    hours = int(elapse // 3600)
    elapse %= 3600
    minutes = int(elapse // 60)
    elapse %= 60
    seconds = int(elapse)
    elapse %= 1
    milliseconds = int(elapse * 1000)
    elapse *= 1000
    microseconds = int(elapse * 1000)
    return elapse_seconds, days, hours, minutes, seconds, milliseconds, microseconds


def file_name_info(file_path):
    file_dir = os.path.dirname(file_path)
    file_name = os.path.split(file_path)[-1]
    file_ext = file_name.split('.')
    return file_dir, file_name, file_ext


def diclist2dic(diclist, keys):
    dics = dict()
    if not isinstance(keys, list):
        keys = [keys]
    for dic in diclist:
        key = ':'.join([str(dic[key]) for key in keys])
        dics[key] = dic
    return dics


class DicObj:
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                setattr(self, key, DicObj(value))
            else:
                setattr(self, key, value)


def dic2obj(dic):
    return DicObj(dic)


def set_log_file(file_name, suffix=None, timestamp = False):
    global g_log_file
    global g_log_file_name
    log_dir = os.path.dirname(file_name)
    if not log_dir:
        log_dir = './logs'
    file_name = os.path.split(file_name)[-1].split('.')[0]

    if suffix:
        file_name = file_name + '.' + suffix

    if timestamp:
        log_file_name = os.path.join(log_dir, '%s_%s.log' % (file_name, time_stamp()[:-7]))
    else:
        log_file_name = os.path.join(log_dir, file_name + '.log')

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    g_log_file_name = os.path.abspath(log_file_name)
    g_log_file = open(log_file_name, mode='wt+', encoding='utf-8')
    return g_log_file_name


def get_log_file_name():
    return g_log_file_name


def log(*args):
    current_thread_id = threading.current_thread().ident
    print('%s[%s]:' % (time_str(), current_thread_id), *args)
    if g_log_file:
        print('%s[%s]:' % (time_str(), current_thread_id), *args, file=g_log_file)
        g_log_file.flush()


def logs(title, *args):
    print('%s:' % time_str(), title)
    print(*args)
    if g_log_file:
        print('%s:' % time_str(), title, file=g_log_file)
        print(*args, file=g_log_file)


def query_log(start_time=None, end_time=None, thread_id=None):
    if g_log_file is None:
        return ''
    log_lines = []
    # 日志格式： 2024-11-23 15:50:10.238[15972]: log text
    r'b([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]b'
    pat = r'(?P<log_time>[2]\d{3}-\d{2}-\d{2}\s\d{2}\:\d{2}\:\d{2}.\d{3})\[(?P<log_thread_id>[0-9]+)\]\:'
    with open(g_log_file_name, 'rt', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        m = re.match(pat, line)
        if not m:
            break
        log_time = m.group('log_time')
        log_thread_id = m.group('log_thread_id')
        if end_time and log_time > end_time:
            break
        if start_time and log_time < start_time:
            continue
        if thread_id and int(log_thread_id) != thread_id:
            continue
        log_lines.append(line)
    return ''.join(log_lines)


def load_json(file_name):
    if not os.path.exists(file_name):
        return None
    with open(file_name, 'r', encoding='utf8') as f:
        return js.load(f)


def save_json(obj, file_name):
    with open(file_name, 'w', encoding='utf8') as f:
        js.dump(obj, f, indent=2, ensure_ascii=False)


def get_train_params(vars):
    para_names = ['batch_size', 'learning_rate', 'lr', 'epochs', 'num_epochs']
    train_params = {}
    for name in para_names:
        if name in vars:
            train_params[name] = vars[name]
    return train_params


# def test_log():
#     name = 'Charley'
#     log('hello, %s' % (name), '\n This is an example of log() \n')




