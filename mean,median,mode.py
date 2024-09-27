import statistics
lst=[16,18,27,16,23,21,19]
mean=sum(lst)/len(lst)
median=statistics.median(lst)
mode=statistics.mode(lst)
print("mean:",mean)
print("median:",median)
print("mode:",mode)
