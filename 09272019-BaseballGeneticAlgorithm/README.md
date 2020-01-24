An extension of the FiveThirtyEight Riddler puzzle here https://fivethirtyeight.com/features/which-baseball-team-will-win-the-riddler-fall-classic/.

Instead of teams, this optimization attempts to find the optimal lineup given the different types of players (additionally, a "triple" type of player was added a Tripette). It turns out that player style diversity does not appear to help and given the rates originally set by the problem, the all Taters lineup appears to perform best in terms of wins (which is the same as the optimal team). Lowering the conversion values for Taters and Moonwalkers (to around 0.08 and .375 respectively), however, we find that the optimized lineup that is found alternates between Moonwalker players and Tripette players (which makes sense, as a Tripette or Moonwalker gets on base, then the next batter will always be able to score the runner if they convert).

The optimization uses a genetic algorithm, with 20 randomized lineups created at the start. Each generation, 20 mutants are created (with a parameterized amount of mutations), and 20 children are created from splicing the DNA lineup of two random parents. Each of the 60 lineups then "plays" each other a parameritized amount of times, and then the 20 lineups of the 60 total with the highest win percentage (alternatively, you can use highest average score) are choosen as parents for the next generation. The optimization appears to find an optimal lineup fairly quickly, most of the time within 20 generations.