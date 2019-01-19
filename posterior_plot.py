import numpy as np
def posterior_predictions(new_predictions): 
    def set_size(w,h, ax=None):
            """ w, h: width, height in inches """
            if not ax: ax=plt.gca()
            l = ax.figure.subplotpars.left
            r = ax.figure.subplotpars.right
            t = ax.figure.subplotpars.top
            b = ax.figure.subplotpars.bottom
            figw = float(w)/(r-l)
            figh = float(h)/(t-b)
            ax.figure.set_size_inches(figw, figh)

    import matplotlib.gridspec as gridspec
    import matplotlib.pyplot as plt
    from matplotlib import figure
    gs = gridspec.GridSpec(4,6)
    plot_titles = ["Male 0-17","Male 18-34","Male 35-54","Male 55+",
                          "Female 0-17","Female 18-34","Female 35-54","Female 55+"]
    plot_indexes = np.array([[0,3],[3,6],[0,3],[3,6],[0,3],[3,6],[0,3],[3,6]])

    for i in range(4):
        plt.tight_layout(pad=0.2, w_pad=0.5, h_pad=1.0)

        ax = plt.subplot(gs[i,0:3])
        set_size(10,10)
        ax.set_ylabel("Accepted number")
        ax.set_title(plot_titles[i])
        ax.set_ylim(0,300)
        ax.hist(new_predictions[i],bins=50,ec='white')
        plt.tight_layout(pad=0.2, w_pad=0.5, h_pad=1.0)

        ax = plt.subplot(gs[i,3:6])
        set_size(10,10)
        ax.set_ylabel("Accepted number")
        ax.set_title(plot_titles[i+4])
        ax.set_ylim(0,300)
        ax.hist(new_predictions[i+4],bins=50,ec='white')
    plt.show()