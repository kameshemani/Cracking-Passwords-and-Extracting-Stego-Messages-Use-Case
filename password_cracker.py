
import itertools
import md5

#opening a file store password dict of lowercase characters of size 5
""" ref url : https://docs.python.org/2/library/itertools.html
i have used itertools.product command from above url content"""
f = open('password_dict.txt','w+')
password_list = itertools.product('trolpaqweyuisdfghjkzxcvbnm',repeat=5) 
for i in password_list:
    """ ref url : https://teamtreehouse.com/community/join-list-python-27-vs-30
                             I have used ().join command from above url content"""
    f.write(''.join(i) + '\n')
f.close()
md5_hash = raw_input("enter md5 hash tag!!")

#code for finding password by comparing elements in password dict for md5 match
""" ref url: https://docs.python.org/2/reference/compound_stmts.html#try
                 i have used try finally commands from above url content"""
try:
    f1 = open('password_dict.txt','r')

#checking for md5 match
    for password in f1:
        md5_match = md5.new(password.strip()).hexdigest()
        print " on the way but %s =======>>> did not match" %password

        if md5_hash == md5_match:
            print "match found and passowrd is ==>>    %s" %password
            break
finally:
    if md5_hash == md5_match:
        print "done the task"
    else:
        print "No match found for the hash tag from given password_dict file"
        quit()
