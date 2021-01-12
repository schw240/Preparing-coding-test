# def longestPalindrome(s):
#     res = ""
#     for i in range(len(s)):
#         print(i)
#         for j in range(len(s),i,-1):
#             print(j)
#             if len(res)>=j-i:
#                 print(i,j)
#                 break
#             elif s[i:j] == s[i:j][::-1]:
#                 print(s[i:j][::-1])
#                 res = s[i:j]
#                 print(res)
#     return res
# print(longestPalindrome(["babad"]))
s = "babad"
print(s[0:5])
print(s[0:5][::-1])