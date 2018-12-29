class AnyIter(object):

    def __init__(self, seq, safe=False):
        self.safe = safe
        self.iter = iter(seq)
        pass

    def __iter__(self):
        return self

    # 该方法用于循环
    def __next__(self, how_many=1):
        result = []
        for eachItem in range(how_many):
            try:
                result.append(self.iter.__next__())
            except StopIteration as e:
                if self.safe:
                    return result
                else:
                    raise e
        return result


anyIter = AnyIter(range(5), True)
# iter()方法等同于调用anyIter的__iter__方法
myIter = iter(anyIter)
myIter.__next__(88)
