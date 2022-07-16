from twttr import shorten

#def main():
#    test_twttr()

def test_shorten ():
    assert shorten("twitter") == "twttr"
    assert shorten("Twitter") == "Twttr"
    assert shorten ("What's your name?")=="Wht's yr nm?"
    assert shorten("CS50")=="CS50"
    assert shorten("IOta")=="t"
    assert shorten("TWITTER")=="TWTTR"


#if __name__ == "__main__":
#    main()

# submitted