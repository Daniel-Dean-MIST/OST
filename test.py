class Solution:
    def isValid(s: str) -> bool:
        combo_list = {'(':')', ')':'(', '[':']', ']':'[', '{':'}', '}':'{'}
        
        reverse_list = []

        i = len(s)
        
        print(i)

        while i > 0:
            reverse_list.append(s[i-1])

            i -= 1
        return reverse_list

print(Solution.isValid('Annelise'))