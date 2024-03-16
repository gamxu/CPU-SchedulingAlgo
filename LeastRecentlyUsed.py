def getMostNotUse(pTable,strArr):
  '''
  Input: pTable: page table array, maxf: Array of references string
  Operation: find the most not used string
  Output: victim: victim string which will be replace
  '''
  maxCount=0
  victim=0
  for i in pTable:
    ctn=0
    for j in strArr[::-1]:
      if j!=i:
        ctn=ctn+1
      else:
        break
    if ctn>=maxCount:
      maxCount=ctn
      victim=i
  return victim


def lru(arr,maxf):
  '''
  Input: arr: Array of references string, maxf: maximum page table size
  Operation: Read the string array and add it to page table,
            perform page replacement using the most not used time,
            print out the visual stages 
  Output: farr: faults array
  '''
  t=[]
  fault=0
  farr=[]
  print("\nLeast Recently Used")
  for i in range(len(arr)):
    if arr[i] not in t:
      if len(t)<maxf:
        t.append(arr[i])
        print(arr[i],"table:",t)
        fault=fault+1
        farr.append(fault)
      else:
        currStr=arr[:i+1]
        vIdx=t.index(getMostNotUse(t,currStr))
        t.pop(vIdx)
        t.append(arr[i])
        print(arr[i],"table:",t)
        fault=fault+1
        farr.append(fault)
    else:
      print(arr[i])
      farr.append(fault)

  return farr