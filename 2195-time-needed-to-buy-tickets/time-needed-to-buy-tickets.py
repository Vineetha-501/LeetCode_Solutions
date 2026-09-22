class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        q = deque()
        # Put all the persons in the queue
        for i in range(len(tickets)):
            q.append(i)
        turns = 0
        # Simulate as lond as tickets[k] > 0
        while tickets[k] > 0:
            # Pop from queue
            front = q.popleft()
            # Serve him a ticket
            tickets[front] -= 1
            # see if he/she still needs more tickets
            if tickets[front] > 0:
                q.append(front)
            turns += 1
        
        return turns