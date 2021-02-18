#
# @file <handle_files.py>
#
# @author Fernando Mendiburu - <fernando.mendiburu@ee.ufcg.edu.br>
#

import os


class HandleFiles:
    def __init__(self, path, extension):
        self.path = path
        self.extension = extension
        self.root = ''
        self.dirs = []
        self.files = []
        self.file_list = []

    def find_files(self):
        for self.root, self.dirs, self.files in os.walk(self.path):
            for file in self.files:
                if file.endswith(self.extension):
                    self.file_list.append(os.path.join(self.root, file))
        return self.file_list

    @staticmethod
    def read_lines_from_file(file_name):
        all_lines = []
        try:
            with open(file_name, 'r') as fh:
                all_lines = fh.readlines()
        except FileNotFoundError:
            print("File not found to read!")
        finally:
            return all_lines

    @staticmethod
    def write_to_file(data_fixed, new_file):
        with open(new_file, 'w') as f:
            for line in data_fixed:
                f.write(f'{line}\n')
        print('File successfully fixed and saved!\n')


if __name__ == '__main__':
    pass