class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) {
            return false;
        }

        const sTable = s.split("").reduce(function(acc, cur) {
            acc[cur] = acc[cur] ? acc[cur] + 1 : 1;
            return acc;
        }, {})
        const tTable = t.split("").reduce(function(acc, cur, i) {
            acc[cur] = acc[cur] ? acc[cur] + 1 : 1;
            return acc;
        }, {})

        if (sTable.length !== tTable.length) {
            return false;
        }
        
        for (const letter in sTable) {
            if (sTable[letter] !== tTable[letter]) {
                return false
            }
        }

        return true
        // const sortedS = s.split("").sort().join();
        // const sortedT = t.split("").sort().join();
        
        // return sortedS == sortedT
    }
}
