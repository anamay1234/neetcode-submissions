class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        q = deque()
        count = 0

        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            course = q.popleft()
            count += 1
            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    q.append(next_course)

        return count == numCourses


            
        