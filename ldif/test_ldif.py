from StringIO import StringIO
import ldif
import re

def run():
    """ ldapsearch -LLL <rest-of-search-params> > data.ldif """

    ldif_file = open("data.ldif")

    """ After cleaning up the file, need to squash multiple empty lines using regexp """

    cleaned_output = re.sub(r'\n\s*\n', '\n\n', ldif_file.read())
    ldif_file = StringIO(cleaned_output)

    parser = ldif.LDIFRecordList(ldif_file)
    parser.parse()

    for dn, entry in parser.all_records:
        try:
            print("{cn}:{password}".format(
                        cn=entry['cn'][0],
                        password=entry['password'][0])
        except KeyError as e:
            pass
