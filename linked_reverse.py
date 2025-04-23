class ListNode():
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next
    #初始化

def create_linked(nums):
    head = ListNode(nums[0]) #將head設定成第一個節點(數字)
    curr = head #設定一個目標節點
    for num in nums[1:]:
        curr.next = ListNode(num)
        curr = curr.next
    #開始跑迴圈把 list 轉換成 linked_list
    return head

def reverse_node(head):
    curr = head #設定一個目標節點
    prev = None #設定一個結尾節點導向None
    while curr:
        next_step = curr.next #紀錄原本curr應該導向的下一個節點
        curr.next = prev #將節點前進方向倒轉 (把下一個節點變成前一個節點)
        prev = curr #前一個節點變成現在節點
        curr = next_step #現在節點變成下一個節點
    return prev

# curr 還是一樣照順序走 None -> 1 -> 2 -> 3 -> 4 -> 5 (照順序消失)
# prev則是 None <- 1 <- 2 <- 3 <- 4 <- 5 (照 1 2 3 4 5 的順序出現)

def print_node(node):
    while node:
        print(node.val,end= " -> " if node.next else '\n')
        node = node.next

a = reverse_node(create_linked([1,2,3,4,5]))
b = create_linked([1,2,3,4,5])
print_node(a)
print_node(b)

