def solution(new_id):
    new = ""
    
    new_id = new_id.lower()

    for i in range(len(new_id)):
        if (
            new_id[i].isalpha()
            or new_id[i].isdigit()
            or new_id[i] == "-"
            or new_id[i] == "_"
            or new_id[i] == "."
        ):
            new += new_id[i]

    while new.count("..") != 0:
        new = new.replace("..", ".")

    if new != "":
        if new[0] == ".":
            new = new[1:]
    if new != "":
        if new[-1] == ".":
            new = new[:-1]

    if new == "":
        new = "a"

    if len(new) >= 16:
        new = new[:15]
        if new[-1] == ".":
            new = new[:-1]

    if len(new) <= 2:
        while len(new) < 3:
            new += new[-1]

    return new


new_id = "...!@BaT#*..y.abcdefghijklm"
new_id = "a"
new_id = "z-+.^."
new_id = "=.="
new_id = "123_.def"
new_id = "abcdefghijklmn.p"
print(solution(new_id))
