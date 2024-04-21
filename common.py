#!C:\Users\pypy2\AppData\Local\Programs\Python\Python311\python.exe
import os.path
from datetime import datetime as datetime
import time
import random
import json as js


g_log_file = None


def time_stamp():
    now = datetime.now()
    stamp = datetime.strftime(now, '%Y%m%d%H%M%S.%f')
    return stamp


def time_str():
    now = datetime.now()
    stamp = datetime.strftime(now, '%Y-%m-%d %H:%M:%S.%f')
    return stamp[:-3]


def file_name_info(file_path):
    file_dir = os.path.dirname(file_path)
    file_name = os.path.split(file_path)[-1]
    file_ext = name.split('.')
    return file_dir, file_name, file_ext


def set_log_file(file_name, suffix=None, timestamp = False):
    global g_log_file
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

    g_log_file = open(log_file_name, mode='wt+')


def log(*args):
    print('%s:' % time_str(), *args)
    if g_log_file:
        print('%s:' % time_str(), *args, file=g_log_file)


def logs(title, *args):
    print('%s:' % time_str(), title)
    print(*args)
    if g_log_file:
        print('%s:' % time_str(), title, file=g_log_file)
        print(*args, file=g_log_file)


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




