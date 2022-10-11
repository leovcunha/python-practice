# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        
        
       #      3
       #     / \
       #    5   1
       #   / \  /\
       #  6  7 8  0     
       #  /\
       # 9 10
        dic = {}
  
        #step 1 - up - find the line of antecessors-sucessors from root to target putting the parent of each node in a dictionary
                      
        q2 = []
        q2.append((root)) #node, parent
        dic[root.val] = None
        
        while q2:
            nod = q2.pop(0)
            
            
            if nod.val == target.val:
                break
            if nod.left:
                dic[nod.left.val] = nod
                q2.append(nod.left)
            if nod.right:
                dic[nod.right.val] = nod
                q2.append(nod.right)

        #down get the nodes that are at a distance K down the target 
        
        queue = []
        visited = set()
        queue.append((target,0))
        answer = []
        
        while queue:
            nod = queue.pop(0)
            visited.add(nod[0].val)
            
            if nod[1] == k:
                print(nod)
                answer.append(nod[0].val)
                continue
                
            if nod[0].left and nod[0].left.val not in visited:
                    queue.append((nod[0].left, nod[1]+1))
                
            if nod[0].right and nod[0].right.val not in visited:
                    queue.append((nod[0].right, nod[1]+1))  
                
    # to get the nodes upwards traversing using the parent dict and appending to the queue with the distance         
            if nod[0].val in dic.keys():
                if dic[nod[0].val] and dic[nod[0].val].val not in visited:
                    queue.append((dic[nod[0].val],nod[1]+1))
        
        return answer 
