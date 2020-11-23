from matplotlib import pyplot as plt

plt.style.use("ggplot")


slices = [40,30,20,10]
labels = ["forty", "thirty", "twenty", "ten"]
colors = ["red", "blue", "green", "orange"]
explode = [0, 0, 0, 0.1]

plt.title("MY PIE CHART")

plt.pie(slices, labels=labels, colors=colors, explode=explode, shadow=True, autopct="%1.1f%%")

plt.savefig('pie.png')
plt.show()