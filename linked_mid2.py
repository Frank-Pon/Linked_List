class ListNode():
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
# 初始化

def create_linked(nums):
    head = ListNode(nums[0])
    curr = head
    for i in nums[1:]:
        curr.next = ListNode(i)
        curr = curr.next
    return head
# 把 list 轉換成 linked_list

def find_K(head,k): #多一個 k 參數 用來抓倒數第 k 位節點
    slow = head #設定目標節點1
    fast = head #設定目標節點2
    for _ in range(k):
        fast = fast.next
    # 先讓快的節點走幾步
    while fast:
        slow = slow.next
        fast = fast.next
    # 偷跑完後再一起跑,最後慢跑的就會停在要取的節點
    return slow

head = create_linked([1,2,3,4,5])
a = find_K(head,2)
print(a.val)