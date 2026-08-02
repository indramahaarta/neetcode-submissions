class Node:
    def __init__(self, key: int = 0, val: int = 0, next: Optional[Node] = None, prev: Optional[Node] = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0
        self.mp = {}
        

    def get(self, key: int) -> int:
        if key in self.mp:
            # get the node
            cur_node = self.mp[key]

            # initialize the prev and next_node
            prev_node = cur_node.prev
            next_node = cur_node.next # can be None

            # change the pointer of prev and next node
            prev_node.next = next_node
            next_node.prev = prev_node

            # change the pointer of cur_node and tail node
            prev_node = self.tail.prev
            prev_node.next = cur_node
            cur_node.prev = prev_node
            cur_node.next = self.tail
            self.tail.prev = cur_node

            return cur_node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            cur_node = self.mp[key]
            cur_node.val = value

            # initialize the prev and next_node
            prev_node = cur_node.prev
            next_node = cur_node.next # can be None

            # change the pointer of prev and next node
            prev_node.next = next_node
            next_node.prev = prev_node

            # change the pointer of cur_node and tail node
            prev_node = self.tail.prev
            prev_node.next = cur_node
            cur_node.prev = prev_node
            cur_node.next = self.tail
            self.tail.prev = cur_node
            return None


        if self.size >= self.capacity:
            first_node = self.head.next
            second_node = first_node.next

            # change the pointer of head and second node
            self.head.next = second_node
            second_node.prev = self.head

            del self.mp[first_node.key]
        
        node = Node(key, value)
        
        # change the pointer of tail
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node

        node.next = self.tail
        self.tail.prev = node

        # record in the map
        self.mp[key] = node

        self.size += 1
        
