import matplotlib.pyplot as plt;
import numpy as np
import matplotlib.pyplot as plt
import os.path
import json 

# objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
# y_pos = np.arange(len(objects))
# performance = [10,8,6,4,2,1]

# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Usage')
# plt.title('Programming language usage')
# # plt.show()
# plt.savefig('chart.png')

oldResult = {}

if os.path.isfile("results/microsoft-vscode.json"):
        with open("results/microsoft-vscode.json","r") as outfile:
            oldResult = json.loads(outfile.read())

# print(oldResult)

sortedLabels = sorted(oldResult['labels'].items(), key = 
             lambda kv:(kv[1], kv[0]))
reversed = sortedLabels[::-1]
reversed = reversed[:5]
# print(reversed[:10])

y_pos = np.arange(len(reversed))
performance = [reversed[i][1] for i in range (0, len(reversed))]
print(performance)
plt.rc('xtick',labelsize=8)
# plt.figure(figsize=(20, 20))
plt.bar(y_pos, performance, align='edge', alpha=0.5, width=0.3)
plt.xticks(y_pos, (reversed[i][0] for i in range (0, len(reversed))))
plt.ylabel('Usage')
plt.title('Most labels used for first commits')
# # plt.show()
plt.savefig('chart2.png')