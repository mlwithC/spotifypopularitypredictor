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

-We trained a Logistic Regression model to classify songs as hits or flops based on their audio features.
-The model achieved an impressive accuracy of 99.5%, indicating strong predictive performance on the test set.
-This serves as a baseline to compare with more complex models like Random Forest and SVM. 

 Decision Tree Classifier,. Random Forest Classifier

Achieved 100% accuracy on the test set.
Also achieved 100% accuracy.

will check later the model is overfitting or anything else 