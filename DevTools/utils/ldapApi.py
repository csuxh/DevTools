# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 15:35
# @Author  : 
import ldap3

def check_login(user, password):
    ldaphost = ('ldaps://xxx:636')
    dn = u'CN={},OU=Users,OU=CN,DC=hcg,DC=xxx,DC=net'.format(user)
    conn = ldap3.Connection(ldap3.Server(ldaphost), user=dn, password=password, check_names=True, lazy=False, raise_exceptions=False)
    conn.bind()
    if conn.result['description'] == 'success':
        print('login success')
        # print(conn)
        return True
        # print((True, attr_dict['mail'], attr_dict['sAMAccountName'], attr_dict['givenName']))
    else:
        print('login failed')
        return False


if __name__ == '__main__':
    check_login('xxx', 'xxx')
    # ldaphost = ('xxx')
    #
    # passwd = 'xxx'
    # bind_dn = 'CN=xxx,OU=Local Service,OU=CN,DC=xxx,DC=xxx'
    # conn = ldap3.Connection(ldap3.Server(ldaphost), bind_dn, passwd, auto_bind=True)
    # # search_filter = '(cn={})'.format(groupname)
    # search_filter = '(sAMAccountName=xxx)'
    # search_base = 'OU=Users,OU=CN,DC=xxx,DC=xxxxxx,DC=net'
    # res = conn.search(search_base=search_base, search_filter=search_filter, search_scope=ldap3.SUBTREE,attributes=ldap3.ALL_ATTRIBUTES)
    #
    # if res:
    #     entry = conn.response[0]
    #     dn = entry['dn']
    #     attr_dict = entry['attributes']
    #     try:
    #         conn2 = ldap3.Connection(ldap3.Server(ldaphost), user=dn, password='xxx', check_names=True, lazy=False, raise_exceptions=False)
    #         conn2.bind()
    #         if conn2.result["description"] == "success":
    #             print((True, attr_dict["mail"], attr_dict["sAMAccountName"], attr_dict["givenName"]))
    #         else:
    #             print("auth fail")
    #     except Exception as e:
    #         print("auth fail")
