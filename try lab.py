from re import U
upper_bnumber= int(input("Enter an upper bound number:"))
abundant_count = 0
perfect_count = 0
deficient_count = 0
i=0
while i<upper_bnumber :
  i=i+1
  divisor_sum = 0
  j=1
  while j<i:
    print(divisor_sum)
    if i % j== 0:
        divisor_sum += j
    j=j+1
    
  if(divisor_sum >i):
    #abundant
    abundant_count += 1
  elif (divisor_sum < i):
    deficient_count += 1
  elif (divisor_sum ==i):
    perfect_count += 1
print("Between 1 and",upper_bnumber," there are ", deficient_count, "deficient numbers",perfect_count,"perfect numbers ",abundant_count,"abundant numbers ")
