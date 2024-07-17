# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:
        if not root:
            return

        to_delete: set[int] = set(to_delete)
        res: list[TreeNode] = [root] if not root.val in to_delete else []
        queue: deque[TreeNode] = deque([root])

        while queue:
            cur_node: TreeNode = queue.popleft()

            if cur_node.left:
                queue.append(cur_node.left)

                if cur_node.left.val in to_delete:
                    cur_node.left = None  # disconnect left child if we will delete it

            if cur_node.right:
                queue.append(cur_node.right)

                if cur_node.right.val in to_delete:
                    cur_node.right = None

            if cur_node.val in to_delete:  # if we need to delete this node
                if cur_node.left is not None:  # It's None if we need to delete left child too
                    res.append(cur_node.left)
                if cur_node.right is not None:
                    res.append(cur_node.right)

        return res
