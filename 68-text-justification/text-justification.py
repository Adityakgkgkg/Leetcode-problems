class Solution(object):
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            letters = 0

            
            while j < n and letters + len(words[j]) + (j - i) <= maxWidth:
                letters += len(words[j])
                j += 1

            line_words = words[i:j]
            gaps = len(line_words) - 1

          
            if j == n or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))

            else:
                spaces = maxWidth - letters
                space_per_gap = spaces // gaps
                extra_spaces = spaces % gaps

                line = ""

                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (space_per_gap + (1 if k < extra_spaces else 0))

                line += line_words[-1]

            result.append(line)
            i = j

        return result

        