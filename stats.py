import numpy as np
import matplotlib.pyplot as plt


def save_plot(stats):
    colors = ['green', 'red', 'blue', 'indigo', 'orange']
    num_buckets = 5
    x = np.arange(0, len(stats), 1)*10
    fig = plt.figure(figsize=(8, 6))
    ax = plt.subplot(111)
    ax.set_ylim(0, 1)
    for i in range(num_buckets):
        ax.plot(x, stats[:, i, 0], color=colors[i])
        ax.fill_between(x, stats[:, i, 0] - stats[:, i, 1], stats[:, i, 0] + stats[:, i, 1], color=colors[i], alpha=0.2)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1, box.width, box.height * 0.9])
    ax.set(ylabel='success rate')
    ax.set_xlabel('Epochs')
    plt.title('Training success rate with LP-based curriculum on 5 buckets.'
              ' \n predicates={close(), above()}, n_objects = 3')
    plt.grid()
    plt.legend(['Bucket {}'.format(i) for i in range(num_buckets)], fancybox=True, shadow=True, loc='lower center',
               bbox_to_anchor=(0.5, -0.25), ncol=5)
    plt.savefig('stats_deepsets04.png')
