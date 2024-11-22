import itertools
import numpy as np
import time
import mdtraj as md
import glob

def calculate_bond_distances(xyz_file_path, top_file_path, x, threshold=0.0):
	x = itertools.combinations(range(6), 2)  # all the atom pairs
	traj = md.load_xyz(xyz_file_path, top_file_path)#, top=None, format='xyz')
	distances = 10*md.compute_distances(traj, x)# [[0,1],[0,2]])
	return distances # bonds

# Example usage:
y = itertools.combinations(range(6), 2)  # all the atom pairs

## 把tuple的逗點換成"-"
delim='-' 
x=[]
for i in y:
	print(i)
	#i="-".join(i)
	j = ''.join([str(ele) + delim for ele in i])
	j = j[ : len(j) - len(delim)]
	x.append(j)
##

csv_name=os.getcwd().split("/")[-3]
datafile = open(csv_name+'.csv', 'w+')
datafile.write('filename')

for i in list(x):
	datafile.write(', '+str(i))
datafile.write('\n')

top_file_path = "/storage/home/hcoda1/3/ywang4107/p-jkretchmer3-0/Orlando/2024/LCPBE0.516_aDZ-aDZ_sing-trip_30K/water-dimer_Joseph.mol2"
threshold = 2.5 

files=glob.glob("*_final.xyz")
for ifile in files: 
	bond_len = calculate_bond_distances(ifile, top_file_path, x, threshold)
	datafile.write(ifile.strip("_final.xyz"))
	datafile.write(",")
	np.savetxt(datafile, bond_len, delimiter=",",fmt='%10.3f')
#	datafile.write(str(bond_len))
#	datafile.write('\n')


