def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one  of the numbers 'a' and 'b' is negative".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    if (a > 0 and b<0 )or (a<0 and b>0):
        m = True
    if (a < 0 and b < 0) or (a > 0 and b > 0) :
      m = False
    return m
print(main(4,1))