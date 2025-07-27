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


