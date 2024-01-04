memory = {}
def count(s):
    n = len(s)
    if n == 0: 
        return 1
    if n % 2 == 1:
        return 0
    elif s in memory:
        return memory[s]
    elif "00" not in s and "11" not in s:
        memory[s] = 0
        return 0
    else:
        result = 0
        for i in range(1, n):
            if s[i] == s[i-1]:
                result += count(s[:i-1]+s[i+1:])
        memory[s] = result
        return result

if __name__ == "__main__":
    print(count("1100")) # 2
    print(count("1001")) # 1
    print(count("100111")) # 5
    print(count("11001")) # 0
    print(count("1100110011100111")) # 113925