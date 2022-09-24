n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

def solution(n, arr1, arr2):
    answer = []
    result = ""
    map1,map2 = [],[]
    for i in arr1:
        bin_arr = bin(i)[2:]
        for cnt in range(n):
            if len(bin_arr)<n:
                bin_arr = '0'+bin_arr
        bin_arr = bin_arr.replace('0'," ")
        bin_arr = bin_arr.replace('1',"#")
        map1.append(bin_arr)

    for j in arr2:
        bin_arr = bin(j)[2:]
        for cnt in range(n):
            if len(bin_arr)<n:
                bin_arr = '0'+bin_arr
        bin_arr = bin_arr.replace('0'," ")
        bin_arr = bin_arr.replace('1',"#")
        map2.append(bin_arr)
#결과값 구현 
    for i in range(len(map1)):
        for j in range(len(map2)):
            if map1[i][j] == "#" or map2[i][j] =="#":
                result+="#"
            else:
                result+=" "
        answer.append(result)
        result = ""
    print(answer)
    return answer

solution(n,arr1,arr2)