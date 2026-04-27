class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = students
        leftover = sandwiches
        end = False

        while not end:
            for student in queue:
                if student == leftover[0]:
                    queue.remove(student)
                    del leftover[0]
                else:
                    queue.remove(student)
                    queue.append(student)
            
            if len(leftover) <= 0 or leftover[0] not in queue:
                end = True
        
        return len(queue)