import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')
plt.style.use('oneHalfColumn.mplstyle')

base_folder = "/home/dventuri/run/"
cases = ["sp_5x5_CoU",
         "sp_5x5_CoU_forced",
         "sp_5x5_CoU_forced_evap",
         "sp_5x5_CoF",
         "sp_5x5_CoF_forced",
         "sp_5x5_CoF_forced_evap",
         "sp_3x3_CoU_forced",
         "sp_3x3_CoU_forced_evap",
         "sp_3x3_CoF_forced",
         "sp_3x3_CoF_forced_evap"]#,
         #"sp30m_5x5_CoU_forced",
         #"sp30m_5x5_CoF_forced"]

for case in cases:

    line01_mean = []
    line01_std = []
    line02_mean = []
    line02_std = []

    for i in range(1,102):
        fn = base_folder+case+f"/probe_points/surf00001_sonda00{i:03d}.dat"
        data = np.loadtxt(fn, delimiter="   ", usecols=11)
        line01_mean.append(np.mean(data))
        line01_std.append(np.std(data))

    for i in range(1,102):
        fn = base_folder+case+f"/probe_points/surf00002_sonda00{i:03d}.dat"
        data = np.loadtxt(fn, delimiter="   ", usecols=11)
        line02_mean.append(np.mean(data))
        line02_std.append(np.std(data))

    x = np.linspace(-0.3207, 0.3207, 101)

    fig, ax = plt.subplots()
    ax.set_ylabel(r'$d_{droplet}$')
    ax.set_xlabel(r'$x$')
    ax.set_title(case)
    ax.axis([-0.3207, 0.3207, 0, 1.5e-3])
    ax.xaxis.set_major_locator(plt.MultipleLocator(0.1))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.025))
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.25e-3))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.125e-3))
    ax.errorbar(x,line01_mean, yerr=line01_std,
                color='black',
                linewidth=1,
                linestyle='-',
                label='line01')
    ax.errorbar(x,line02_mean, yerr=line02_std,
                color='blue',
                linewidth=1,
                linestyle='-',
                label='line02')
    ax.legend(loc='best')
    ax.vlines(0, 0, 0.0015, colors='grey', linestyles='dashed')
    ax.vlines(0.1390171932, 0, 0.0015, colors='grey', linestyles='dashed')
    ax.vlines(-0.1390171932, 0, 0.0015, colors='grey', linestyles='dashed')
    fig.tight_layout(pad=0.01)
    plt.savefig(f'figures/{case}.png',
                format='png',
                dpi=300)
