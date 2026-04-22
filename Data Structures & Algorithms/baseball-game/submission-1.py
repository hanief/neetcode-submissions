class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record, res = [], 0
        for i, ops in enumerate(operations):
            if ops == "+":
                res += record[-1] + record[-2]
                record.append(record[-1] + record[-2])
            elif ops == "D":
                res += (record[-1] * 2)
                record.append(record[-1] * 2)
            elif ops == "C":
                res -= record.pop()
            else:
                res += int(ops)
                record.append(int(ops))

        return res
