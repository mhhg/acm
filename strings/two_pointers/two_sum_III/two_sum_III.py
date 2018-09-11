
class TwoSum(object):
    def __init__(self):
        self.hash_map = dict()

    def add(self, num):
        if num in self.hash_map:
            self.hash_map[num] += 1
        else:
            self.hash_map[num] = 1

    def find(self, num):
        for key, value in self.hash_map.items():
            target = num - key
            if target in self.hash_map:
                if key == target and value < 2:
                    continue
                return True

        return False
