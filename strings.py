import sys
import re
from math import log, e
import math


def rotate_array(k, i):
    l = len(i)
    return i[l - k:l] + i[0:l - k]


def reverse_words_string(v):
    return " ".join(list(reversed(v.split())))


def eval_reverse_polish_notation(i):
    stack = []
    for v in i:
        stack.append(v)
        if v in ["+", "*", "-", "/"]:
            a, b, c = stack.pop(), stack.pop(), stack.pop()
            stack.append(eval("{}{}{}".format(c, a, b)))

    return stack.pop()


def is_isomorphic_string(s, t):
    if s is None or t is None or len(s) != len(t):
        return False

    m = dict()
    for i, c1 in enumerate(s):
        c2 = t[i]
        if c1 in m:
            if m[c1] != c2:
                return False
        else:
            if c2 in m.values():
                return False
            m[c1] = c2

    return True


class Word(object):
    def __init__(self, word, steps):
        self.word = word
        self.steps = steps


def word_ladder_1(begin, end, words):
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    queue = list()
    queue.append(Word(begin, 1))
    words.append(end)
    while queue:
        top = queue.pop()
        word = top.word

        if word == end:
            return top.steps

        for i, c in enumerate(word):
            for ch in ascii_lowercase:
                new_word = word
                if c != ch:
                    tmp = list(word)
                    tmp[i] = ch
                    new_word = "".join(tmp)
                if new_word in words:
                    queue.append(Word(new_word, top.steps + 1))
                    words.remove(new_word)

    return 0


def word_ladder_2(begin, end, words):
    pass


def find_kth(k, a, b, s1, s2):
    if s1 >= len(a):
        return b[s2 + k - 1]

    if s2 >= len(b):
        return a[s1 + k - 1]

    if k == 1:
        return min(a[s1], b[s2])

    m1 = s1 + k / 2 - 1
    m2 = s2 + k / 2 - 1
    if m1 < len(a):
        mid1 = a[m1]
    else:
        mid1 = sys.maxint

    if m2 < len(b):
        mid2 = b[m2]
    else:
        mid2 = sys.maxint

    if mid1 < mid2:
        return find_kth(k - k / 2, a, b, m1 + 1, s2)
    else:
        return find_kth(k - k / 2, a, b, s1, m2 + 1)


def find_median_sorted_array(a, b):
    total = len(a) + len(b)
    if total % 2 == 0:
        return (find_kth(total / 2 + 1, a, b, 0, 0) +
                find_kth(total / 2, a, b, 0, 0, )) / 2
    else:
        return find_kth(total / 2 + 1, a, b, 0, 0)


def find_kth_largest_elm(a, k):
    a = sorted(a)
    return a[len(a) - k]


def regexp_match(a, b):
    if len(b) == 0:
        return len(a) == 0

    if len(b) == 1 or b[1] != "*":
        if len(a) < 1 or (b[0] != '.' and a[0] != b[0]):
            return False
        return regexp_match(a[1:], b[1:])

    else:
        i = -1
        while i < len(a) and (i < 0 or b[0] == '.' or b[0] == a[i]):
            if regexp_match(a[i + 1:], b[2:]):
                return True
            i += 1
        return False


def candy(rating):
    if rating is None or len(rating) == 0:
        return 0
    candies = list()
    for i in range(len(rating)):
        candies.append(0)

    candies[0] = 1
    for i in range(1, len(rating)):
        if rating[i] > rating[i - 1]:
            candies[i] = candies[i - 1] + 1
        else:
            candies[i] = 1

    result = candies[len(rating) - 1]
    for i in range(len(rating) - 2, 0, -1):
        cur = 1
        if rating[i] > rating[i + 1]:
            cur = candies[i + 1] + 1

        result += max(cur, candies[i])
        candies[i] = cur

    return result


def merge_intervals(intervals):
    intervals = sorted(intervals)
    result = []
    pre = intervals[0]
    for i in range(0, len(intervals)):
        current = intervals[i]
        if pre[1] > current[0]:
            pre = [pre[0], max(current[1], pre[1])]
        else:
            result.append(pre)
            pre = current

    result.append(pre)
    return result


def insert_interval(intervals, new):
    result = []
    for _, i in enumerate(intervals):
        if i[1] < new[0]:
            result.append(i)
        elif i[0] > new[1]:
            result.append(new)
            new = i
        elif i[1] >= new[0] or i[0] <= new[1]:
            new = [min(i[0], new[0]),
                   max(new[1], i[1])]

    result.append(new)
    return result


def sum_1(numbers, target):
    hash_map = dict()
    for i, n in enumerate(numbers):
        if n in hash_map:
            return [hash_map.get(n), i]
        else:
            hash_map[target - n] = i


def sum_2(numbers, target):
    i, j = 0, len(numbers) - 1
    while i < j:
        x = numbers[i] + numbers[j]
        if x < target:
            i += 1
        elif x > target:
            j -= 1
        else:
            return [i + 1, j + 1]


