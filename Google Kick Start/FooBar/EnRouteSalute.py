s= '--->-><-><-->-'
s= '--->-<-'
s= '<<>><'


def solution(s):
    comes = goes = 0
    for index, emp in enumerate(s):
        right = left = 0
        if emp == '>':
            for i in s[index:]:
                if i == '<':
                    right += 1

        if emp == '<':
            for i in s[:index]:
                if i == '>':
                    left += 1

        comes += right
        goes += left
    return comes + goes


print(solution(s))