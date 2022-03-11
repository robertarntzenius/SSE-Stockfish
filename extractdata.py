#!/bin/python3
import sys
import math
import matplotlib.pyplot as plt

# ./extractdata.py `cat energy.data | grep "Joules"| awk '{print $1}' | sed 's/\.//' | sed 's/,/\./'`

N = 30
VERSIONS = 13

#totals = [0] * VERSIONS
#stddev = [0] * VERSIONS

#for i in range(1, len(sys.argv)):
#	totals[(i-1) % VERSIONS] += float(sys.argv[i])

#for i in range(1, len(sys.argv)):
#	totals[(i-1) % VERSIONS] += float(sys.argv[i])

#for i in range(1, len(sys.argv)):
#	val = float(sys.argv[i])
#	avg = totals[(i-1) % VERSIONS] / N;
#	stddev[(i-1) % VERSIONS] += (val - avg) * (val - avg)

#for i in range(len(stddev)):
#	stddev[i] = math.sqrt( stddev[i] / ( N - 1 ) )

#for i in range(len(totals)):
#	if i+1 < 3:
#		print("Version", i + 1 , ":" , totals[i] / N , ", stddev: ", stddev[i])
#	else:
#		print("Version", i + 2 , ":" , totals[i] / N , ", stddev: ", stddev[i])


# Plot for version 12 tot 14

#data = [[0] * N] * (3)
#
#fig, ax = plt.subplots()
#
#for i in range(3):
#	data[i] = [0] * N
#	for j in range(N):
#		data[i][j] = float(sys.argv[(j*VERSIONS)+i+VERSIONS-3+1])
#
#ax.boxplot(data, vert=False)
#ax.violinplot(data, vert=False, widths=1.9)
#
#plt.yticks([1,2,3],["12","13","14"])

# Plot for version 1 tot 11

data = [[0] * N] * (VERSIONS - 3)

fig, ax = plt.subplots()

for i in range(VERSIONS - 3):
	data[i] = [0] * N
	for j in range(N):
		data[i][j] = float(sys.argv[(j*VERSIONS)+i+1])

ax.boxplot(data, vert=False)
ax.violinplot(data, vert=False, widths=1.9)

plt.yticks([1,2,3,4,5,6,7,8,9,10],["1","2","4","5","6","7","8","9","10","11"])

# Plot for version 1 tot 14

#data = [[0] * N] * (VERSIONS)
#
#fig, ax = plt.subplots()
#
#for i in range(VERSIONS):
#	data[i] = [0] * N
#	for j in range(N):
#		data[i][j] = float(sys.argv[(j*VERSIONS)+i+1])
#
#ax.boxplot(data, vert=False)
#ax.violinplot(data, vert=False, widths=1.9)
#
#plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13],["1","2","4","5","6","7","8","9","10","11","12","13","14"])

plt.grid(axis='y', linestyle='-')

plt.xlabel('Energy consumption (J)')
plt.ylabel('Stockfish version')
plt.show()