class TwoSum(object):
    def __init__(self):
        self.hash_map = dict()

    def add(self, num):
        if num in self.hash_map:
            self.hash_map[num] += 1
        else:
            self.hash_map[num] = 1

    def find(self, num):
        for key, value in self.hash_map.iteritems():
            target = num - key
            if target in self.hash_map:
                if key == target and value < 2:
                    continue
                return True

        return False


def atoi(s):
    if not s:
        return 0

    flag = "+"
    if s[0] == "-":
        flag = "-"

    res = 0
    for i, ch in enumerate(s):
        if "0" <= ch <= "9":
            res = res * 10 + int(ch)

    if flag == "-":
        res *= -1

    if res > sys.maxint:
        return sys.maxint

    return res


def sum_3(arr):
    arr = sorted(arr)
    res = list()
    for i1, n in enumerate(arr):
        i2 = i1 + 1
        while i2 < len(arr):
            i3 = i2 + 1
            while i3 < len(arr):
                if arr[i1] + arr[i2] + arr[i3] == 0:
                    if not [arr[i1], arr[i2], arr[i3]] in res:
                        res.append([arr[i1], arr[i2], arr[i3]])
                i3 += 1
            i2 += 1

    return res


def sum_4(arr, target):
    arr = sorted(arr)
    res = list()
    for i1, n in enumerate(arr):
        i2 = i1 + 1
        while i2 < len(arr):
            i3 = i2 + 1
            while i3 < len(arr):
                i4 = i3 + 1
                while i4 < len(arr):
                    if arr[i1] + arr[i2] + arr[i3] + arr[i4] == target:
                        if not [arr[i1], arr[i2], arr[i3], arr[i4]] in res:
                            res.append([arr[i1], arr[i2], arr[i3], arr[i4]])
                    i4 += 1
                i3 += 1
            i2 += 1

    return res


def sum_3_closest(arr, target):
    m = sys.maxint
    res = 0
    arr = sorted(arr)
    for i, n in enumerate(arr):
        j = i + 1
        k = len(arr) - 1
        while j < k:
            s = n + arr[j] + arr[k]
            diff = abs(s - target)
            if diff == 0:
                return s

            if diff < m:
                m = diff
                res = s

            if s <= target:
                j += 1
            else:
                k -= 1

    return res


def sum_3_pointer(arr):
    res = []
    arr = sorted(arr)
    for i, n in enumerate(arr):
        if i == 0 or arr[i] > arr[i - 1]:
            j = i + 1
            k = len(arr) - 1
            while j < k:
                s = n + arr[j] + arr[k]
                if s == 0:
                    res.append([n, arr[j], arr[k]])
                    j += 1
                    k -= 1

                    while j < k and arr[j] == arr[j - 1]:
                        j += 1

                        while j < k and arr[k] == arr[k + 1]:
                            k -= 1

                elif s < 0:
                    j += 1
                else:
                    k -= 1

    return res


def merge_two_sorted_array(a, b):
    i, j, k, res = 0, 0, len(a) + len(b) - 2, list()
    while k >= 0:
        k -= 1
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    while i < len(a):
        res.append(a[i])
        i += 1
    while j < len(b):
        res.append(b[j])
        j += 1

    return res


def longest_valid_parentheses(string):
    x, i = "()", 0
    while string.find(x) != -1:
        x += "()"
        i += 1

    return i * 2


def strStr(haystack, needle):
    if not (haystack or needle or len(needle)):
        return 0

    for i, ch in enumerate(haystack):
        if needle in haystack[i:i + len(needle)]:
            return i

    return -1


def min_size_subarray_sum(arr, target):
    arr = sorted(arr, reverse=True)
    res = 1
    while res <= len(arr):
        if sum(arr[0:res]) >= target:
            return res
        res += 1

    return 0


def search_insert(arr, target):
    if target in arr:
        return arr.index(target)

    arr.append(target)
    return sorted(arr).index(target)


def longest_consecutive_sequence(arr):
    if len(arr) == 0:
        return 0
    res = 1
    for e in arr:
        left = e - 1
        right = e + 1
        count = 1
        while left in arr:
            arr.remove(left)
            count += 1
            left -= 1
        while right in arr:
            arr.remove(right)
            count += 1
            right += 1
        res = max(count, res)

    return res


def zig_zag_conversion(string, rows):
    """
    rows   = 3
    string = PAYPALISHIRING
    res    = PAHNAPLSIIGYIR

    P   A   H   N
    A P L S I I G
    Y   I   R

    item: 1 2 3 4 5 6 7 8 9 10 11
    row : 1 2 3 2 1 2 3 2 1 2  3
    col : 1 1 1 2 3 3 3 4 5 5  5

    rows   = 4
    string = PPAYPAASSRIHHSGR
    res    = PAHPASHSAPSIGYRR

    P     A     H
    P   A S   H S
    A P   S I   G
    Y     R     R

    row: 1 2 3 4 3 2 1
    col: 1 1 1 1 2 3 4
    """
    zig_zag, row, col, add, res = [[] for i in range(rows)], 0, 0, True, ""
    for ch in string:
        zig_zag[row].append(ch)

        if add:
            row += 1
        else:
            row += -1

        if row == rows - 1:
            add = False
        elif row == 0:
            add = True

    for i in range(rows):
        res += ''.join(zig_zag[i])

    return res


