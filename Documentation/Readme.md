# DPL

## Data Parsing and Cleaning

**File** -> [Clean data](Z:\DPL\DataFrames\cleaning.ipynb)

### Description

Using the [Pandas](https://pandas.pydata.org/) library, the sheet datahas been cleaned separately for Batsmen, Bowlers and All rounders by removing the irrelevant data.

### Our Data Frame Structure

```json 
    Teams = {
        'Team name' : {
            'Batsmen' : {
                'Batsman name' : {
                    "_comment" : The pandas Data Frame with player attributes i.e the Sheet Data
                }
            }
            'Bowlers' : {
                'Bowler name' : {
                    "_comment" : The pandas Data Frame with player attributes i.e the Sheet Data
                }
            }
            'Allrounder' : {
                'All Rounder name' : {
                    "_comment" : The pandas Data Frame with player attributes i.e the Sheet Data
                }
            }
        }
    }
```

Using the above Dataframe any questions can be answered with the help of the following functions.
- [pandas.DataFrame.describe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
- [pandas.DataFrame.groupby](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)
- 
- 
- 

## Innings Distribution

**File** -> [Innings Distribution](Z:\DPL\DataFrames\innings_distribution.ipynb)

For an user input of a player name, A count plot will be shown to infer Innings Distribution and Order Distribution.

## Opponent Analysis 

For every player, the toughest or the most difficult opponent wil be displayed as a Table

## Ground Analysis 

Using Grouping and Distribution techniques, The Top & Worst 5 Pitches will be shown as Output

## Strike Rate Analysis 

A brief plot of strike rate over innings is plotted for each player. A graph is shown for inference. 

## Final Prediction

CSK will win its 6th Championship