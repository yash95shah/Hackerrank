def rotLeft(a, d):
    temp_array = []
    final_array = []
    j =0
    #pointer = temp_array[j]
    for k in range(a):
        temp_array.append(k+1)
    if a == d:
        final_array = temp_array
    else:
        temp2 = 0
        temp1 = 0
        for j in range(d):
            for i in range(a):
                if i == 0:
                    temp2 = temp_array[i]
                    temp1 = temp_array[i]
                else:
                    temp1 = temp_array[i]
                    if i != a-1:
                        temp_array[i-1] = temp_array [i]
                    else:
                        temp_array[i-1] = temp_array [i]
                        temp_array[i] = temp2
    return temp_array



print rotLeft(5,4)
