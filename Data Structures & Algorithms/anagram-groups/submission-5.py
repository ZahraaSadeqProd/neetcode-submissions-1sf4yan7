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
            arr = [0] * 26

            for char in word:
                index = ord(char) - 97
                
                arr[index] += 1

            key = tuple(arr)

            if key in hashmap:
                hashmap[key].append(word)

            else:
                hashmap[key] = [word]

        res = []
        
        for item in hashmap:
            value = hashmap[item]
            res.append(list(value))

        return res



        