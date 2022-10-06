import re


def simplifyPath( path):
    res = []
    for i in path.split("/"):
        if i != '' and i != '.' and i != '..':
            res.append(i)
        if i == '..' and res:
            res.pop()

    return '/'+'/'.join(res)

path = "/home/../../temp//./"

print(simplifyPath(path))