import matplotlib
import matplotlib.pyplot as plt
import img_scatter
import numpy

a = numpy.linspace(0, 10, 10)
b = numpy.exp(a)
c = numpy.sinh(a)

matplotlib.style.use("science")
fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111)
ax.set_yscale("log")
ax.scatter_img(x=a, y=b, s=200, marker="o", index=2)
ax.scatter_img(x=a, y=c, s=200, marker="s", index=7)

fig.savefig("one_figure_log.svg")
fig.savefig("one_figure_log.png")
fig.savefig("one_figure_log.pdf")




