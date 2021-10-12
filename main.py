def is_palindrome(n):
    '''
    Verifica daca un numar e palindrom returnand true/false dupa caz.
    n=nr. intreg 

    '''
    x=0
    k=0
    cn=n
    while n>0:
        k=n%10
        x=x*10+k
        n=n//10
    if cn==x:
        return True
    else:
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
    return v//z

def test_get_n_choose_k():
     assert get_n_choose_k(4,3) == 4
     assert get_n_choose_k(5,2) == 10
     assert get_n_choose_k(6,2) == 15
     assert get_n_choose_k(4,4) == 1
     

def is_superprime(n):
    '''
    Verifica daca un numar si toate prefixele sale sunt numere prime si returneaza True/False dupa caz.
    n-numar intreg
    '''
    if n<2:
        return False
    else:
     while n>1:
        if n<2:
            return False
        for i in range(2,n):
            if n%i == 0:
                return False
        n=n//10
    return True

def test_is_superprime():
    assert is_superprime(233) == True
    assert is_superprime(237) == False
    assert is_superprime(24) == False
    assert is_superprime(17) == True



def main():
    while True:
        print("1.Verificati daca un numar este palindrom")
        print("2.Determinati combinari de n luate cate k")
        print("3.Verificati daca un numar este superprim")
        print("4.Iesire")
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
            n=int(input("Alegeti un numar pentru a verifica daca e superprim: "))
            if is_superprime(n):
                print("Este superprim")
            else:
                print("Nu este superprim")
        elif optiune == '4':
             break


if __name__ == '__main__':
    main()
