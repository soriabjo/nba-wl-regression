# CSE-163-Final-Project

For our final project for CSE 163, we decided to predict NBA win percentage's from one regular season to the next using a supervised regression ML model. To do this, we scraped [Basketball Reference](https://www.basketball-reference.com) using BeautifulSoup in order to get our team data from the 2018-2019 and 2019-2020 NBA regular season. Additionally, we wanted to examine whether traditional or advanced statistics is best at predicting the win percentage of a team.

In the context of our project, "traditional" statistics refers to a basic counting stats such as a team's PTS/REB/AST per game, while "advanced" statistics refers to more complex measures such as offensive/defensive rating, assist percentage, pace, etc.

## Libraries Used

- BeautifulSoup - For web scraping data
- ELI5 - To interpret variable weights
- Scikit-learn - For implementing ML + metrics
- Matplotlib - Producing graphs
- Seaborn - Producing graphs
- Pandas - To store and wrangle data  
