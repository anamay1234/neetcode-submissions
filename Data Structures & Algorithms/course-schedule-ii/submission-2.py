class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        inorder = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)

            inorder[course] += 1
    

        q = deque()

        for course in range(numCourses):
            if inorder[course] == 0:
                q.append(course)


        order = []
        
        while q:
            courseDone = q.popleft()
            order.append(courseDone)

            for course in graph[courseDone]:
                inorder[course] -= 1

                if inorder[course] == 0:
                    q.append(course)

        return [] if len(order) != numCourses else order



        