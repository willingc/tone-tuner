__author__ = 'carol'

import mailbox

print('getting started')

import gzip

import gzip
with gzip.open('2015-April.txt.gz', 'rb') as f:
    file_content = f.read()
    print(file_content)

input_file = gzip.open('2015-April.txt.gz', 'rb')
try:
    print 'Entire file:'
    all_data = input_file.read()
    print all_data

    expected = all_data[5:15]

    # rewind to beginning
    input_file.seek(0)

    # move ahead 5 bytes
    input_file.seek(5)
    print 'Starting at position 5 for 10 bytes:'
    partial = input_file.read(10)
    print partial

    print
    print expected == partial
finally:
    input_file.close()

for message in mailbox.mbox('2015-April.txt.gz'):
    subject = message['subject']       # Could possibly be None.
    if subject and 'python' in subject.lower():
        print(subject)
