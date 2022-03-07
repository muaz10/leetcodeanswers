from collections import Counter

def characterReplacement(s: str, k: int) -> int:
    left = 0
    max_len = 0
    counter = Counter()
    
    # move right and add right to dict
    for right in range(len(s)):
        counter[s[right]] += 1
    
        # if exceeds limit, deduct left from dict and move left
        # NOTE: ints that can be exchanged = ints in the sliding window that is not the most frequent element in dic
        while (right - left + 1 - max(counter.values())) > k:
            counter[s[left]] -= 1
            left += 1
            
        # update window size
        max_len = max(max_len, right - left + 1)
        
    # return 
    return max_len

s = "ABAB"
characterReplacement(s, 2)