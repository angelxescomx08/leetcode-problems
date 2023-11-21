# 104. Maximum Depth of Binary Tree

Este problema se resuelve fácil, la profundidad máxima de un árbol binario es el camino de nodos más largo posible. Para calcularlo simplemente pensemos que recorremos el árbol desde la raíz, si la raíz apunta a nada, regresamos un 0, en caso contrario medimos la profundidad del hijo izquierdo y derecho más 1 dado que el nodo raíz cuenta. Ahora en el algoritmo ya recorrimos el lado izquierdo y derecho por lo que simplemente retornamos el lado que sea mayor.

```py
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right)+1)
```