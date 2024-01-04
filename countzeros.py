def count_zeros(start,end):
    count=0
    for num in range(start,end+1):
        if num==0:
            count +=1
        return count
start=1
end=1000
zeros_count=count_zeros(start,end)

print("number of zeros present in the given array : ",zeros_count)