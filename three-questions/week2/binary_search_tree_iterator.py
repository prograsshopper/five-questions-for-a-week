# Flatten Tree

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.bst_list = []
        self.index = -1
        self.flatten(root)
    
    def flatten(self, root):
        if not root:
            return
        self.flatten(root.left)
        self.bst_list.append(root.val)
        self.flatten(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.bst_list[self.index]
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index < (len(self.bst_list) - 1)

