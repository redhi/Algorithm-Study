class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarayTree:
    def __init__(self):
        self.root = None

    def inorder(self, node):
        if node != None:
            if node.left:
                self.inorder(node.left)
            print(node.value, " ", end="")
            if node.right:
                self.inorder(node.right)

    def height(self, root):
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1


def solution(info, edges):
    answer = 0
    for i in range(len(info)):
        globals()["node{}".format(i)] = Node(info[i])
    tree = BinarayTree()
    tree.root = node0
    for e in edges:
        i, j = e

        if globals()["node{}".format(i)].left:
            globals()["node{}".format(i)].right = globals()["node{}".format(j)]
        else:
            globals()["node{}".format(i)].left = globals()["node{}".format(j)]

    tree.inorder(tree.root)

    return answer


info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [
    [0, 1],
    [1, 2],
    [1, 4],
    [0, 8],
    [8, 7],
    [9, 10],
    [9, 11],
    [4, 3],
    [6, 5],
    [4, 6],
    [8, 9],
]
print(solution(info, edges))
