def create(s):
    if len(s) == 1 or len(s) == 0:
        taulukko = []
        taulukko[:0] = s
        return taulukko
    else:
        taulukko = []
        for i in range(len(s)):
            ensimmainen = s[i]
            loput = s[:i] + s[i+1:]
            anagrammit = create(loput)
            for j in anagrammit:
                taulukko.append(ensimmainen + j)

        res = [*set(taulukko)]
        return sorted(res)

if __name__ == "__main__":
    print(create("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create("aaaaa")) # ['aaaaa']
    print(create("abab")) # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    print(len(create("aybabtu"))) # 1260