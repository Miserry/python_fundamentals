#The whole purpose of this code is to test the calculator.py and tell if we messed up something with the function there.


from calculator import square


def main():
    test_square()


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-4) == 16


if __name__ == "__main__":
    main()

    
#We can even run this with pytest, which i did and it works just fine.
#Doesn't look particularly necessary at this point, but still good to know.
