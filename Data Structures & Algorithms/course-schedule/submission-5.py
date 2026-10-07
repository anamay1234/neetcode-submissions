class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        inorder = [0] * numCourses 


        for course, prereq in prerequisites:
            graph[prereq].append(course)

            inorder[course] += 1


        q = deque()

        for course in range(numCourses):
            if inorder[course] == 0:
                q.append(course)

        while q:

            doingCourse = q.popleft()

            for course in graph[doingCourse]:
                inorder[course] -= 1

                if inorder[course] == 0:
                    q.append(course)

        return True if max(inorder) == 0 else False
        

        