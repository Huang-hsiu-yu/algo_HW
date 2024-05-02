import matplotlib.pyplot as plt

f_values = [0, 1]
n=[]
for i in range(5, 51):
    f_values.append(f_values[-1] + f_values[-2])
    n.append(i)
    print(f'F({i}) = {f_values[-1]}, Number of Times F(4) is Computed = {f_values[-1]}')



plt.plot(n, f_values[2:], marker='o')
plt.xlabel('n')
plt.ylabel('Number of Times F(4) is Computed')
plt.title('Degree of Overlapping Subproblems')
plt.savefig('Degree_of_Overlapping_Subproblems.png')
plt.show()
