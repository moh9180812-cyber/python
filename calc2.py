def get_int (p):
    while (True) :
        try :
            return int(input (p))
        except :
            pass
def main ():
    x = get_int ("x :")
    y = get_int ("y :")
    print(x+y)
main()
