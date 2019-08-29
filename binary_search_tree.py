INT_MAX = float('inf')
INT_MIN = float('-inf')


class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def bst_insert(self, value):
        if value <= self.data:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.bst_insert(value)
        else:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.bst_insert(value)

    def contains(self, value):
        if value == self.data:
            return True
        elif value <= self.data:
            if not self.left:
                return False
            else:
                return self.left.contains(value)
        elif value >= self.data:
            if not self.right:
                return False
            else:
                return self.right.contains(value)

    def get_size(self):
        if self.left and self.right:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return 1

    def print_spiral_order(self):
        if not self.data:
            print "It is an empty Node"
            return None
        stack_left = []
        stack_right = []
        stack_right.append(self)
        while stack_right or stack_left:
            # stay while either has elements
            while stack_right:
                root = stack_right.pop()
                print root.data
                if root.right:
                    stack_left.append(root.right)
                if root.left:
                    stack_left.append(root.left)

            while stack_left:
                root = stack_left.pop()
                print root.data
                if root.left:
                    stack_right.append(root.left)
                if root.right:
                    stack_right.append(root.right)

    def print_in_order(self):
        if self.left:
            self.left.print_in_order()
        print self.data
        if self.right:
            self.right.print_in_order()

    def __repr__(self):
        return "Node-{n}".format(n=self.data)


def is_bst(node):
    return (is_bst_util(node, INT_MIN, INT_MAX))


def is_bst_util(node, mini, maxi):
    # Retusn true if the given tree is a BST and its values
    # >= min and <= max

    # An empty tree is BST
    if node is None:
        return True

    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (is_bst_util(node.left, mini, node.data - 1) and
            is_bst_util(node.right, node.data + 1, maxi))


if __name__ == '__main__':
    print "Binary Search Tree..."
    # n4 = Node(1)
    # n4.bst_insert(3)
    # n4.bst_insert(2)
    # n4.bst_insert(7)
    # n4.bst_insert(4)
    # n4.bst_insert(5)
    # n4.bst_insert(6)
    # n4.bst_insert(8)
    # n4.bst_insert(9)
    # n4.bst_insert(10)
    # n4.print_spiral_order()

    # n4.print_in_order()
    # print "Size is {}".format(n4.get_size())
    # print "Is BST -- {}".format(is_bst(n4))
    # print spiral order
    n1 = Node(1)
    n1.left = Node(2)
    n1.right = Node(3)

    n1.left.left = Node(4)
    n1.left.right = Node(5)

    n1.right.left = Node(6)
    n1.right.right = Node(7)

    n1.left.left.left = Node(8)
    n1.left.right.left = Node(9)

    n1.right.right.right = Node(10)
    # n1.print_in_order()

    n1.print_spiral_order()
