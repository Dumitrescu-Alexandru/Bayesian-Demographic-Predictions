def plot_results(fit,all_mus2_5,all_mus97_5,all_people):
    import numpy as np
    alpha = fit.extract('alpha')
    alpha = alpha['alpha']
    a = np.mean(alpha,axis=0)
    b = fit.extract('beta')
    b = b['beta']
    b = np.mean(b,axis=0)
    new_predictions = fit.extract()['y_pred_18']
    new_predictions = np.mean(new_predictions,axis=0)
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
    years = list(range(2010,2018,1))
    years = np.array(years)
    plt.show()
    for i in range(4):

    	# PLOT MALE
        if (i < 3):
            male = all_people[:,i]
            female = all_people[:,i+4]
            ax = plt.subplot(gs[i,0:3])
            set_size(10,10)
            plt.tight_layout(pad=0.2, w_pad=0.5, h_pad=1.0)
            ax.set_xlabel("Years")
            ax.set_ylabel("Accepted number")
            ax.set_title(plot_titles[i])
            ax.set_ylim(0,2700)
            ax.scatter(years,male)
            ax.plot(years,all_mus2_5[:,i],linestyle='--')
            
            ax.plot(years,b[i]+ a[i]*years) # ??? 
            ax.plot(years,all_mus97_5[:,i],linestyle='--')
            ax.scatter(2018,new_predictions[i],marker="x")
            # PLOT FEMALE 
            ax = plt.subplot(gs[i,3:6])
            ax.set_xlabel("Years")
            ax.set_ylabel("Accepted number")
            ax.set_title(plot_titles[i+4])
            ax.set_ylim(0,2700)
            ax.scatter(years,female)
            ax.plot(years,all_mus2_5[:,i+4],linestyle='--')
            ax.plot(years,b[i+4]+a[i+4]*years)
            ax.scatter(2018,new_predictions[i+4],marker="x")
            ax.plot(years,all_mus97_5[:,i+4],linestyle='--')
        else:
            male = all_people[:,i]
            female = all_people[:,i+4]
            ax = plt.subplot(gs[i,0:3])
            set_size(10,10)
            plt.tight_layout(pad=0.2, w_pad=0.5, h_pad=1.0)
            ax.set_xlabel("Years")
            ax.set_ylabel("Accepted number")
            ax.set_title(plot_titles[i])
            ax.set_ylim(0,500)
            ax.scatter(years,male)
            ax.plot(years,all_mus2_5[:,i],linestyle='--')
            ax.plot(years,b[i]+a[i]*years)
            ax.plot(years,all_mus97_5[:,i],linestyle='--')
            ax.scatter(2018,new_predictions[i],marker="x")
            # PLOT FEMALE 
            ax = plt.subplot(gs[i,3:6])
            ax.set_xlabel("Years")
            ax.set_ylabel("Accepted number")
            ax.set_title(plot_titles[i+4])
            ax.set_ylim(0,500)
            ax.scatter(years,female)
            ax.plot(years,all_mus2_5[:,i+4],linestyle='--')
            ax.plot(years,b[i+4]+a[i+4]*years)
            ax.scatter(2018,new_predictions[i+4],marker="x")
            ax.plot(years,all_mus97_5[:,i+4],linestyle='--')
    plt.show()