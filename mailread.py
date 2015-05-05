import email

with open('2015-April.txt.gz', 'r') as fp:
    message = email.message_from_file(fp)
print '%r' % (message.items(),)
