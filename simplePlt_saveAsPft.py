import matplotlib.pyplot as plt

plt.xlabel('x') 
plt.ylabel('y')


plt.scatter(darray)
## plt.hist(darray,bins=100)

# plt.show()                                                

plt.savefig("question_2_plot.pdf",bbox_inches='tight')                      # Save the plot as a pdf named '