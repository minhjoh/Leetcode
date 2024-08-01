class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            age = int(detail[11:13]) > 60
            if age: count += 1
        return count

