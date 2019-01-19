def plot_results_pooled(fit,all_mus2_5,all_mus97_5,all_people):
    import numpy as np
    alpha = fit.extract('alpha')
    alpha = alpha['alpha']
    alpha = np.mean(alpha,axis=0)
    beta = fit.extract('beta')
    beta = beta['beta']
    beta = np.mean(beta,axis=0)
    new_predictions = fit.extract()['y_pred_18']
    new_predictions = np.mean(new_predictions,axis=0)
    import matplotlib.pyplot as plt
    years_repeat = np.array(list(range(2010,2018,1))).reshape((8,1))
    years_repeat = np.tile(years_repeat,8).flatten()
    years = np.array(list(range(2010,2018,1)))
    
    flatten_all_ppl = all_people.flatten()
    plt.scatter(years_repeat,flatten_all_ppl)
    pred_vals = []
    for year in years:
        pred_vals.append(alpha*year+beta)
    plt.plot(years,pred_vals)
    plt.plot(years,all_mus2_5,linestyle='--')
    plt.plot(years,all_mus97_5,linestyle='--')
