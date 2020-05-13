import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def swap(A, i, j):
    if i != j:
        A[i], A[j] = A[j], A[i]
def quicksort(A, start, end):
    if start >= end:
        return
    pivot = A[end]
    pivotIdx = start
    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx+=1
        yield A
    swap(A,end,pivotIdx)
    yield A
    yield from quicksort(A, start, pivotIdx-1)
    yield from quicksort(A, pivotIdx+1, end)

#sort using quick sort
A = np.random.randint(low=1, high=1000, size=1000)

generator = quicksort(A,0,len(A)-1)
fig,ax = plt.subplots()
ax.set_title("bottom text")
bar_rects = ax.bar(range(len(A)), A, align="edge")

text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

iteration = [0]
def update_fig(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text("# of operations: {}".format(iteration[0]))

anim = animation.FuncAnimation(fig, func=update_fig,
    fargs=(bar_rects, iteration), frames=generator, interval=1,
    repeat=False)
plt.show()
