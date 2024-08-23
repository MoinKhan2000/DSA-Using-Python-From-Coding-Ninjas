verse(head, k):
    # return reverseLinkedListIteratively(head,head.next.next)[0]
    if head is None or head.next is None or k <= 1:
        return head
    start = head
    end = head
    i = 0
    while i < k:
        end = end.next
        i += 1
        if end is None:
            return head
    printLinkedList(end)
    remaining = end
    end, start = reverseLinkedListIteratively(start, end)
    start.next = kReverse(remaining, k)
    return end
