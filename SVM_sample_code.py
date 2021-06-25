#서포트벡터머신

def create_svm_plot(value1, value2, shape):

    from sklearn import svm
    from mlxtend.plotting import plot_decision_regions
    # First, we'll import pandas, a data processing and CSV file I/O library
    import pandas as pd
    # We'll also import seaborn, a Python graphing library
    import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
    warnings.filterwarnings("ignore")
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np

    X = dataframe[[value1, value2]]
    y = dataframe['citySidoName']

    plt.figure(figsize=(16,8))

    if shape == "round":
        clf = svm.SVC(decision_function_shape = 'ovo')
    elif shape == "linear":
        clf = svm.SVC(C=0.5, kernel='linear')
    else:
        raise NameError('Shape must be round of linear')
    clf.fit(X.values, y.values)

    # Plot Decision Region using mlxtend's awesome plotting function
    plot_decision_regions(X=X.values,
                          y=y.values,
                          clf=clf)

    # Update plot object with X/Y axis labels and Figure Title
    plt.xlabel(X.columns[0], size=14)
    plt.ylabel(X.columns[1], size=14)
    plt.title('SVM Decision Region Boundary : ' + value1 + " and " + value2, size=16)

    legend = plt.legend()
    legend.get_texts()[0].set_text('Iris-setosa')
    legend.get_texts()[1].set_text('Iris-versicolor')
    legend.get_texts()[2].set_text('Iris-virginica')

create_svm_plot('ctznCnt', 'sum_Quantity', "linear")
fig = plot.get_figure()
plt.show()