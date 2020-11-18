from node import Node


def inorder_traversal(node: Node) -> list:
    if node is None:
        return []
    numbers = []
    numbers += inorder_traversal(node.left)
    numbers.append(node.data)
    numbers += inorder_traversal(node.right)
    return numbers


def preorder_traversal(node: Node) -> list:
    if node is None:
        return []
    numbers = [node.data]
    numbers += preorder_traversal(node.left)
    numbers += preorder_traversal(node.right)
    return numbers


def postorder_traversal(node: Node) -> list:
    if node is None:
        return []
    numbers = []
    numbers += postorder_traversal(node.left)
    numbers += postorder_traversal(node.right)
    numbers.append(node.data)
    return numbers


def execute_inorder_traversal():
    n = Node(0)
    right = n.insert_right(Node(2))
    right.insert_right(Node(4))
    left = n.insert_left(Node(3))
    left.insert_left(Node(5))
    print(inorder_traversal(n))


def execute_preorder_traversal():
    n = Node(0)
    right = n.insert_right(Node(2))
    right.insert_right(Node(4))
    left = n.insert_left(Node(3))
    left.insert_left(Node(5))
    print(preorder_traversal(n))


def execute_postorder_traversal():
    n = Node(0)
    right = n.insert_right(Node(2))
    right.insert_right(Node(4))
    left = n.insert_left(Node(3))
    left.insert_left(Node(5))
    print(postorder_traversal(n))


if __name__ == '__main__':
    print('----inorder traversal----')
    execute_inorder_traversal()
    print('----preorder traversal----')
    execute_preorder_traversal()
    print('----postorder traversal----')
    execute_postorder_traversal()