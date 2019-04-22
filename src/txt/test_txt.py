with open('unicode.txt', 'w') as f:
    f.write("Col1\tCol2\tCol3\n")
    f.write(r"Col1\tCol2\tCol3\n")
    f.write(u"Col1\tCol2\tCol3\n")
    f.write("Swedish characters åäöÅÄÖ\n")

with open('binary.txt', 'wb') as f:
    f.write(b"Col1\tCol2\tCol3\n")
    f.write("Swedish Characters åäöÅÄÖ\n".encode('utf-8'))
