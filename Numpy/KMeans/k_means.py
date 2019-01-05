# 导入所有模块
from numpy import *
import operator


# def create_data_set():
#     group = array([1.0, 1.1], [1.0, 1.0], [0, 0], [0, 1])
#     lables = ['A', 'A', 'B', 'B']
#     return group, lables

def classify(index, k):
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 1]])
    lables = ['A', 'A', 'B', 'B']
    dataset_size = group.shape[0]
    diff_mat = tile(index, (dataset_size, 1)) - group
    sq_diff_mat = diff_mat * 2
    sq_distances = sum(sq_diff_mat, axis=1)
    # distances = sqrt(sq_distances)
    # distances = [item**0.5 for item in sq_distances]
    sorted_dist = argsort(sq_distances)
    class_count = {}
    for i in range(k):
        vote_label = lables[sorted_dist[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]


if __name__ == '__main__':
    result = classify([0, 0], 3)
    print(result)
