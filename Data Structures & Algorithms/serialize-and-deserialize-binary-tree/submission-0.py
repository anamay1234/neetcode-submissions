# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        s = ""
        q = deque()
        q.append(root)

        while q:
            curNode = q.popleft()

            if curNode is None:
                s += "#,"
            else:
                s += str(curNode.val) + ","
                q.append(curNode.left)
                q.append(curNode.right)

        return s

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        # Split string by commas into an iterator to mirror getline(s, str, ',')
        values = iter(data.split(","))

        # Initialize root node
        first_val = next(values)
        root = TreeNode(int(first_val))

        q = deque([root])

        while q:
            node = q.popleft()

            # Process left child
            left_val = next(values)
            if left_val == "#":
                node.left = None
            else:
                left_node = TreeNode(int(left_val))
                node.left = left_node
                q.append(left_node)

            # Process right child
            right_val = next(values)
            if right_val == "#":
                node.right = None
            else:
                right_node = TreeNode(int(right_val))
                node.right = right_node
                q.append(right_node)

        return root
