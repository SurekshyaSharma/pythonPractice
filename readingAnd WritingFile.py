def read_test():
    f = open("demo.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        print(contents)


def write_test():
    f = open("demo.txt", "a")
    f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et "
            "dolore magna aliqua.Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip "
            "ex ea commodo consequat.Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu "
            "fugiat nulla pariatur.Excepteur sint occaect cupidatat non proident, sunt in culpa qui officia deserunt "
            "mollit anim id est laborum.")
    f.close()

    # open and read the file after the appending:
    f = open("demo.txt", "r")
    print(f.read())


write_test()

# read_test()
