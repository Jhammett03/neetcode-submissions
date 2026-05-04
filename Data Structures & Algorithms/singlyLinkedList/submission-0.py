class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr != None:
            if i == index:
                return curr.value
            i += 1
            curr = curr.next
        return -1


    def insertHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head.next
        self.head.next = new
        if not new.next:
            self.tail = new
        
    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while i < index and curr:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        curr = self.head.next
        out = []
        while curr:
            out.append(curr.value)
            curr = curr.next
        return out

        
