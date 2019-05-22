def prost_in_new(list, list_new=[], i=0):
    if i==len(list)-1:
        return list_new
    for p in range (2, list[i]):
        if list[i]%p==0:
            return prost_in_new(list,list_new, i+1)
            break
        else:
            p+=1
    else:
        list_new.append(list[i])
        return prost_in_new(list,list_new, i+1)





list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("Ваш массив:", list, "\n")
print("\n")

list_new=prost_in_new(list)
print("Простые числа в Вашем массиве: ", end=" ")
print(*list_new)
