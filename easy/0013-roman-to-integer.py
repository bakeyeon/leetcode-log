class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        res = 0
        roman = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000, 
        }

        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in roman:
                res += roman[s[i:i+2]]
                i += 2
            else:
                res += roman[s[i]]
                i += 1
        
        return res