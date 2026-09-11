class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in sorted_map:
                sorted_map[sorted_string].append(string)
            else:
                sorted_map[sorted_string] = [string]
        return list(sorted_map.values())