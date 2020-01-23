import os
import re

from File import File
from Function import Function


def find_file(path):
    py_files = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(('.py')):
                rel_dir = os.path.relpath(root, path)
                rel_file = os.path.join(rel_dir, filename)
                if rel_file.startswith('.'):
                    py_files.append(path + rel_file[1:])
                else:
                    py_files.append(path + '/' + rel_file)
    return py_files


def parse_file(file_path):
    file = File(os.path.basename(file_path), os.path.getsize(file_path))
    f = open(file_path, 'r',encoding='utf-8')
    line = f.readline()
    curr_fun = None
    fun_indent_position = 0
    while line:
        # parse if line is not comment or is not empty - have only whitespaces
        if not line.isspace() and not line.startswith('#'):
            words = line.strip().split(' ')
            words = list(filter(None, words))

            # line is function definition only if starts with "def" word
            if words[0] == 'def':
                fun_indent_position = indent_pos(line)
                # function name is always after "def" and before character "("
                function_name = words[1].split('(')[0]
                curr_fun = Function(function_name + '()')
                file.add_functions(curr_fun)

            elif words[0] == 'import' or words[0] == 'from':
                # dependency name is always after "import" or "from"
                dependency = words[1].split('.')[-1]
                file.add_dependency(dependency + '.py')

            # if parser is in function definition lines
            elif curr_fun:
                # if function ended
                if indent_pos(line) <= fun_indent_position:
                    curr_fun = None
                else:
                    for word in words:
                        # check if word have character "(" so can have a function name
                        if '(' in word:
                            function_names = word.split('(')[:-1]
                            for function_name in function_names:
                                function_name = function_name.split('.')[-1]
                                # add if name contains only allowed characters
                                if re.match(r'^[A-Za-z0-9_]+$', function_name):
                                    curr_fun.add_functions_names(function_name + '()')

        line = f.readline()
    f.close()
    return file


def indent_pos(line):
    return len(line) - len(line.lstrip())