def add_binary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]


def add_binary_orig(x, y):
    """
    11 1 -> 11 01
    flag = False => 1 + 1     = 0 flag = True
    flag = True  => 1 + 0 + f = 0 flag = True
    flag = True  => 0 + 0 + f = 1 flag = False
    100
    """
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)

    result = ''
    carry = 0

    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0

        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1

    if carry != 0: result = '1' + result

    return result.zfill(max_len)


def length_last_word(string):
    return len(string.strip()) - string.strip().rfind(' ')


def triangle(arr):
    res = [min(arr[len(arr) - 1])]
    index = arr[len(arr) - 1].index(res[0])
    for i in range(len(arr) - 2, 0, -1):
        res.append(min(arr[i][index - 1: index + 1]))

    res.append(arr[0][0])
    return sum(res)


def contains_duplicate(arr):
    d = dict()
    for n in arr:
        if n in d:
            return True
        d[n] = n
    return False


def contains_duplicate_two(arr, k):
    d = dict()
    for i, n in enumerate(arr):
        if n in d:
            if i - d[n] <= k:
                return True
        else:
            d[n] = i
    return False


def insertion_sort(arr):
    for i, key in enumerate(arr):
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def exercise_1(n):
    z = 0
    o = 0
    for i in range(n):
        j = 1
        while j <= n:
            z += 1
            j *= 2
            o += 1
        o += 1
    return z


def remove_duplicate_from_sorted_array(arr):
    i = 0
    while True:
        if i >= len(arr) - 1:
            break
        if arr[i] == arr[i + 1]:
            del arr[i]
        i += 1

    return len(arr), arr


def remove_duplicate_from_sorted_array_two(arr):
    i = 0
    while True:
        if i >= len(arr) - 2:
            break
        if arr[i] == arr[i + 1] == arr[i + 2]:
            del arr[i]
        i += 1

    return len(arr), arr


def remove_element(arr, elem):
    i, j = 0, 0
    for j in range(len(arr)):
        if arr[j] != elem:
            arr[i] = arr[j]
            i += 1
    return i


