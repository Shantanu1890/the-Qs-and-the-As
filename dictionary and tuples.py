lab_value={}
for i in range(0,5):
    testname=input()
    minvalue=float(input())
    maxvalue=float(input())
    lab_value[testname]= (minvalue,maxvalue)
print(lab_value)
#name of test
test=input()
# actual value of test
obs_value=float(input())
#find range of values of the test
rangeval= lab_value[test]

minvalue=rangeval[0]
maxvalue=rangeval[1]
if minvalue<obs_value<maxvalue:
    print("normal")
else:
    print("not normal")
    
