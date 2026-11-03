
def lcs_brute(text1, text2):
    if len(text1) == 0 or len(text2) == 0:
        return 0

    if text1[-1] == text2[-1]:
        return 1 + lcs_brute(text1[:-1], text2[:-1])

    return max(
        lcs_brute(text1[:-1], text2),
        lcs_brute(text1, text2[:-1])
    )


# User input
text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

print("Length of LCS:", lcs_brute(text1, text2))
