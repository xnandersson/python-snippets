import ldap

""" sudo apt-get install devscripts python3-dev libldap2-dev libsasl2-dev """

def run():
    con = ldap.initialize('ldap://127.0.0.1')
    con.protocol_version = ldap.VERSION3
    con.simple_bind_s('cn=admin,dc=openforce,dc=org', 'Secret007!')
    
    entries = con.search_s(
            base="dc=openforce,dc=org",
            scope=ldap.SCOPE_SUBTREE,
            filterstr='(objectClass=*)',
            attrlist=('cn',))

    for entry in entries:
        print(entry)

if __name__ == '__main__':
    run()
