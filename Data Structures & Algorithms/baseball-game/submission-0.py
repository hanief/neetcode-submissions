class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i, ops in enumerate(operations):
            n = len(record)
            if ops == "+":
                record.append(int(record[n-1]) + int(record[n-2]))
            elif ops == "D":
                record.append(int(record[n-1]) * 2)
            elif ops == "C":
                record.pop()
            else:
                record.append(int(ops))

        return sum(record)
