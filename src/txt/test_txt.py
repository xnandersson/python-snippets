""" https://www.w3resource.com/python/python-bytes.php """

def write_unicode():
    with open('unicode.txt', 'w') as f:
        f.write("Col1\tCol2\tCol3\n")
        f.write(r"Col1\tCol2\tCol3\n")
        f.write(u"Col1\tCol2\tCol3\n")
        f.write("Swedish characters åäöÅÄÖ\n")

def write_binary():
    with open('binary.txt', 'wb') as f:
        f.write(b"Col1\tCol2\tCol3\n")
        f.write("Swedish Characters åäöÅÄÖ\n".encode('utf-8'))


def read_unicode():
    with open('unicode.txt') as f:
        for row in f:
            print(row, end="")

if __name__ == '__main__':
    write_unicode()
    write_binary()
    read_unicode()
