class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # get a count of a every task in tasks
        # Now all do is every time u do the task with maxFrequency.
        # Then do the next task if it is there.

        hashmap = {}

        for task in tasks:
            if task not in hashmap:
                hashmap[task] = hashmap.get(task, 0) + 1
            else:
                hashmap[task] += 1

        counts = list(hashmap.values())
        # count of task, time till can be done next
        counts = [counts[i] * -1 for i in range(len(counts))]

        heapq.heapify(counts)

        q = deque()
        time = 1

        while counts or q:

            if q and q[0][1] == time:
                canDoNow = q.popleft()
                heapq.heappush(counts, canDoNow[0])

            if counts:
                # take maxmimum task
                maxTask = heapq.heappop(counts)
                # we did one of these tasks
                maxTask += 1
                if maxTask != 0:
                    q.append([maxTask, time + n + 1])

            if not counts and not q:
                return time

            time += 1







        