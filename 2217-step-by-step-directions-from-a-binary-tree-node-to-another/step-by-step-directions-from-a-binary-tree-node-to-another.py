# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_path_from_root(cur_node, target_value, path_to_append):
            if cur_node is None:
                return False
            if cur_node.val == target_value:
                return True

            path_to_append.append("R")
            if find_path_from_root(cur_node.right, target_value, path_to_append):
                return True
            # If we haven't found target at right subtree delete it from path
            path_to_append.pop()

            path_to_append.append("L")
            if find_path_from_root(cur_node.left, target_value, path_to_append):
                return True
            path_to_append.pop()

            return False

        path_to_start = []
        find_path_from_root(root, startValue, path_to_start)
        path_to_destination = []
        find_path_from_root(root, destValue, path_to_destination)

        common_path_len = 0  # length of the path to LCA
        while (
            common_path_len < len(path_to_start)
            and common_path_len < len(path_to_destination)
            and path_to_start[common_path_len] == path_to_destination[common_path_len]
        ):
            common_path_len += 1

        # First we need to go up to the LCA
        res = ["U" for _ in range(len(path_to_start) - common_path_len)]
        # Then we just go through all the path to destination without common path
        res += path_to_destination[common_path_len:]

        return "".join(res)