class Solution:
    def mask_pii(self, s: str) -> str:
        # email
        ans = ''
        flag = False
        cnt = 0
        if s.find('@') > 0:
            for i in s[::-1]:
                ans += i.lower()
                if flag:
                    ans += '*' * 5 + s[0].lower()
                    return ans[::-1]
                if i == '@':
                    flag = True

            return ans[::-1]
        else:
            # phone
            for i in s[::-1]:
                if ord('0') <= ord(i) <= ord('9'):
                    cnt += 1
                    if cnt == 11:
                        flag = True
                        ans += '-'
                    if cnt <= 4:
                        ans += i
                    else:
                        ans += '*'
                    if cnt == 4 or cnt == 7:
                        ans += '-'
            if flag:
                ans += '+'
            return ans[::-1]

# test git reset
email = "LeetCode@LeetCode.com"
solution = Solution()
print(solution.mask_pii(email))
