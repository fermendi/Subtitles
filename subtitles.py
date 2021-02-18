#
# @file <subtitles.py>
#
# @author Fernando Mendiburu - <fernando.mendiburu@ee.ufcg.edu.br>
#

import argparse

from subtitle import Subtitle
from handle_files import HandleFiles


def Credits():
    print("\n----------------------------------------------------------------\n"
          "subtitles.py: Print the subtitles in only one line!\n"
          "Fernando Mendiburu - 2021\n"
          "----------------------------------------------------------------\n")


class Parameters:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Information')
        self.parser.add_argument('--path_file', '--p', '-p', dest='path_folder',
                                 type=str, required=True,
                                 help='Path folder to find .str files')
        self.parser.add_argument('--overwrite_file', '--o', '-o', dest='overwrite_file',
                                 type=str, required=True,
                                 help='Overwrite the file')
        self.args = self.parser.parse_args()

    def get_params(self):
        return self.args


if __name__ == '__main__':
    Credits()
    params = Parameters().get_params()
    files = HandleFiles(params.path_folder, ".srt").find_files()
    for file in files:
        print(f'File: "{file}"')
        sub = Subtitle(file)
        try:
            print(params.overwrite_file)
            sub.run(params.overwrite_file)
        except:
            pass
