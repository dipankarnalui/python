name= "alias"
phone= "1234567890"
email="foo@bar.foo"

#Output:
#Hi "alias" your phone number is "1234567890" and your email ID is "foo@bar.foo"


#solution 1
#result = 'Hi "{}" your phone number is {} and your email ID is {} '
#print(result.format(name, phone, email))


#Solution2 for Python 3.6
result=f'Hi "{name}" your phone number is "{phone}" and your email ID is "{email}" '
print(result)

