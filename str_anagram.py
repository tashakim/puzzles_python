from collections import Counter
import pytest

""" ### Task hw3.15 Is Anagram
Given two strings s and t, write a function to determine if t is an anagram of s. 
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
""" TFD Steps
1. Inputs
- String s, and string t

2. Outputs
- Boolean, True or False

3. Special Cases
- s is None or t is None
- s == '' or t == ''
- len(s) == 1 and len(t) == 1
- len(s) != len(t)

4. Usual Cases
- s, t are non-empty strings with length >= 1
Example: s = 'car', t = 'cra'


5, 6, 7, 8: See below
"""
# 5. Function Specification, & 7. Implement Function
def is_anagram(s: str, t: str) -> bool:
    """
    Purpose:
    Time Complexity:
    Space Complexity: O(n) 
    """
    if s is None or t is None:
        raise Exception("Input string(s) is invalid")
    return Counter(s) == Counter(t)

# 6. Implement Test Cases
def test_is_anagram():
    assert is_anagram('rat', 'tar') == True, "Usual test failed"
    assert is_anagram('anagrampossible', 'sibelsopnagaram') == True, "Longer test failed"

    assert is_anagram('a', 'b') == False, "Single different char test failed"
    assert is_anagram('a', 'a') == True,  "Single same char test failed"

    assert is_anagram('aab', 'baa') == True, "Order test failed"
    assert is_anagram('aab', 'abb') == False, "Repeat char test failed"
    assert is_anagram('abb', 'ab') == False, "Different length test failed"

    with pytest.raises(Exception):
        is_anagram(None, None) # Raise error when input string is None
    with pytest.raises(Exception):
        is_anagram(None, 'abc') # Raise error when input string is None


if __name__ == "__main__":
    test_is_anagram()

# 8. Add/Improve tests as needed
# A: No additional tests needed

# END OF SOLUTION
