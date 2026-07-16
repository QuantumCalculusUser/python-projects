# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        if len(s) < total_len:
            return []

        target = {}
        for word in words:
            target[word] = target.get(word, 0) + 1

        result = []

        for offset in range(word_len):
            left = offset
            count = 0
            current = {}

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                if word not in target:
                    current.clear()
                    count = 0
                    left = right + word_len
                    continue

                current[word] = current.get(word, 0) + 1
                count += 1

                while current[word] > target[word]:
                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    count -= 1

                if count == num_words:
                    result.append(left)

        return result


if __name__ == "__main__":
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    print(Solution().findSubstring(s, words))
