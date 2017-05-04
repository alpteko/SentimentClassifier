import learn_probabilities as lp
from math import log
p_total = 0
n_total = 0


def classify_no_smooth(review):
    global p_total
    global n_total
    p_neg = 1
    p_pos = 1
    total = 0
    p_zero = 0
    n_zero = 0
    for word in review:
        if word in lp.pos_probability:
            p_count = lp.pos_probability[word]
        else:
            p_count = 0
            p_zero = 1
        if word in lp.neg_probability:
            n_count = lp.neg_probability[word]
        else:
            n_count = 0
            n_zero = 1
        if p_count == 0:
            p_zero = 1
        if n_count == 0:
            n_zero = 1
        if n_zero + p_zero == 0:
            p_pos += log(p_count)
            p_pos -= log(p_total)
            p_neg += log(n_count)
            p_neg -= log(n_total)
            total += log(p_count)
            total -= log(p_total)
            total -= log(n_count)
            total += log(n_total)
    if p_zero is 1 and n_zero is 1:
        return 0
    elif p_zero is 1:
        return -1
    elif n_zero is 1:
        return 1
    else:
        if total > 0:
            return 1
        else:
            return -1


def classify_with_smooth(review):
    global p_total
    global n_total
    d_size = len(lp.general_dictionary)
    total = 0
    for word in review:
        if word in lp.pos_probability:
            p_count = lp.pos_probability[word]
        else:
            p_count = 0
        if word in lp.neg_probability:
            n_count = lp.neg_probability[word]
        else:
            n_count = 0
        total += log(p_count + 1)
        total -= log(p_total + d_size)
        total -= log(n_count + 1)
        total += log(n_total + d_size)
    if total > 0:
        return 1
    else:
        return -1