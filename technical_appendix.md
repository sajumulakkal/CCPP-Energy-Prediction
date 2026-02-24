# 📚 TECHNICAL APPENDIX: Mathematical Evaluation

To ensure the reliability of our power plant forecasts, we utilized two primary statistical metrics to validate our models and analyzed the architectural logic of the winning algorithm.

---

### 1. Root Mean Square Error (RMSE)
RMSE represents the standard deviation of the residuals (prediction errors). It tells us how far, on average, our predictions are from the actual MW values.

$$RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$

* **$n$**: Total number of observations.
* **$y_i$**: Actual Energy Output (PE) recorded by sensors.
* **$\hat{y}_i$**: Predicted Energy Output from the model.

**Significance:** A lower RMSE indicates a more precise "tightness" to the actual data. Our Random Forest achieved a low **3.25 MW** error.

---

### 2. Coefficient of Determination ($R^2$)
The $R^2$ score represents the proportion of variance for the energy output that is explained by the environmental features (AT, V, AP, RH).

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$$

**Where:**
* **$SS_{res}$** $= \sum (y_i - \hat{y}_i)^2$ (Sum of Squares of Residuals)
* **$SS_{tot}$** $= \sum (y_i - \bar{y})^2$ (Total Sum of Squares)

**Significance:** An $R^2$ of **0.9637** means that over **96%** of the variability in power production is directly explained by our four sensors, leaving less than 4% to unknown factors.

---

### 3. Random Forest Logic
Unlike the rigid single line of Linear Regression, the Random Forest utilizes **Bootstrap Aggregation (Bagging)** to reduce variance and handle non-linear sensor relationships.



The model builds an ensemble of decision trees and aggregates their results to reach a single conclusion:

$$\hat{f} = \frac{1}{B} \sum_{b=1}^{B} f_b(x)$$

* Each **$f_b(x)$** is an individual decision tree trained on a random subset of data.
* The final prediction is the **average** of all trees.
* **Benefit:** This prevents "overfitting," ensuring the model performs well on new, unseen weather data rather than just memorizing the training set.
