import numpy as np
import pandas as pd
import io
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score as r2

plt.switch_backend('Agg')

models = {"linear": LinearRegression,
          "logistic": LogisticRegression}

#needs to differentiate between classifier and regression. If classifier, data displayed should be
#points on on real line (-1 - 1) colored to demonstrate accuracy of classifier.

#if regression, plot dependent variable vs loss (show where the model predicts well and where not)

def calculate_regression(input_csv, dependent_var, independent_vars, model_type, is_classifier):
    data = pd.read_csv(input_csv)
    #print(data[dependent_var])
    X = data[independent_vars]
    y = data[dependent_var]
    regression = models[model_type]()
    regression.fit(X, y)

    predictions = regression.predict(data[independent_vars])
    print(regression.coef_)
    print(regression.intercept_)
    print(predictions)
    print("r^2 = " + str(r2(y, predictions)))

    plt.close()
    # TODO - return tuple including plot as png bytes.
    # require the classes to be labeled -1 or 1
    if is_classifier:
        colors = ["red" if datum > 0 else "blue" for datum in y]
        red_predictions = [predictions[i] for i, color in enumerate(colors) if color == "red"]
        blue_predictions = [predictions[i] for i, color in enumerate(colors) if color == "blue"]
        #plt.scatter(predictions, np.zeros_like(predictions), c=colors, s=100)  # s=300 sets the size of the points
        reds = plt.scatter(red_predictions, np.zeros_like(red_predictions), c="red", s=100)
        blues = plt.scatter(blue_predictions, np.zeros_like(blue_predictions), c="blue", s=100)
        plt.axvline(x=0, color='black', linewidth=3)  # Add a thick tick mark at zero

        # Customizing the plot
        plt.yticks([])  # Hide y-axis ticks since we're only interested in the real line
        plt.xticks(range(int(min(predictions))-1, int(max(predictions))+2))  # Adjust x-ticks to provide some padding
        plt.legend([reds, blues], [dependent_var, "not " + dependent_var])

        #plt.show()
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        return(buf) #this will be tuple including buf, r2, and regression coefs