class ListNode():
    def __init__(self,val = 0 ,next = None):
        self.val = val
        self.next = next
# 初始化

def create_linked(nums):
    head = ListNode(nums[0])
    curr = head
    for num in nums[1:]:
        curr.next = ListNode(num)
        curr = curr.next
    return head
#把 list 轉換成 linked_list

def find_mid(head):
    slow = head #設定目標節點1
    fast = head #設定目標節點2
    while fast and fast.next: #因為fast要一次走兩步,所以fast走完就停
        slow = slow.next 
        fast = fast.next.next
        #slow走一步 fast走兩步 -> fast走完時,slow剛好在中間,列表內容物偶數時會停在中間靠後位置
    return slow

head = create_linked([1,2,3,4,5])
mid = find_mid(head)
print(mid.val)
