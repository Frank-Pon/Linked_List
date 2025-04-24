class ListNode():
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
#初始化
def create_linked(nums):
    head = ListNode(nums[0])
    curr = head
    for _ in nums[1:]:
        curr.next = ListNode(_)
        curr = curr.next
    return head
#把 list 轉換成 linked list


linked_list = create_linked([5,10,1,20,50,4,30,8,7,6,8,14])

even = [] #偶數陣列
curr = [] #設定當前陣列
long = [] #設定最長陣列
while linked_list:
    if linked_list.val % 2 == 0:
        curr.append(linked_list.val)
        # 如果 linked_list有值,且當前節點的值是偶數就放進當前陣列
    else:
        if curr:
            if len(curr)>len(long):
                long = curr
            even.append(curr)
        curr=[]
        #如果遇到奇數,且當前陣列比最長陣列長就將當前陣列放進最長陣列並清空當前陣列
        #接著把當前陣列放進偶數陣列然後清空當前陣列
    linked_list=linked_list.next
    #做完一輪就更新節點
    if len(curr)>len(long):
        long = curr
    #避免最後沒有奇數不會比較,所以最後再比較一次
even.append(curr)
#將最後一次的curr放進even
    
print(f"偶數段: {even} 最長偶數段為: {long}")

