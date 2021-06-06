def isUnique(list):
    char = []
    for x in list:
        if char.count(x) > 0:
            return False
        else:
            char.append(x)
    return True


# Time complexity:O(n)
def urlify(s):
    temp = []
    for x in s:
        if x.isspace():
            temp.append("%20")
        else:
            temp.append(x)
    string = "".join(temp)
    return string


def check_permutation(s1, s2):
    temp = []
    if len(s2) > len(s1):
        return False
    else:
        for x in s1:
            temp.append(x)

        for i in s2:
            if temp.count(i) == 0:
                return False
        return True


def pal_per(string):
    temp = []
    for x in string:
        if temp.count(x) > 0:
            temp.remove(x)
        else:
            temp.append(x)
    if len(temp) == 1:
        return True
    else:
        return False


def oneAway(s1, s2):
    temp = []
    for x in s1:
        temp.append(x)
    for i in s2:
        if temp.count(i) > 0:
            temp.remove(i)

    if len(temp) == 1:
        return True
    else:
        return False


def string_compression(string):
    s1 = []
    s2 = []
    character = ""
    for x in string:
        s1.append(x)
    for i in string:
        if s2.count(i) < 1:
            s2.append(i)
    if len(s1) == len(s2):
        string = "".join(s2)
        return string

    for z in s2:
        c = s1.count(z)
        character = character + z + str(c)
    return character


def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    print(matrix)

def zero(m):
    for i in range(len(m)):
        j = 0
        while j<len(m):
            m[i][j] = 0
            j+=1
    print(m)

def zero_matrix(m):
    for i in range(len(m)):
        j = 0
    while j<len(m):
        if m[i][j] ==0:
            zero(m)
            return
        else:
            j+=1
    print(m)

def isSubstring(s1,s2):
    string1 = len(s1)
    string2 = len(s2)
    if string1 !=string2:
        return False
    temp = s1 + s2
    bho = temp.count(s2)
    print(temp.count(s2))
    if temp.count(s2)>0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(isSubstring("waterbottle","erbottlewat"))