def move_zero(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            del arr[i]
            arr.append(0)
    return arr


def trap_rain_water(height):
    if height is None or len(height) <= 2:
        return 0

    left, right = [0] * len(height), [0] * len(height)

    maximum, left[0] = height[0], height[0]

    # scan from left to right
    for i in range(len(height)):
        if height[i] < maximum:
            left[i] = maximum
        else:
            left[i] = height[i]
            maximum = height[i]

    # scan from right to left
    maximum = height[len(height) - 1]
    right[len(height) - 1] = height[len(height) - 1]
    for i in range(len(height) - 2, 0, -1):
        if height[i] < maximum:
            right[i] = maximum
        else:
            right[i] = height[i]
            maximum = height[i]

    return sum([min(left[i], right[i]) - h for i, h in enumerate(height)])


def summary_range(arr):
    result = []
    start = arr[0]
    for i, item in enumerate(arr[:len(arr) - 1]):
        if item + 1 == arr[i + 1]:
            end = item + 1
        else:
            if end:
                result.append(str(start) + "->" + str(end))
            else:
                result.append(str(item))
            start = arr[i + 1]
            end = None
    else:
        if end:
            result.append(str(start) + "->" + str(end))
        else:
            result.append(str(arr[len(arr) - 1]))

    return result


def one_edit_distance(s, t):
    if s is None or t is None:
        return False

    m, n = len(s), len(t)
    if abs(m - n) > 1:
        return False

    i, j, count = 0, 0, 0

    while i < m and j < n:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            count += 1
            if count > 1:
                return False
            if m > n:
                i += 1
            elif m < n:
                j += 1
            else:
                i += 1
                j += 1
    if i < m or j < n:
        count += 1

    if count == 1:
        return True

    return False


def shortest_word_distance(words, a, b):
    distance = None
    index = dict()
    index[a], index[b] = None, None

    for i, word in enumerate(words):
        if word == a:
            index[a] = i
        if word == b:
            index[b] = i

        if not index[a] is None and not index[b] is None:
            if distance:
                distance = min(distance, abs(index[a] - index[b]))
            else:
                distance = abs(index[a] - index[b])
            index[a], index[b] = None, None

            if word == a:
                index[a] = i
            if word == b:
                index[b] = i

    return distance


def shortest_word_distance_three(words, a, b):
    distance = None
    idx = None
    for i, w in enumerate(words):
        if w == a and idx:
            distance = min(distance, abs(i - idx)) if distance else abs(i - idx)
            idx = i
        elif w == a:
            idx = i

    return distance


def find_min_rotated_sorted_arr(arr):
    i, j = 0, len(arr) - 1
    while True:
        m = (i + j) / 2
        if arr[m] > arr[i]:
            i = m
        else:
            j = m
        if i + 1 == j:
            break

    return arr[i] if arr[i] < arr[j] else arr[j]


def find_min_rotated_sorted_arr_dup(arr):
    i, j = 0, len(arr) - 1
    while True:
        if arr[i] == arr[j]:
            i += 1
            continue
        m = (i + j) / 2
        if arr[m] < arr[i]:
            i = m
        else:
            j = m
        if i + 1 == j:
            break

    return arr[i] if arr[i] < arr[j] else arr[j]


def binary_search(arr, target):
    i, j = 0, len(arr) - 1

    while i + 1 < j:
        m = (i + j) / 2
        if target > arr[m]:
            i = m
        else:
            j = m

    if arr[i] == target:
        return i
    elif arr[j] == target:
        return j

    return -1


def search_range(arr, target):
    idx = binary_search(arr, target)
    if idx == -1:
        return -1, -1
    i, j = idx, idx
    break_left, break_right = False, False
    while not (break_right and break_left) and (j + 1 < len(arr)):
        if i != 0:
            if arr[i - 1] == target:
                i -= 1
            else:
                break_left = True
        else:
            break_left = True
        if arr[j + 1] == target:
            j += 1
        else:
            break_right = True

    return i, j


def guess_number(n):
    def guess(num):
        res = 153
        if num == res:
            return 0
        elif num < res:
            return -1
        else:
            return 1

    i, j = 0, n
    while i + 1 < j:
        m = (i + j) / 2
        x = guess(m)
        if x == 0:
            return m
        elif x > 0:
            j = m
        else:
            i = m


def solver():
    n = 1000
    for i in range(1, n, 1):
        if i + log(i, e) == 0:
            return i


def search_rotated_sorted_array(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        m = left + (right - left) / 2
        if target == arr[m]:
            return m

        if arr[left] <= arr[m]:
            if arr[left] <= target < arr[m]:
                right = m - 1
            else:
                left = m + 1
        else:
            if arr[m] < target <= arr[right]:
                left = m + 1
            else:
                right = m - 1

    return -1


def search_rotated_sorted_array_two(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        m = (left + right) / 2
        if target == arr[m]:
            return m

        if arr[left] <= arr[m]:
            if arr[left] <= target < arr[m]:
                right = m - 1
            else:
                left = m + 1
        elif arr[left] > arr[m]:
            if arr[m] < target <= arr[right]:
                left = m + 1
            else:
                right = m - 1
        else:
            left += 1

    return -1


class Stack(object):
    def __init__(self):
        self.min = None
        self.stack = list()

    def push(self, x):
        self.stack.append(x)
        if not self.min:
            self.min = x
        else:
            if self.min > x:
                self.min = x


def largest_rect_histogram(arr):
    stack, m = list(), 0
    i = 0
    while i < len(arr):
        if not stack:
            stack.append(i)
            i += 1
            continue
        if arr[i] >= arr[stack[len(stack) - 1]]:
            stack.append(i)
            i += 1
        else:
            h = arr[stack.pop()]
            w = i if not stack else i - stack[len(stack) - 1] - 1
            m = max(h * w, m)

    while stack:
        h = arr[stack.pop()]
        w = i if not stack else i - stack[len(stack) - 1] - 1
        m = max(h * w, m)

    return m


def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    arr = [0] * 26
    for i, ch in enumerate(s):
        arr[ord(ch) - ord('a')] += 1
        arr[ord(t[i]) - ord('a')] -= 1
    for i, x in enumerate(arr):
        if x != 0:
            return False

    return True


def palindrome_pairs(s):
    pairs = []
    data = dict()
    for i, w in enumerate(s):
        data[w[::-1]] = i

    for i, w in enumerate(s):
        if w in data:
            pairs.append([data[w], i])

    return pairs


def longest_sub_str(s):
    res = ""
    for i in range(len(s)):
        tmp = dict()
        for j, ch in enumerate(s, i):
            if ch in tmp:
                res = s[i:j] if len(s[i:j]) > len(res) else res
                break
            else:
                tmp[ch] = j
    return res


def longest_sub_str_2_unique_char(s):
    m, start, data = 0, 0, dict()

    for i, ch in enumerate(s):
        data[ch] = 1 if ch not in data else data[ch] + 1
        if len(data) > 2:
            m = max(m, i - start)
            while len(data) > 2:
                t = s[start]
                count = data[t]
                if count > 1:
                    data[t] = count - 1
                else:
                    del data[t]
                start += 1

    return max(m, len(s) - start)


def min_window_sub_str(s, t):
    pass


def get_target_num(arr, target):
    pass


def flip_game(s):
    result = []
    s = list(s)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1] and s[i] == '+':
            s[i], s[i + 1] = '-', '-'
            result.append(''.join(s))
            s[i], s[i + 1] = '+', '+'

    return result


def flip_game_two(s):
    s = list(s)
    for i in range(len(s) - 1):
        if s[i] == '+' and s[i + 1] == '+':
            s[i], s[i + 1] = '-', '-'
            win = flip_game_two(s)
            s[i], s[i + 1] = '+', '+'

            if not win:
                return True
    return False


def word_pattern(pattern, s):
    arr = s.split(" ")

    if len(arr) != len(pattern):
        return False

    data = dict()
    for i, p in enumerate(pattern):
        if p in data:
            if data[p] != arr[i]:
                return False
        elif arr[i] in data.values():
            return False
        data[p] = arr[i]

    return True


def is_scramble(s1, s2):
    if len(s1) != len(s2):
        return False

    if len(s1) == 0 or s1 == s2:
        return True

    if sorted(list(s1)) != sorted(list(s2)):
        return False

    for i in range(1, len(s1)):
        s11 = s1[0:i]
        s12 = s1[i:len(s1)]
        s21 = s2[0:i]
        s22 = s2[i:len(s2)]
        s23 = s2[0:len(s2) - i]
        s24 = s2[len(s2) - i:len(s2)]

        if is_scramble(s11, s21) and is_scramble(s12, s22):
            return True

        if is_scramble(s11, s24) and is_scramble(s12, s23):
            return True

    return False


def is_valid(string):
    o, e, stack, i = ['(', '[', '{'], [')', ']', '}'], [string[0]], 0
    for x, c in enumerate(string[1:]):
        if (c in o and stack[i] in e) or (c in e and stack[i] in o):
            stack.pop(i)

            i -= 1
        stack.append(c)
        i += 1

    stack.pop()
    if len(stack) == 0:
        return True
    return False


def remove_invalid_parentheses(s):
    result = list()
    for i, ch in enumerate(s):
        x = s[:i] + s[(i + 1):]
        if x not in result:
            if is_valid(x):
                result.append(x)

    return result


def is_valid_palindrome(string):
    string = re.compile('[^a-zA-Z]').sub("", string).lower()
    for i in range(len(string) - 1 / 2):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True


def shortest_palindrome(s):
    result = list()
    m = len(s) * 2
    for i in range(1, len(s)):
        x = s[len(s) - i::]
        x = x[::-1]
        if is_valid_palindrome(x + s):
            if len(x + s) < m:
                result.append(x + s)
                m = len(x + s)

    return result


def top_k_frequent_elements(arr, k):
    tmp = dict()
    for x in arr:
        tmp[x] = 1 if x not in tmp else tmp[x] + 1

    result = []
    for key, val in tmp.iteritems():
        if val == k:
            result.append(key)
    return result


def meeting_rooms_two(intervals):
    intervals = sorted(intervals)
    queue, rooms = list(), 1
    queue.append(intervals[0][1])
    for i, interval in enumerate(intervals[1:]):
        if interval[0] < queue[len(queue) - 1]:
            rooms += 1
        else:
            queue = queue[1:]
        queue.append(interval[1])
    return rooms


def meeting_rooms(intervals):
    intervals = sorted(intervals)
    for i in range(len(intervals) - 1):
        if intervals[i][1] < intervals[i + 1][0]:
            return False
    return True


def range_addition(length, updates):
    pass


def merge_k_sorted_arrays(arr):
    result = [x for x in arr[0]]
    for x in arr[1:]:
        for y in x:
            for i, z in enumerate(result):
                if y < z:
                    result.insert(i, y)
                    break
            else:
                result.append(y)
    return result


def contain_nearby_duplicate(nums, k, t):
    for i, n in enumerate(nums):
        if i + k < len(nums):
            if abs(n - nums[i + k]) == t:
                return True
        if i - k >= 0:
            if abs(n - nums[i - k]) == t:
                return True
    return False


def missing_number(nums):
    return len(nums) * (len(nums) + 1) / 2 - sum(nums)


def find_duplicate_number(arr):
    pass


def first_missing_positive(arr):
    for i, x in enumerate(sorted(arr)):
        if x >= 0:
            if x + 1 not in arr:
                return x + 1


def h_index(citation):
    result = 0
    for i, x in enumerate(sorted(citation)):
        result = max(result, min(x, len(citation) - i))
    return result


def sliding_window_max(nums, k):
    pass


def moving_avg_data_stream():
    pass


def largest_number(nums):
    def compare(s1, s2):
        s1, s2 = str(s1), str(s2)
        lr, rl = s1 + s2, s2 + s1
        return -cmp(str(lr), str(rl))

    return ''.join([str(x) for x in sorted(nums, cmp=compare)])


def increasing_triplet_subsequence(nums):
    x, y = sys.maxint, sys.maxint

    for z in nums:
        if x >= z:
            x = z
        elif y >= z:
            y = z
        else:
            return True

    return False


def course_schedule(num_courses, prerequisites):
    tmp = dict()
    for x in prerequisites:
        tmp[x[0]] = x[1]
        if x[0] in tmp.values():
            return False
    return True


def minimum_height_tree(n, edges):
    pass


def is_ugly(n):
    if n == 0:
        return False
    if n == 1:
        return True

    if n % 2 == 0:
        n /= 2
        return is_ugly(n)

    if n % 3 == 0:
        n /= 3
        return is_ugly(n)

    if n % 5 == 0:
        n /= 5
        return is_ugly(n)

    return False


def is_ugly_two(n):
    uglies = []
    i = 1
    while len(uglies) < n:
        if is_ugly(i):
            uglies.append(i)
        i += 1

    return uglies


def find_k_pairs_smallest_sums(num1, num2, k):
    resualt = []
    n1, n2 = 0, 0
    if k > 0:
        resualt.append([num1[0], num2[0]])

    for i in range(k - 1):
        a = num1[n1 + 1] + num2[n2]
        b = num1[n1] + num2[n2 + 1]
        if a < b:
            n1 += 1
        else:
            n2 += 1
        resualt.append([num1[n1], num2[n2]])

    return resualt


def edit_distance(s1, s2):
    n = len(s1) if len(s1) < len(s2) else len(s2)
    distance = 0
    # replace
    for i in range(n):
        if s1[i] == s2[i]:
            continue
        else:
            distance += 1


def word_break(s, data):
    for x in data:
        if x in s:
            s = s.replace(x, "")
        if len(s) == 0:
            return True
    return False


def maximum_subarray(nums):
    start = 0
    result = [nums[0]]
    max_sum = sum(result)
    for i, n in enumerate(nums):
        _sum = sum(nums[start:i])
        if _sum > max_sum:
            max_sum = _sum
            result = nums[start:i]
        if n > _sum:
            start = i

    return result


def maximum_product_subarray(nums):
    def prod(lst):
        if len(lst) == 0:
            return 0
        r = lst[0]
        for x in lst:
            r *= x
        return r

    start = 0
    result = [nums[0]]
    max_prod = sum(result)
    for i, n in enumerate(nums):
        _prod = prod(nums[start:i])
        if _prod > max_prod:
            max_prod = _prod
            result = nums[start:i]
        if n > _prod:
            start = i

    return result


def palindrome_partitioning(s):
    pass


def house_robber(nums):
    pass


def jump_game(nums):
    i = 0
    j = 0
    while True:
        if j > len(nums):
            return False
        j += 1

        if i > len(nums):
            return False

        if nums[i] > len(nums):
            return False

        if nums[i] == len(nums) - j:
            return True
        i = nums[i]


def jump_game_two(nums):
    last_reach = 0
    reach = 0
    step = 0
    i = 0
    while True:
        if i > reach or i >= len(nums):
            break
        if i > last_reach:
            step += 1
            last_reach = reach
        reach = max(reach, nums[i] + i)
        i += 1
    if reach < len(nums) - 1:
        return 0

    return step


def max_profit(prices):
    m = prices[0]
    result = 0
    for i in range(len(prices)):
        result = max(result, prices[i] - m)
        m = min(m, prices[i])

    return result


def max_profit_two(prices):
    profit = 0
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]
        if diff > 0:
            profit += diff
    return profit


def min_path_sum(grid):
    # 4 3 1 9
    # 2 4 8 6
    # 3 5 1 6
    # 7 2 3 8

    result = 0
    for arr in grid:
        result += min(arr)
    return result


def unique_path(m, n):
    # 4 1 4
    # 3 6 1
    # 7 2 9
    dp = [[None] * m] * n
    for i in range(m):
        dp[i][0] = 1

    for i in range(n):
        dp[0][i] = 1

    for i in range(m):
        for j in range(n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


def longest_increasing_subsequence(nums):
    maximum = [1] * len(nums)
    for i, n in enumerate(nums):
        for j, m in enumerate(nums[:i]):
            if n > m:
                maximum[i] = max(maximum[i], maximum[j] + 1)
            print ' ', n, '\t', m, '  \t', n > m, '\t', maximum
    return max(maximum)


def coin_change(coins, amount):
    pass


def perfect_squares(n):
    m = int(math.sqrt(n))
    dp = [sys.maxint] * (n + 1)
    for i in range(n):
        for j in range(m):
            if i == j * j:
                dp[i] = 1
            elif i > j * j:
                dp[i] = min(dp[i], dp[i - j * j] + 1)

    return dp[n]


def generate_parentheses(n):
    def dfs(result, s, left, right):
        if left > right:
            return

        if left == 0 and right == 0:
            result.append(s)
            return

        if left > 0:
            dfs(result, s + '(', left - 1, right)

        if right > 0:
            dfs(result, s + ')', left, right - 1)

    _result = []
    dfs(_result, "", n, n)
    return _result


def combination_sum(candidates, target):
    def dfs(candidates, target, j, curr, result):
        if target == 0:
            tmp = [curr]
            result.append(tmp)
            return

        for i in range(j, len(candidates)):
            if target < candidates[i]:
                return
            curr.append(candidates[i])
            dfs(candidates, target - candidates[i], i, curr, result)
            curr = curr[:len(curr) - 1]

    current, result = [], []
    candidates = sorted(candidates)
    dfs(candidates, target, 0, current, result)
    return result


def substr_concat_all_words(s, words):
    l = len(words[0])
    result = []
    for i in range(0, len(s) - l, l):
        if s[i:i + l] in words:
            print s[i:i + l], i
    return


def group_anagrams(s):
    pass


def wildcard_matching():
    pass


def is_reachable(nums, target):
    def dfs(_nums, left, right, target):
        result = []
        if left > right:
            return result
        elif left == right:
            result.append(_nums[left])
            return result
        for i in range(left, right):
            r1 = dfs(_nums, left, i, target)
            r2 = dfs(_nums, i + 1, right, target)

            for x in r1:
                for y in r2:
                    result.append(x + y)
                    result.append(x - y)
                    result.append(x * y)
                    if y != 0:
                        result.append(x / y)
        return result

    i, j = 0, len(nums) - 1
    results = dfs(nums, i, j, target)
    for num in results:
        if num == target:
            return True

    return False


def super_ugly_numbers(n, primes):
    pass


def word_break_two(s, data):
    def dfs(pos, result, curr, i):
        if i == 0:
            result.append(str.strip(curr))
            return

        for s in pos[i]:
            combined = s + " " + curr
            dfs(pos, result, combined, i - len(s))

    pos = [None] * (len(s) + 1)
    pos[0] = []
    for i in range(len(s)):
        if pos[i] is not None:
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if sub in data:
                    if pos[j] is None:
                        pos[j] = [sub]
                    else:
                        pos[j].append(sub)

    if pos[len(s)] is None:
        return []
    else:
        result = []
        dfs(pos, result, "", len(s))
        return result


def subsets(s):
    result = [[]]
    for n in s:
        result.append([n])
    result.append(s)
    for i, n in enumerate(s):
        tmp = []
        for j, m in enumerate(s):
            if i == j:
                continue
            tmp.append(m)
        if tmp not in result:
            result.append(tmp)
    return result


# different algorithm: 151
# not correct: 152
# maybe wrong: 153

exit(0)
print triangle([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
print word_break_two("catsanddog", ["cat", "cats", "and", "sand", "dog"])
print super_ugly_numbers()
print is_reachable([1, 2, 3, 4], 21)
print group_anagrams(["abc", "cba"])
print substr_concat_all_words("barfoothefoobarman", ["foo", "bar"])
print combination_sum([2, 3, 6, 7], 7)
print generate_parentheses(3)
print perfect_squares(13), perfect_squares(12)
print longest_increasing_subsequence([10, 9, 2, 15, 16, 7, 101, 18])
print unique_path(3, 3)
print min_path_sum([[4, 3, 1, 9], [2, 4, 8, 6], [3, 5, 1, 6], [7, 2, 3, 8]])
print max_profit_two([3, 1, 5, 3, 6, 4, 5, 1])
print max_profit([3, 1, 5, 3, 6, 4, 5, 1])
print jump_game_two([2, 3, 1, 1, 4])
print jump_game([2, 3, 1, 1, 4]), jump_game([3, 2, 1, 0, 4])
print house_robber([])
print palindrome_partitioning("aab")
print maximum_product_subarray([2, 3, -2, 4])
print maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print word_break("leetcode", ["leet", "code"])
print edit_distance("a", "b"), edit_distance("abd", "def")
print find_k_pairs_smallest_sums([1, 7, 11], [2, 4, 6], 3)
print is_ugly_two(10)
print is_ugly(14), is_ugly(6), is_ugly(8)
print course_schedule(2, [[1, 0]]), course_schedule(2, [[1, 0], [0, 1]])
print increasing_triplet_subsequence([1, 2, 3, 4, 5]), \
    increasing_triplet_subsequence([5, 4, 3, 2, 1])
print largest_number([3, 30, 34, 5, 9])
print h_index([3, 0, 6, 1, 5])
print first_missing_positive([1, 2, 0, 4])
print find_duplicate_number([1, 2, 2, 3])
print missing_number([0, 1, 3])
print contain_nearby_duplicate([12, 78, 500, 21, 65, 5, 46, 52], 3, 13)
print merge_k_sorted_arrays([[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]])
print meeting_rooms([[0, 30], [5, 10], [15, 20]])
print meeting_rooms_two([[15, 16], [11, 14], [17, 22], [1, 24]]), '\n', \
    meeting_rooms_two([[9, 12], [10, 13], [12, 15], [17, 18], [23, 1]])
print top_k_frequent_elements([3, 1, 1, 2, 3, 1, 2, 3, 4, 2], 3)
print shortest_palindrome("aacecaaa"), \
    shortest_palindrome("abcd")
print remove_invalid_parentheses("()())()")
print is_scramble("great", "rgeat")
print word_pattern("abab", "red blue red blue"), \
    word_pattern("aaaa", "asd asd asd asd"), \
    word_pattern("aabb", "xyz abc xyz abc")
print flip_game_two("-++-++")
print flip_game("+++-+-++-++--+-++")
print get_target_num([1, 2, 3, 4], 21)
print min_window_sub_str("ADOBECODEBANC", "ABC")
print longest_sub_str_2_unique_char("abcbbbbcccbdddadacb")
print longest_sub_str("abcabcbb"), longest_sub_str("bbbbb")
print palindrome_pairs(["bat", "tab", "cat"])
print valid_anagram("ali", "ila"), valid_anagram("ali", "ile")
print largest_rect_histogram([2, 1, 5, 6, 2, 3])
print search_rotated_sorted_array_two([4, 5, 6, 7, 4, 4, 4], 4)
print search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 2)
print guess_number(10 ** 10000)
print search_range([5, 7, 7, 8, 8, 10], 8)
print find_min_rotated_sorted_arr_dup([3, 3, 3, 1, 2, 3, 3])
print find_min_rotated_sorted_arr([4, 5, 6, 7, 0, 1, 2])
words = ["practice", "makes", "perfect", "py", 'makes']
print shortest_word_distance_three(words, "makes", "makes")
print shortest_word_distance(words, "coding", "practice"), "\n", \
    shortest_word_distance(words, "makes", "coding")
print one_edit_distance("ali", "eli"), one_edit_distance("ali", "mhg")
print summary_range([0, 1, 2, 4, 5, 7])
print trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print move_zero([0, 1, 0, 3, 12])
print remove_element([1, 1, 1, 2, 3, 4, 1, 2, 3, 4], 1)
print remove_duplicate_from_sorted_array_two([1, 1, 1, 2, 2, 3, 4, 4, 4, 5])
print remove_duplicate_from_sorted_array([1, 1, 2, 3, 4, 4, 4, 5])
print exercise_1(10)
print insertion_sort([5, 2, 4, 6, 1, 3])
print contains_duplicate_two([1, 2, 5, 1, 4], 2), \
    contains_duplicate_two([1, 2, 1, 7, 5], 2)
print contains_duplicate([1, 2, 3, 4]), contains_duplicate([1, 2, 3, 1])
print triangle([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
print length_last_word("hello my friend     ")
print add_binary_orig("1", "11")
print add_binary("1", "11")
print zig_zag_conversion("PAYPALISHIRING", 3), \
    zig_zag_conversion("PPAYPAASSRIHHSGR", 4)
print is_valid_palindrome("Red rum, sir, is murder"), \
    is_valid_palindrome("Programcreek is awesome")
print longest_consecutive_sequence([100, 4, 200, 1, 3, 2])
x = [1, 3, 5, 6]
print search_insert(x, 5), search_insert(x, 2), search_insert(x, 7), \
    search_insert(x, 0)
print min_size_subarray_sum([2, 3, 1, 2, 4, 3], 17)
print strStr("abcaadfg", "aa"), strStr("abcaadfg", "c")
print longest_valid_parentheses(")()()())")
print is_valid("()[]{}"), is_valid("((({}")
print merge_two_sorted_array([2, 5, 10, 31], [1, 4, 12, 23])
print sum_3_pointer([-1, 0, 1, 2, -1, 4])
print sum_3_closest([-1, 2, 1, 4], 1)
print sum_4([1, 0, -1, 0, -2, 2], 0)
print sum_3([-1, 0, 1, 2, -1, 4])
print atoi("123")


def two_sum():
    x = TwoSum()
    x.add(1)
    x.add(3)
    x.add(5)
    print x.find(4)
    print x.find(7)


two_sum()
print sum_2([2, 7, 11, 15], 9)
print sum_1([2, 7, 11, 15], 9)
print merge_intervals([[1, 6], [4, 7], [9, 14], [13, 18], [8, 10]])
print regexp_match("aab", "c*a*b")
print candy([3, 2, 6, 1, 2, 7, 8, 1])
print find_kth_largest_elm([4, 1, 5, 3, 34, 2, 55], 2)
print insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 9])
print find_median_sorted_array([1, 2, 3, 4], [5, 6, 7, 8])
print word_ladder_1("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
print word_ladder_1("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
print is_isomorphic_string("egg", "add"), is_isomorphic_string("foo", "bar")
print eval_reverse_polish_notation(["2", "1", "+", "3", "*"])
print reverse_words_string("Hello My Friend")
print rotate_array(3, [1, 2, 3, 4, 5, 6, 7])

# not solved:

# problems:
# 12 14 21 22 38 40 45 46 54 55 71 78 82 83 85 90 91 100 101 102 105 106 107 110
# 113 114 119 120 121 122 123 130 132 133 134 135 137 138 139 140 141 143 144
# 145 146 147 148 149 150

# difficult: 23 44 46 60 61 62 63 68 116

# read again: 30 37 43 48 49 50 56 57 59 92 93 108 125 136 142 143

# not important:
# 29 36 42 51 58 70 73 80 84 87 89 94 95 96 97 98 99 104 109 112
# 126 127 128 129

# sort: 88

# different algorithm: 103 115 118 124 131
