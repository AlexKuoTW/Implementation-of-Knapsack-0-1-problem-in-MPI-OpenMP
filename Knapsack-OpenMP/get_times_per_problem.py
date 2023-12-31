# #!/usr/bin/python

# import sys

# if len(sys.argv) != 2:
#     print ("Usage:", sys.argv[0], "<results_file.csv>")
#     exit(1)

# f = open(sys.argv[1], 'r')

# results = {}

# for line in f:
#    l = line.split()
#    if len(l) == 6:
#        results[(l[0], l[1], l[5])] = l[4]

# f.close()
# f = open(sys.argv[1], 'r')

# print ("Width Items Time1Thread Time2Threads Time3Threads Time4Threads")
# for line in f:
#    line = line.strip('\n')
#    l = line.split()
#    try:
#        if len(l) == 6:
#            if l[5] == '1':
#                print (l[0], l[1], l[4], results[(l[0], l[1], '2')], results[(l[0], l[1], '3')], results[(l[0], l[1], '4')])
#    except:
#        pass

# f.close()

#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print ("Usage:", sys.argv[0], "<results_file.csv>")
    exit(1)

f = open(sys.argv[1], 'r')

results = {}

for line in f:
   l = line.split()
   if len(l) == 6:
       results[(l[0], l[1], l[5])] = l[4]

f.close()
f = open(sys.argv[1], 'r')

print ("Width Items Time1Thread Time2Threads Time3Threads Time4Threads Time5Threads Time6Threads Time7Threads Time8Threads")
for line in f:
   line = line.strip('\n')
   l = line.split()
   try:
       if len(l) == 6:
           if l[5] == '1':
               print (l[0], l[1], l[4], 
                      results.get((l[0], l[1], '2'), 'N/A'), 
                      results.get((l[0], l[1], '3'), 'N/A'), 
                      results.get((l[0], l[1], '4'), 'N/A'),
                      results.get((l[0], l[1], '5'), 'N/A'), 
                      results.get((l[0], l[1], '6'), 'N/A'), 
                      results.get((l[0], l[1], '7'), 'N/A'),
                      results.get((l[0], l[1], '8'), 'N/A'))
   except:
       pass

f.close()
