class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        w = 0 
        r = 0

        while r < len(chars):
            ch = chars[r]
            counter = 0

            while r < len(chars) and chars[r] == ch:
                r += 1
                counter += 1
            
            chars[w] = ch
            w += 1

            if counter > 1:
                for d in str(counter):
                    chars[w] = d
                    w += 1

        return w