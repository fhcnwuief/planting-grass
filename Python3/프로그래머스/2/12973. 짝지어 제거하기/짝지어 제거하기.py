def solution(s):
    st = []
    for i in range(len(s)):
        if not st:
            st.append(s[i])
        else:
            if (s[i] == st[-1]):
                st.pop()
            else:
                st.append(s[i])
    return 0 if st else 1