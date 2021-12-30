from subprocess import check_output
p = check_output(['node', '~/hello.js filepath theme'])
print (p)