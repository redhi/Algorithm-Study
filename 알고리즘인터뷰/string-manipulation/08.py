class person(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


def solution(strings, n):
    tmp_dict = {}

    tmp_dict[person("bob")] = 18
    tmp_dict[person("bob")] = 20
    tmp_dict[person("anna")] = 15

    print(tmp_dict)


solution("", 1)
