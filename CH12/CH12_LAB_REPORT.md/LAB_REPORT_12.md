# Chapter 12: Regression (K-Nearest Neighbors (KNN)) — Lab Report
---

## Student Information
**Name:** Owen A LeeChong  
**Date:** April 27, 2026  
**Algorithm Analysis:** K-Nearest Neighbors (KNN) Regression for Bakery Loaf Prediction

---

## Algorithm Understanding

**What type of problem is this algorithm solving?** This is a supervised learning problem, specifically a regression task, because we are predicting a continuous numerical value (the number of loaves) based on input features.

**How does KNN regression differ from KNN classification?** In KNN classification, the model assigns a discrete label based on the majority "vote" of its neighbors. In KNN regression, the model predicts a continuous value by calculating the average (mean) of the target values of the $K$ nearest neighbors.



**What does the "K" in KNN represent, and why did we choose k=4 for this problem?** "K" represents the number of nearest data points the algorithm looks at to make a prediction. We chose K=4 to balance the model; it is large enough to smooth out noise from a single outlier day but small enough to remain sensitive to specific patterns in the local data.

**In your own words, explain how the model produces a prediction for a new day.** When given a new day's conditions (weather, holiday, game status), the model looks through the historical dataset to find the 4 days that have the most similar conditions. It then takes the number of loaves sold on those 4 days and calculates their average to give us today's prediction.

---

## Implementation Questions

**Why do we separate the DataFrame into features (X) and target (y) before training?** Scikit-learn models require a clear distinction between the independent variables (features used for prediction) and the dependent variable (the outcome we want to predict). This mimics the mathematical function f(X) = y.

**Why must the input to `model.predict()` be a 2D array (e.g., `[[4, 1, 0]]`) instead of a 1D array (`[4, 1, 0]`)?** Scikit-learn is designed to handle batch predictions (predicting many days at once). Even if you are only predicting for one day, the model expects a matrix (rows and columns), where each row is a sample.

**What does `.fit(X, y)` actually do for a KNN model?** Unlike algorithms that calculate complex weights (like Linear Regression), KNN is a "lazy learner." The `.fit()` method primarily stores the training data in an efficient internal structure (like a KD-Tree) so that distances can be calculated quickly during the prediction phase.

**Why do we use `.values` when extracting columns from the DataFrame?** The `.values` attribute converts the Pandas Series or DataFrame into a NumPy array. Scikit-learn is built on top of NumPy, and using raw arrays ensures compatibility and faster numerical processing.

---

## Extension: Choosing K

**What would happen if we set k=1? What are the risks?** Setting K=1 leads to overfitting. The model would simply mimic the single closest historical day. If that one day had an unusual event (like a random large party order), the prediction would be highly inaccurate and sensitive to "noise."

**What would happen if we set k=20 (the size of the entire dataset)? What does the model become?** If K=20, the model would average every single day in the history for every prediction. It would effectively become a simple average model, predicting the same number of loaves regardless of the weather or if it’s a weekend.

**How would you decide what value of k is best for a given dataset?** I would use cross-validation. This involves testing various values of "K" on a subset of data and choosing the one that results in the lowest error (such as Mean Squared Error) on data the model hasn't "seen" yet.

---

## Extension: Distance and Feature Scaling

**KNN uses distance to find "nearest" neighbors. Our features have very different ranges: weather is 1–5, but weekend_holiday and game_on are 0/1. Why could this be a problem?** Features with larger ranges dominate the distance formula. A change of 1 in weather (from 4 to 5) might be seen by the computer as equally important as a change of 1 in `game_on` (from 0 to 1), even though a game might have a much larger real-world impact on sales than a slight weather shift.

**Give an example of two days where the weather feature would unfairly dominate the distance calculation.** If Day A has `Weather=5, Game=0` and Day B has `Weather=1, Game=0`, the distance is 4 units. If Day C has `Weather=5, Game=1`, the distance between Day A and Day C is only 1 unit. The model might think A and C are "closer" just because the weather matches, ignoring the fact that a game (Game=1) changes the business dynamic entirely.

**How would you modify the data preparation step to fix this?** I would use feature scaling, such as `StandardScaler` from scikit-learn. This transforms all features so they have a mean of 0 and a standard deviation of 1, putting them on a "level playing field" for distance calculations.

---

## Reflection Questions

**What is a limitation of KNN regression? Provide a scenario where it would make a poor prediction.** KNN cannot **extrapolate**. If a massive blizzard occurred with a weather rating of 10 (outside our 1–5 scale), KNN could only predict based on the nearest historical days (weather 5), likely underestimating the impact of the extreme event.

**Our dataset only has 20 days of data. How might the predictions change if we had 2,000 days of data instead?** With 2,000 days, the "neighborhoods" would be much denser. The model would find days that are nearly identical to today's conditions, likely making the prediction much more accurate and stable.

**What other features could the bakery collect to improve predictions?** External temperature, local school holiday schedules, the price of the bread that day, and perhaps social media mentions of the bakery.

**KNN is sometimes called a "lazy learning" algorithm. What is the tradeoff at prediction time?** The tradeoff is computation speed. While training is nearly instant, the computer must calculate the distance between the new day and *every single point* in the database at prediction time. For huge datasets, this can be very slow.

**Identify the 4 historical days used for the 70.5 loaf prediction.** Looking at the data for conditions `Weather=4, Weekend=1, Game=0`, the closest days are:
1. Day 4 (4, 1, 0) -> 72 loaves
2. Day 20 (4, 1, 0) -> 75 loaves
3. Day 8 (4, 0, 0) -> 50 loaves
4. Day 10 (5, 1, 0) -> 85 loaves
*Average: (72 + 75 + 50 + 85) / 4 = 70.5.*

**Why might a bakery prefer a slightly inaccurate ML prediction over a human guess?** ML is consistent and data-driven. A human might forget how a rainy Tuesday 3 months ago went, but the model remembers perfectly. It removes emotional bias and provides a reliable baseline for ordering supplies.

**If the bakery wanted to MINIMIZE waste, how might you change the approach?** I would adjust the prediction by a safety margin (e.g., subtracting 5% from the result) or use a custom loss function that penalizes over-predicting more heavily than under-predicting.

