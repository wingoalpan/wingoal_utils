
import sys, os
import argparse
import time

sys.path.append('..\\..\\wingoal_utils')
from common import (
    set_log_file,
    log,
    logs
)

set_log_file(os.path.split(__file__)[-1], timestamp=True)


def main():
    print('to be implemented')


def test_0():
    print('You can provide some other functions here')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("params", nargs="*")
    args = parser.parse_args()
    if len(args.params) == 0:
        log('executing function [main] ...')
        main()
    else:
        func = args.params[0]
        if func != 'main':
            set_log_file(os.path.split(__file__)[-1], suffix=func, timestamp=True)
        param_list = args.params[1:]
        log('executing function [%s] ...' % func)
        eval(func)(*param_list)
    log('finish executing function!')

