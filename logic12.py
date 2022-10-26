def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    if a%11==0:
          return True
    else:
        a%11!=0
         
    return False
print(main(22))