class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Input: strs = ["act","pots","tops","cat","stop","hat"]
        Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

        
        hash = 
        {
            "act" : set("act"),
            "opst" : set("pots"),
        
        }


        word = "pots"
        check if "opst" in set:
            add to "opst" 
        else:
            add "opsts" key and "pots" to set 

        """

        hashmap = {}

        for word in strs:
            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word)

            if sorted_word in hashmap:
                hashmap[sorted_word].append(word)

            else:
                hashmap[sorted_word] = [word]

        res = []
        
        for item in hashmap:
            value = hashmap[item]
            res.append(list(value))

        return res



        