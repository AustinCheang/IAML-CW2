##########################################################
#  Python module template for helper functions of your own (IAML Level 10)
#  Note that:
#  - Those helper functions of your own for Questions 1, 2, and 3 should be defined in this file.
#  - You can decide function names by yourself.
#  - You do not need to include this header in your submission.
##########################################################
import pandas as pd 
import numpy as np
import scipy

def split_classes(Xtrn, Ytrn):
    Xtrn_classes = pd.DataFrame(Xtrn) 
    Xtrn_classes['class'] = Ytrn
    return Xtrn_classes

def i_class(Xtrn_classes, Ytrn):
    classes = []
    for i in range(len(set(Ytrn))):
        classes.append(Xtrn_classes[Xtrn_classes['class'] ==i])
    return classes

def classes_mean(classes, Ytrn):
    class_mean = []
    for i in range(len(set(Ytrn))):
        class_mean.append(np.mean(classes[i].iloc[:,:-1], axis = 0))
    return class_mean

def find_all_distance(class_data, means):
    distances = []
    distance = {}
    for i in range(len(class_data)):
        temp = {}
        for j in range(len(class_data[i])):
            val = scipy.spatial.distance.euclidean(class_data[i].iloc[j,:-1], means[i])
            distance[j] = val
        temp = {k: v for k, v in sorted(distance.items(), key=lambda item: item[1])}
#         print(i, "is added")
        distances.append(temp)
    return distances

def get_closest_furthest(distance):
    distance = list(distance.keys())
    required = []
    close_1 = distance[0]
    close_2 = distance[1]
    further_2 = distance[-2]
    further_1 = distance[-1]
    required.append(close_1)
    required.append(close_2)
    required.append(further_2)
    required.append(further_1)
    return required