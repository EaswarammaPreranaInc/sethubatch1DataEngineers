# Slice  demo  program
# 0      1       2        3      4       5       6       7
# R      a       m       a                R       a       o
# -8    -7      -6      -5     -4      -3     -2      -1
a = 'Rama Rao'
print(a[:7:2])
# [0:7:2] indexes from 0 to 6 in steps of 2
# '0 2 4 6'
# 'R m    a'
print(a[:7]) 
# [0:7:1] indexes from 0 to 7 in steps of 1
# Rama Rao
print(a[2:4])
#indexes from 2 to 3 in steps of 1
#ma
print(a[6:2])
# indexes fron 6 to 1 
