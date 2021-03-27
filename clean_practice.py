import os


def find_all(string, substring):
    """
    Yields all the positions of
    the pattern p in the string s.
    """

    result_idxs = []
    idx = string.find(substring)
    while idx != -1:
        result_idxs.append(idx)
        idx = string.find(substring, idx + 1)

    return result_idxs


def get_only_task_comment(string: str):
    parts = string.split('"""')
    if len(parts) == 3:
        comment_task = '"""\n'
        lines = parts[1].split('\n')
        if lines[0] == '' or lines[0] == '    ':
            del lines[0]
        if lines[-1] == '' or lines[-1] == '    ':
            del lines[-1]
        need_replace = lines[0].find('') >= 0
        for line in lines:
            if need_replace:
                comment_task += line.replace('    ', '', 1)
            else:
                comment_task += line

            comment_task += '\n'
        comment_task += '"""'
        return comment_task
    else:
        pass
        return parts[0]


def clean_file_with_solution(f_path):
    with open(f_path, "r") as f:
        text = f.read()
        cleaned_string = get_only_task_comment(text)

    with open(f_path, "w") as f:
        f.write(cleaned_string)


if __name__ == '__main__':
    folders_with_solutions = []
    folder = []
    for i in os.walk('.'):
        folder.append(i)
        if 'hw' in i[0] or 'practice' in i[0]:
            folders_with_solutions.append(i)

    folders_with_solutions.sort()
    for address, dirs, files in folders_with_solutions:
        print(address, dirs, files)
        for file_path in files:
            if '.pyc' not in file_path and '__init__' not in file_path:
                clean_file_with_solution(os.path.join(address, file_path))
