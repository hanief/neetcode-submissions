class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []

        for str in strs:
            isGrouped = False
            sortedStr = "".join(sorted(str))
            
            for group in groups:
                sortedFirst = "".join(sorted(group[0]))
                if sortedStr == sortedFirst:
                    group.append(str)
                    isGrouped = True
                    break
            
            if not isGrouped:
                newGroup = [str]
                groups.append(newGroup)
        
        return groups if len(groups) else [[""]]