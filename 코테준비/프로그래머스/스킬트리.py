import copy


def solution(skill, skill_trees):
    answer = 0
    s_skill = []

    for i in range(len(skill)):
        s_skill.append(skill[: i + 1])
    for i in range(len(skill_trees)):
        skill_trees[i] = "".join(x for x in skill_trees[i] if x in skill)
    # print(skill_trees)

    # print(s_skill)
    for tree in skill_trees:
        is_not = 0
        for s in s_skill:
            if s == tree:
                is_not = 1
                break
            if tree == "":
                is_not = 1
                break
        if is_not == 1:
            answer += 1

    return answer


skill = "CB"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA", "C", "AAA"]
print(solution(skill, skill_trees))
