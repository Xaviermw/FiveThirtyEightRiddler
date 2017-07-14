/*

Created By Xavier Weisenreder:

Congratulations! The Acme Axegrinders, which you own, are the regular season champions of the National Squishyball League (NSL). Your team will now play a championship series against the Boondocks Barbarians, which had the second-best regular season record. You feel good about Acme’s chances in the series because Acme won exactly 60 percent of the hundreds of games it played against Boondocks this season. (The NSL has an incredibly long regular season.) The NSL has two special rules for the playoffs:

The owner of the top-seeded team (i.e., you) gets to select the length of the championship series in advance of the first game, so you could decide to play a single game, a best two out of three series, a three out of five series, etc., all the way up to a 50 out of 99 series.
The owner of the winning team gets $1 million minus $10,000 for each of the victories required to win the series, regardless of how many games the series lasts in total. Thus, if the top-seeded team’s owner selects a single-game championship, the winning owner will collect $990,000. If he or she selects a 4 out of 7 series, the winning team’s owner will collect $960,000. The owner of the losing team gets nothing.
Since Acme has a 60 percent chance of winning any individual game against Boondocks, Rule 1 encourages you to opt for a very long series to improve Acme’s chances of winning the series. But Rule 2 means that a long series will mean less winnings for you if Acme does take the series.

How long a series should you select in order to maximize your expected winnings? And how much money do you expect to win?

 */

package squishballsim;

//Used For Checking if Team Wins
import java.util.Random;


public class SquishballSim {

    public static void main(String[] args) 
    {
        //Amount of Sims at each level
        final int SIMS_EACH_SERIES_AMOUNT = 1000000;
        
        //ACME Team WP
        final double WIN_PERCENTAGE = .6;
        
        //Tracks Game Victories Each Sim
        int acmeVictories;
        int boonVictories;
        
        double moneyGained;
        
        //Total Wins To Win a Series
        int winThreshold;
        
        //Used For Win Percentage At Each Level
        int totACVics;
        int totBNVics;

        Random rand = new Random();
        
        //Each Level Up to 199 Series Length
        for (int i  = 1; i <= 199; i = i + 2)
        {
            //Resets Values For New Level
            moneyGained = 0;
            winThreshold = i/2 + 1;
            totACVics = 0;
            totBNVics = 0;
            
           
            for (int s = 0; s < SIMS_EACH_SERIES_AMOUNT; s++)
            {
                //Resets Victories Each New Series
                acmeVictories = 0;
                boonVictories = 0;
                
                //While The Series Is Still Going
                for (int g = 1; g <= i; g++)
                {
                    //Determines Who Wins
                    if (rand.nextDouble() < WIN_PERCENTAGE)
                        acmeVictories++;
                    else
                        boonVictories++;
                    
                    //Checks if Series is Over
                    if (acmeVictories == winThreshold)
                    {
                        //Money gained that sim divided by total sims
                        moneyGained += ((1000000-(winThreshold*10000.0))/SIMS_EACH_SERIES_AMOUNT);
                        g = i + 1;
                        totACVics++;
                    }
                    else if (boonVictories == winThreshold)
                    {
                        g = i + 1;    
                        totBNVics++;
                    }
                }
            }
            
   
            //System.out.println(moneyGained);
            //System.out.println((totACVics*1.0)/(totACVics*1.0+totBNVics));
            
            //Prints Average Value Given Series Length
            System.out.println("Series Length " + i + " average gain: " + moneyGained);
        }
        
        
    }
    
}
