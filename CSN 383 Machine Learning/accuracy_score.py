f = open("./final_result.txt",'r')
g = open("./gt.txt")
lf = f.readlines()
lg = g.readlines()
count = 0
for i in range(1,16256):
  sf = lf[i-1].split(',')
  sg = lg[i-1].split(',')
  #print(sf[1][0:len(sf[1])-1].lower(),sg[1])
  if sf[1][0:len(sf[1])-1].lower() == sg[1].lower():
    count += 1


print "Number of images correctly predicted are ",count
print "Total Number of images are ",i

accuracy = (float(count)/float(i))*100

print "Accuracy is ", accuracy
