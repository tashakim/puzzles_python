preIndex = 0
postIndex = 0

def constructFromPrePost(self, pre, post):
    root = TreeNode(pre[self.preIndex])
    self.preIndex += 1
    if root.val != 