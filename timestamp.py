#
# @file <timestamp.py>
#
# @author Fernando Mendiburu - <fernando.mendiburu@ee.ufcg.edu.br>
#

from datetime import datetime
from common import Constants, Functions


class TimeStamp:
    @staticmethod
    def is_timestamp(line):
        if Functions.is_included(Constants.ARROW, line) and \
                TimeStamp.is_time(line.split(Constants.ARROW)[0]) and \
                TimeStamp.is_time(line.split(Constants.ARROW)[1]):
            return True
        else:
            return False

    @staticmethod
    def pick_timestamp(line):
        time_start = line.split(Constants.ARROW)[0]
        time_end = line.split(Constants.ARROW)[1]
        return tuple([time_start, time_end])

    @staticmethod
    def is_time(line):
        try:
            datetime.strptime(line, '%H:%M:%S,%f')
            return True
        except:
            return False

if __name__ == '__main__':
    pass
