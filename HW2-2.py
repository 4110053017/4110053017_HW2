# 2. Let's measure the degree of overlapping subproblem.
# Calculate the times are F(4) computed when we compute
# F(5),F(6),.....,F(50). Plot the results into line chart.

import matplotlib.pyplot as plt

def f_top_down(n):
    if n == 4 or n == 5:
        return 1
    else:
        return f_top_down(n - 1) + f_top_down(n - 2)

top_d = []  # overlapping subproblem of top_down

for i in range(4, 51):
    top_d.append(f_top_down(i))

    if i % 5 == 4 and i != 4:
        print("* ", end="")
    if i % 5 != 4:
        print("*", end="")

x = []
for i in range(4, 51):
    x.append(i)

print("\n\n""Degree of overlapping subproblem:")
for i in range(4, 51):
    print(str(i) + " " + str(top_d[i-4]) + "(degree)")

plt.plot(x, top_d, 'ro-')
plt.title('Degree of overlapping subproblem of top-down method')
plt.xlabel('number of Fibonacci ')
plt.ylabel('overlapping subproblem')
plt.legend(loc='upper left')
plt.show()
