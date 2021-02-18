#
# @file <common.py>
#
# @author Fernando Mendiburu - <fernando.mendiburu@ee.ufcg.edu.br>
#

import re


class Constants:
    WHITESPACE = ' '
    NEWLINE = '\n'
    BLANK_LINE = ''
    ARROW = ' --> '


class Functions:
    @staticmethod
    def is_included(word, line):
        return word in line

    @staticmethod
    def remove_of_list(list, word_to_remove, exact_match=True):
        list_new = []
        for line in list:
            if exact_match:
                if line is not word_to_remove:
                    list_new.append(line)
            else:
                list_new.append(re.sub(word_to_remove, '', line))
        return list_new


if __name__ == '__main__':
    pass
