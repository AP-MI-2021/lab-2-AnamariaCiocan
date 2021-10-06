def is_palindrome(n):
    '''
    Verifica daca un numar e palindrom returnand true/false dupa caz.
    n=nr. intreg 

    '''
    x=0
    cn=n
    while n!=0:
        x*=10+n%10
        n=n//10
    if cn==x:
        return True
    elif: 
        return False


def test_is_palindrome():
    assert is_palindrome(22) == True
    assert is_palindrome(13) == False
    assert is_palindrome(2) == True
    assert is_palindrome(101) == True
    assert is_palindrome(124) == False

def get_n_choose_k(n, k):
    '''
    Calculeaza si returneaza valoarea expresiei combinari de n luate cate k.
    n,k numere intregi
    
    '''
    x=1
    for i in range(2,n+1):
        x*=i
    y=1
    for i in range(2,k+1):
        y*=i
    z=1
    for i in range(2,n-k+1):
        z*=i
    v=x//y
    return v/z

 def test_get_n_choose_k():
     assert get_n_choose_k(3,4) == 4
     assert get_n_choose_k(2,5) == 10
     assert get_n_choose_k(2,6) == 15
     assert get_n_choose_k(4,4) == 1
     

   

def main():
    while True:
        print("1.Verificati daca un numar este palindrom")
        print("2.Determinati combinari de n luate cate k")
        print("3.Iesire")
        optiune = input("Alegeti optiune: ")
        if optiune == '1':
            n=int(input("Alegeti un numar pentru a verifica daca e palindrom: "))
            if is_palindrome(n):
                print(" este palindrom")
            else:
                print(" nu este palindrom")
        elif optiune == '2':
            n=int(input("combinari de: "))
            k=int(input("luate cate: "))
            print("Rezultatul este: ")
            print(get_n_choose_k(n,k))
        elif optiune == '3':
             break



main()