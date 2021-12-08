import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')
plt.style.use('oneHalfColumn.mplstyle')


def calculate_line_statistics(case_name: str, probe_number: int):

    n_points_per_line = 101

    mean = []
    std = []

    for i in range(1,n_points_per_line+1):
        fn = f"{case_name}/output/probe_points/surf{probe_number:05d}_sonda{i:05d}.dat"
        idx, data = np.loadtxt(fn,
                               delimiter="   ",
                               usecols=(1,11),
                               unpack=True)
        idx = idx[::-1]
        data = data[::-1]

        unique, unique_idx = np.unique(idx, return_index=True)
        data = data[unique_idx]

        mean.append(np.mean(data))
        std.append(np.std(data))

    return mean, std


def plot_statistics(mean, std, fig, ax):
    x = np.linspace(-0.3207, 0.3207, 101)

    ax.set_ylabel(r'$d_{droplet}$')
    ax.set_xlabel(r'$x$')
    #ax.set_title(case)
    ax.axis([-0.3207, 0.3207, 0, 1.5e-3])
    ax.xaxis.set_major_locator(plt.MultipleLocator(0.1))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.025))
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.25e-3))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.125e-3))
    ax.errorbar(x,mean, yerr=std,
                color='black',
                linewidth=1,
                linestyle='-',
                label='line01')
    ax.legend(loc='best')
    ax.vlines(0, 0, 0.0015, colors='grey', linestyles='dashed')
    ax.vlines(0.1390171932, 0, 0.0015, colors='grey', linestyles='dashed')
    ax.vlines(-0.1390171932, 0, 0.0015, colors='grey', linestyles='dashed')
    fig.tight_layout(pad=0.01)
    # plt.savefig(f'figures/{case}.png',
    #             format='png',
    #             dpi=300)


def main():
    base_folder = "/home/dventuri/run/"
    cases = [#"sp_5x5_CoU",
             #"sp_5x5_CoU_forced",
             "sp_5x5_CoU_forced_evap",
             #"sp_5x5_CoF",
             #"sp_5x5_CoF_forced",
             #"sp_5x5_CoF_forced_evap",
             #"sp_3x3_CoU_forced",
             #"sp_3x3_CoU_forced_evap",
             #"sp_3x3_CoF_forced",
             #"sp_3x3_CoF_forced_evap"
            ]

    n_probe_lines = 10

    for case in cases:
        fig, ax = plt.subplots()
        for n in range(1,n_probe_lines+1):
            mean, std = calculate_line_statistics(f"{base_folder}{case}", n)

            plot_statistics(mean, 0, fig, ax)

    #list for linestyles and linecolors?

if __name__ == "__main__":
    main()
