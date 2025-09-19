def length_of_longest_substring(s: str) -> int:
    chars = set()
    left = res = 0
    for right in range(len(s)):
        while s[right] in chars:
            chars.remove(s[left])
            left += 1
        chars.add(s[right])
        res = max(res, right - left + 1)
    return res