#
# @file <subtitle.py>
#
# @author Fernando Mendiburu - <fernando.mendiburu@ee.ufcg.edu.br>
#


import sys
import shutil

from common import Functions, Constants
from timestamp import TimeStamp
from handle_files import HandleFiles


class Subtitle:
    def __init__(self, name_file):
        self.name_file = name_file
        self.timestamp = TimeStamp()
        self.raw_subtitle = []
        self.list_subtitle = []
        self.timestamps = []

    def separate_timestamp(self):
        self.raw_subtitle = HandleFiles.read_lines_from_file(self.name_file)
        self.raw_subtitle = Functions.remove_of_list(self.raw_subtitle, Constants.NEWLINE, False)

        for line in self.raw_subtitle:
            if self.timestamp.is_timestamp(line):
                tuple_time = self.timestamp.pick_timestamp(line)
                self.timestamps.append(tuple_time)

    def fix_timestamp(self):
        if len(self.timestamps):
            time_saved = self.timestamps[-1][0]
            timestamp_fixed = []

            for line in reversed(self.timestamps):
                timestamp_fixed.append(tuple([line[0], time_saved]))
                time_saved = line[0]

            timestamp_fixed.reverse()
            timestamp_fixed.pop(-1)
            timestamp_fixed.append(tuple([self.timestamps[-1][0], self.timestamps[-1][1]]))

            return timestamp_fixed
        else:
            print("Insert lines in .srt file!\n"
                  "Exit program!\n")
            sys.exit()

    def fix_subtitles(self, timestamp_fixed):
        i = 0
        for line in self.raw_subtitle:
            if self.timestamp.is_timestamp(line):
                self.list_subtitle.append(f'{timestamp_fixed[i][0]}{Constants.ARROW}{timestamp_fixed[i][1]}')
                i += 1
            else:
                self.list_subtitle.append(line)
        return self.list_subtitle

    def run(self, overwrite):
        self.separate_timestamp()
        time_fixed = self.fix_timestamp()
        subs_fixed = self.fix_subtitles(time_fixed)
        if overwrite == 'No':
            shutil.copy2(self.name_file, f'{self.name_file}_ORIGINAL')
        HandleFiles.write_to_file(subs_fixed, self.name_file)



if __name__ == '__main__':
    name_file = input("Insert the name of the .srt file!\n")
    sub = Subtitle(name_file)
    sub.run('Yes')

