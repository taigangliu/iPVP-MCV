import numpy as np
from sklearn.metrics import roc_auc_score,roc_curve,accuracy_score,confusion_matrix

AACindproy = np.loadtxt("data/NEW-10fold-PVP-final-AAC-probas_y.csv",delimiter=",")[:,1]
PRTindproy = np.loadtxt("data/NEW-10fold-PVP-final-PRT-probas_y.csv",delimiter=",")[:,1]
DPindproy = np.loadtxt("data/NEW-10fold-PVP-final-DP-lag4-probas_y.csv",delimiter=",")[:,1]

AACindprey = np.loadtxt("data/NEW-10fold-PVP-final-AAC-predict_y.csv",delimiter=",")
PRTindprey = np.loadtxt("data/NEW-10fold-PVP-final-PRT-predict_y.csv",delimiter=",")
DPindpre = np.loadtxt("data/NEW-10fold-PVP-final-DP-lag4-predict_y.csv",delimiter=",")

Combindprey=AACindprey+PRTindprey+DPindpre

result=[]
for i in range(Combindprey.shape[0]):
    if Combindprey[i]>0:
        result.append(1)
    else :
        result.append(-1)

indtesty = np.loadtxt("data/NEW-10fold-PVP-final-AAC-test_y.csv",delimiter=",")
print("10-fold-ACC：{}".format(accuracy_score(indtesty,result)))
#
confusion = confusion_matrix(indtesty, result)
TP = confusion[1, 1]
TN = confusion[0, 0]
FP = confusion[0, 1]
FN = confusion[1, 0]

print("SP:{}".format(TN / (TN + FP)))
print("SN:{}".format(TP / (TP + FN)))
n = (TP * TN - FP * FN) / (((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)) ** 0.5)
print("PRE:{}".format(TP / (TP + FP)))
print("MCC:{}".format(n))
print("F-score:{}".format((2 * TP) / (2 * TP + FP + FN)))
print("ACC:{}".format((TP + TN) / (TP + FP + TN + FN)))
