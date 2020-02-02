# Cricket Fever

https://www.youtube.com/watch?v=n3Ld_40X1EY

Welcome to Cricket Fever! The goal of the game is to win coins. All your coins add up to give you a place on the leaderboard. To win coins, you can play cricket trivia or predict the result of the upcoming cricket match!

In cricket trivia, I will ask you a random question. For every right answer, you get 1 coin. You have to respond with the number of the answer. For example, say one, two, three, or four.

While for the game prediction game, I will tell you about an upcoming match between Team A and Team B. You will wager 10 coins to predict the result. You win 20 coins for a correct prediction and lose 10 coins for a wrong prediction. To make a prediction, you just say either Team A or Team B. You can say skip if you don't want to make any predictions and go back to the dashboard.

#### Architecture Details
The complete presentation for the skill can be viewed directly on: https://docs.google.com/presentation/d/1j1Kgm9A7tHdGQ7_Y7VYBA-CPadNgjTczarMKe1fGV1A/edit?usp=sharing

The skill's Voice User Interface (VUI) and the logic have been completely written in Voiceflow. The flow blocks have been added in the presentation file. Alternatively, you can access the complete project by importing it in Voiceflow through: https://creator.voiceflow.com/dashboard?import=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0SWQiOjkyMzE3LCJwcm9qZWN0TmFtZSI6IkNyaWNrZXQgRmV2ZXIiLCJpYXQiOjE1ODA2NTE5MjJ9.-D4q1XnM3yJJd8K3-ONtUE5Yp4w09ku8U1IWY44Zxto

For the database, we are using Google Sheets: https://docs.google.com/spreadsheets/d/1XU_hEaU_g_hhHLA254WQ5OmsUcoGOc9Of2UfqbVlj4Y/edit?usp=sharing

We are running a Flask App that allows a player to view the dynamic global leaderboard. It also continously polls the database and the Cricket API to view the match result and update the coins of the participants automatically. After the updation, it fetches new upcoming match details and updates the database. The code for the Flask app can be accessed through: https://github.com/hannansatopay/Cricket-Fever

The Cricket API being utilized for fetching the match results: https://rapidapi.com/dev132/api/cricket-live-scores

#### Instructions:
1. Open the skill by saying "Alexa, open cricket fever"
2. You will be greeted by the skill. You can say "Yes" to continue
3. Next, you can say "cricket trivia" to play cricket trivia or say "predict match" to play the match prediction game
4. Follow the flow to win coins and score high rank in the leaderboard
5. Note that you only make one match prediction and you have to wait for the match to end to make the next prediction. You can play cricket trivia an unlimited number of times.
6. You can say "Alexa, help" to get more details about the skill. You can say "Alexa, stop" to stop the skill.

##### Note:
Vendor ID: M3JWD8H81W6DWV
Skill ID: amzn1.ask.skill.f2d5e6d2-634f-4c5b-815e-1990415bb29a
