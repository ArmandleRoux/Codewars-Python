def str_to_cam(s):
    for i in range(len(s)):
        if s[i] == "_" or s[i] == "-":
            s = s[0:i+1] + s[i+1].upper() + s[i+2:]
    s = s.replace("_", "")
    return s.replace("-", "")


print(str_to_cam("A_pippi-is-Pippi"))


