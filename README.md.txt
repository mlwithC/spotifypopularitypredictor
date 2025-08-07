 A machine learning regression project to predict whether a song is likely to be popular based on its audio features such as danceability, energy, tempo, etc.

Project Objective
To build a regression model that uses various audio features of songs to predict the popularity target score (binary or continuous) of Spotify tracks.


~Loaded and explored the dataset
~Created the full DataFrame with features and target
~Checked for null values and unique target values

Comparative Analysis of Musical Features

We plotted the distribution of key features — `danceability`, `energy`, `valence`, and `acousticness` — to compare hit and flop songs:

- Hit songs show higher danceability and energy, indicating a preference for rhythm and high engagement.
- Valence (musical positivity) is slightly higher in hit songs, reflecting listener preference for uplifting music.
- Acousticness is higher in flop songs, suggesting that less electronically-produced songs are less popular.

These trends help in selecting and prioritizing features during modeling. 

Data Cleaning & Preprocessing

- Removing nulls and duplicate records to ensure clean data.
- Dropping non-numeric columns (song_title, artist) not useful for model training.
- Separating features (X) and target (y).
- Applying StandardScaler to normalize all numeric features, ensuring they have the same scale for better model performance and stability.

Split and train ,Logistic Regression model

We trained a Logistic Regression model to classify songs as hits or flops based on their audio features.
-The model achieved an impressive accuracy of 99.5%, indicating strong predictive performance on the test set.
-This serves as a baseline to compare with more complex models like Random Forest and SVM. 

 Decision Tree Classifier,. Random Forest Classifier

Achieved 100% accuracy on the test set.
Also achieved 100% accuracy. 

will check later the model is overfitting or anything else 

K-Nearest Neighbors (KNN)
-Achieved an accuracy of 94.55%.
-Performs well and is easy to implement, but slightly less accurate due to sensitivity to feature scaling and neighbor selection.

Support Vector Machine (SVM)
-Achieved an accuracy of 98.27%.
-Offers strong performance with clear class boundaries, especially in high-dimensional space.

added the comparison model barplot among them we have choosen the random forest model to save.

saved the model and tried to run but the model is predicting wrong well thts expected 
it i think the model is unbalanced so wrking on it 

 Although this project originally used regression to predict exact popularity scores,
# the dataset was found to be heavily imbalanced — with almost all songs having low popularity (0–30).
# As a result, the model failed to generalize and always predicted low values (underfitting).
# To resolve this, we switch to a classification approach: Low, Medium, High popularity categories.

will make a new file and do the classification model there

before moving here is the reason
well tried to figure it out but didn't work out so will do again tomorrow
so wht we did the cause is we initially tried regression to predict a song’s popularity score, but the dataset didn’t have a proper numerical popularity column—only a binary target (popular or not). 
Since the outcome is just 0 or 1.
it makes more sense to treat this as a classification problem.
This way, the model can better learn patterns that separate popular songs from unpopular ones.

so we made a classifer for the spotify popularity predictor and we got 77% which is kinda great for now
and we tested with the manual and real song from data test wht we got is:
Our model is 77% accurate, but it's not always right. In this case, it missed a popular song. That’s because some things like fame or promotions — which also affect popularity — weren’t in our dataset.

 



