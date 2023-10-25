class Solution:
    def lengthOfLongestSubstring(self, s):
        char_index_map = {}
        max_length = 0
        start = 0

        for end in range(len(s)):
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                start = char_index_map[s[end]] + 1
            char_index_map[s[end]] = end
            max_length = max(max_length, end - start + 1)

        return max_length


def test_lengthOfLongestSubstring():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring(" ") == 1
    assert solution.lengthOfLongestSubstring("au") == 2
    assert solution.lengthOfLongestSubstring("dvdf") == 3
    print("Todos os testes passaram!")


if __name__ == "__main__":
    test_lengthOfLongestSubstring()
