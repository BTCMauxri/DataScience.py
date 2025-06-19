from matplotlib import pyplot as plt

# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]    # x - axis

dev_y = [38496, 42000, 46752, 49320, 53200,             # y - axis
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x, dev_y, 'k--', label = 'All Devs')                      # (x-axis, y-axis)

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,             #y-axis
            65998, 70003, 70000, 71496, 75370, 83640]

plt.plot(ages_x, py_dev_y, 'b', label = 'Python')

plt.xlabel('Ages')                           # x-label name
plt.ylabel('Median Salary (USD)')            # y-label name
plt.title('Median Salary (USD) by Age')      # Sets title for the plot

plt.legend()    # no arguments required since I defined kabels when plotting

plt.show()                                  # Display the plot

# Median Python Developer Salaries by Age
##py_dev_y = [45372, 48876, 53850, 57287, 63016,             #y-axis
            #65998, 70003, 70000, 71496, 75370, 83640]

# Median JavaScript Developer Salaries by Age
#js_dev_y = [37810, 43515, 46823, 49293, 53437,
            #56373, 62375, 66674, 68745, 68746, 74583]

# Ages 18 to 55
#ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          #36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

