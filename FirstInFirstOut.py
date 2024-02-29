def fifo(arr,maxf):
  '''
  Input: arr: Array of references string, maxf: maximum page table size
  Operation: Read the string array and add it to page table,
            perform page replacement in fifo queue order,
            print out the visual stages 
  Output: farr: faults array
  '''
  t=[]
  fault=0
  farr=[]
  count=0
  print("\nFirst In First Out")
  for i in arr:
    if i not in t:
      if len(t)<maxf:
        t.append(i)
        print(i,"table:",t)
        fault=fault+1
        count=count+1
        farr.append(count)
      else:
        t.pop(0)
        t.append(i)
        print(i,"table:",t)
        fault=fault+1
        count=count+1
        farr.append(count)
    else:
        print(i)
        farr.append(count)
  return farr