# Definition for binary tree node
# class TreeNode(item):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class CodingATree:

    def serialize(self, root):
        if not root: 
        	return 'x'

        return root.val, self.serialize(root.left), self.serialize(root.right)


    def deserialize(self, data):
        if data[0] == 'x': 
        	return None

        node = TreeNode(data[0])

        node.left = self.deserialize(data[1])
        node.right = self.deserialize(data[2])

        return node

""" Other method using memoization:

class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)

        return ' '.join(vals)
        

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())

        return doit()


"""