from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.diameter = 0

    def height(node: Optional[TreeNode]) -> int:
      if node is None:
        return 0
      # Calculamos la altura de los subárboles izquierdo y derecho
      left_height = height(node.left)
      right_height = height(node.right)
      
      # Actualizamos el diámetro (que es el camino más largo entre dos nodos)
      self.diameter = max(self.diameter, left_height + right_height)
      
      # La altura del nodo actual es el máximo entre las alturas de sus subárboles más 1
      return max(left_height, right_height) + 1

    height(root)
    return self.diameter