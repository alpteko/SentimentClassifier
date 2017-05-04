from learn_probabilities import traverse_files, complete_general_dictionary, tokenize
import os
from classifier import  classify_with_smooth,classify_no_smooth
import classifier

path_to_train_neg = "/data/train/neg"
path_to_train_pos = "/data/train/pos"
path_to_test_pos = "/data/test/pos"
path_to_test_neg = "/data/test/neg"
current_dir = os.getcwd()
########################
data_dir = current_dir + path_to_train_neg
classifier.n_total = traverse_files(data_dir, 0)
########################
data_dir = current_dir + path_to_train_pos
classifier.p_total = traverse_files(data_dir, 1)
########################
data_dir = current_dir + path_to_test_neg
complete_general_dictionary(data_dir)
########################
data_dir = current_dir + path_to_test_pos
complete_general_dictionary(data_dir)
########################
data_dir = current_dir + path_to_test_neg



neg_data_dir = current_dir + path_to_test_neg;
pos_data_dir = current_dir + path_to_test_pos;
list_of_dir = [neg_data_dir,pos_data_dir];

pos_tp, pos_fp, pos_fn, pos_tn = 1, 1, 1, 1
neg_tp, neg_fp, neg_fn, neg_tn = 1, 1, 1, 1

real = -1;
for data_dir in list_of_dir:
    for file in os.listdir(data_dir):
        if file.endswith(".txt"):
            f = open(data_dir+'/' + file).read()
            cl = classify_no_smooth(tokenize(f))
            if real == -1:
                if real == cl:
                    neg_tp += 1
                elif real * -1 == cl:
                    neg_fp += 1
            else:
                if real == cl:
                    neg_tn += 1
                elif real * -1 == cl:
                    neg_fn += 1
    real = 1;


real = -1;
for data_dir in list_of_dir:
    for file in os.listdir(data_dir):
        if file.endswith(".txt"):
            f = open(data_dir+'/' + file).read()
            cl = classify_no_smooth(tokenize(f))
            if real == 1:
                if real == cl:
                    pos_tp += 1
                elif real * -1 == cl:
                    pos_fp += 1
            else:
                if real == cl:
                    pos_tn += 1
                elif real * -1 == cl:
                    pos_fn += 1
    real = 1;

pos_precision = pos_tp / (pos_tp + pos_fp)
pos_recall = pos_tp / (pos_tp + pos_fn)
pos_f_measure = 2*pos_precision*pos_recall / (pos_precision + pos_recall)
print("-------SMOOTHING DISABLED--------------")
print(" ==== Positive Class ======")
print("Precision : " + str(pos_precision))
print("Recall    : " + str(pos_recall))
print("F_measure : " + str(pos_f_measure))
print("==========================")


neg_precision = neg_tp / (neg_tp + neg_fp)
neg_recall = neg_tp / (neg_tp + neg_fn)
neg_f_measure = 2*neg_precision*neg_recall / (neg_precision + neg_recall)
print("==== Negative Class ======")
print("Precision : " + str(neg_precision))
print("Recall    : " + str(neg_recall))
print("F_measure : " + str(neg_f_measure))
print("==========================")
print("==========================")
print(" ==== Results ======")
macroaveraged_precision = (pos_precision + neg_precision) / 2
print('macroaveraged precision ' + str(macroaveraged_precision))
microaveraged_precision = (pos_tp + neg_tp) / (pos_tp + neg_tp + pos_fp + neg_fp)
print('microaveraged precision ' + str(microaveraged_precision))
print("==========================")
pos_tp, pos_fp, pos_fn, pos_tn = 0, 0, 0, 0
neg_tp, neg_fp, neg_fn, neg_tn = 0, 0, 0, 0

real = -1;
for data_dir in list_of_dir:
    for file in os.listdir(data_dir):
        if file.endswith(".txt"):
            f = open(data_dir+'/' + file).read()
            cl = classify_with_smooth(tokenize(f))
            if real == -1:
                if real == cl:
                    neg_tp += 1
                else:
                    neg_fp += 1
            else:
                if real == cl:
                    neg_tn += 1
                else:
                    neg_fn += 1
    real = 1;


real = -1;
for data_dir in list_of_dir:
    for file in os.listdir(data_dir):
        if file.endswith(".txt"):
            f = open(data_dir+'/' + file).read()
            cl = classify_with_smooth(tokenize(f))
            if real == 1:
                if real == cl:
                    pos_tp += 1
                else:
                    pos_fp += 1
            else:
                if real == cl:
                    pos_tn += 1
                else:
                    pos_fn += 1
    real = 1;

pos_precision = pos_tp / (pos_tp + pos_fp)
pos_recall = pos_tp / (pos_tp + pos_fn)
pos_f_measure = 2*pos_precision*pos_recall / (pos_precision + pos_recall)
print("-------SMOOTHING ENABLED--------------")
print(" ==== Positive Class ======")
print("Precision : " + str(pos_precision))
print("Recall    : " + str(pos_recall))
print("F_measure : " + str(pos_f_measure))
print("==========================")


neg_precision = neg_tp / (neg_tp + neg_fp)
neg_recall = neg_tp / (neg_tp + neg_fn)
neg_f_measure = 2*neg_precision*neg_recall / (neg_precision + neg_recall)
print("==== Negative Class ======")
print("Precision : " + str(neg_precision))
print("Recall    : " + str(neg_recall))
print("F_measure : " + str(neg_f_measure))
print("==========================")
print("==========================")
print(" ==== Results ======")
macroaveraged_precision = (pos_precision + neg_precision) / 2
print('macroaveraged precision ' + str(macroaveraged_precision))
microaveraged_precision = (pos_tp + neg_tp) / (pos_tp + neg_tp + pos_fp + neg_fp)
print('microaveraged precision ' + str(microaveraged_precision))
print("==========================")
