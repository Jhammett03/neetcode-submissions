class Solution:
    def isValid(self, s: str) -> bool:
        mp = {"}" : "{", ")" : "(", "]" : "["}
        stack = []

        for c in s:
            if c in mp:
                if not stack or stack.pop() != mp[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0