import numpy as np
rec = np.array([0.33, 0.33, 0.67])
prec = np.array([1, 0.5, 0.67])
mrec = np.concatenate(([0.], rec, [1.]))
mpre = np.concatenate(([0.], prec, [0.]))
print(mrec, mpre)
# compute the precision envelope
for i in range(mpre.size - 1, 0, -1):
    mpre[i - 1] = np.maximum(mpre[i - 1], mpre[i])
print(mpre)
# to calculate area under PR curve, look for points
# where X axis (recall) changes value
#i = np.where(mrec[1:] != mrec[:-1])[0]
i = np.arange(0, len(mpre) - 1)
print(i)
# and sum (\Delta recall) * prec
ap = np.sum((mrec[i + 1] - mrec[i]) * mpre[i + 1])
print(ap)