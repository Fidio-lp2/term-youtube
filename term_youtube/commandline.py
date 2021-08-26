# -*- coding:utf-8 -*-
"""
Create a pseudo command line.
"""

import re
import sys
import termios
# THE ULTIMATE SPECIAL MAGIC SPELL
import readline


class CommandLine():
    prompt: str
    cmdlog = []

    __hiragana: re.Pattern
    __katakana: re.Pattern
    __kanji: re.Pattern
    __sonota: re.Pattern

    def __init__(self, prompt: str = '>') -> None:
        self.prompt = prompt

        self.__sonota = re.compile('[\u3000-\u3040]+')
        self.__hiragana = re.compile('[\u3041-\u309F]+')
        self.__katakana = re.compile('[\u30A0-\u30FF]+')
        self.__kanji = re.compile('[\u4E00-\u9FFF]+')

    def commandline(self) -> str:
        sys.stdout.write(self.prompt + ' ')
        sys.stdout.flush()

        input_value = self.__enhancedInput()

        return input_value

    def __dig_up_cmdlog(self, sub: int) -> str:
        """
        Parameters
        ----------
        direc : bool
            When direc is 0, go back one command log.
            When direc is 1, go one step forward it.
        """
        sys.stdout.write("\033[2K\033[G")
        sys.stdout.write(self.prompt + ' ')
        sys.stdout.flush()

        try:
            return_val = self.cmdlog[sub]
        except IndexError:
            return_val = ''

        return return_val

    def __enhancedInput(self) -> str:
        fd = sys.stdin.fileno()

        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)

        new[3] &= ~termios.ICANON

        new[3] &= ~termios.ECHO

        input_str = []

        try:
            termios.tcsetattr(fd, termios.TCSANOW, new)

            string: str = ''
            cmdlog_sub: int = len(self.cmdlog)

            while True:
                string = sys.stdin.read(1)

                # delete operation
                if string.encode('utf-8') == b'\x7f':
                    if len(input_str) != 0:
                        sys.stdout.write("\033[1D\033[K")
                        pop_char = input_str.pop()

                        if self.__hiragana.fullmatch(pop_char) or\
                        self.__katakana.fullmatch(pop_char) or\
                        self.__kanji.fullmatch(pop_char) or\
                        self.__sonota.fullmatch(pop_char):
                            sys.stdout.write("\033[1D")

                        sys.stdout.flush()

                    continue

                # up arrow and down arrow operation
                elif string.encode('utf-8') == b'\x1b':
                    string = sys.stdin.read(1)
                    string = sys.stdin.read(1)

                    judge_str = string.encode('utf-8')

                    if judge_str == b'A':
                        if cmdlog_sub > 0:
                            cmdlog_sub -= 1
                    elif judge_str == b'B':
                        if cmdlog_sub < len(self.cmdlog):
                            cmdlog_sub += 1
                    else:
                        continue

                    string = self.__dig_up_cmdlog(cmdlog_sub)
                    input_str = list(string)
                    sys.stdout.write(string)
                    sys.stdout.flush()
                    continue

                # enter operation
                elif string.encode('utf-8') == b'\n' or string.encode('utf-8') == b'\r':
                    break

                sys.stdout.write(string)
                sys.stdout.flush()
                input_str.append(string)

        finally:
            termios.tcsetattr(fd, termios.TCSANOW, old)

        self.cmdlog.append(''.join(input_str))
        return ''.join(input_str)
