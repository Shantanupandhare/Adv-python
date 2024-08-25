def simple_interst(p,n,r):
    """
    This will calculte simple interest
    """
    I= (p*n*r)/100
    A= p+I
    return I, A

"""
__main__ will refer to current file --> new change for git
"""

if __name__ == "__main__":
    I1,A1 = simple_interst(p=57000,n=5,r= 7.5)
    print(f"Simple Intrest : {I1:.2f}")
    print(f'Amount : {A1:.2f}')
