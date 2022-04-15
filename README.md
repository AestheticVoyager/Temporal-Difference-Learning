# Definition and role of backpropagation in TD-Gammon
Before we discuss the TD algorithm, we should talk briefly about the supervised learning technique known as backpropagation. 
Backpropagation works for neural networks that are “feed forward”, meaning there is no feedback or loops. 
Provided with an expected output, backpropagation takes the error and applies it starting at the outputs and propagating backwards with the amount of correction dependent on the existing weight.


But for backpropagation to work in a game like backgammon, after every move the network would require the “correct” decision and use that knowledge to train the network. 
As that informa-tion is not available, Tesauro used temporal difference methods. 
TD methods are somewhat like backpropagation over time to assign credit or blame of some reward to a previous state.
More specifically, when the network wins or loses a game, were all moves equally responsible for that win or loss? 
Obviously not. 
So, a temporal difference method is used to identify and reinforce the credit or blame with respect to the outcome.

The actual mechanics work like this.
You start with a random network.
This network is used to play both sides of a backgammon game.
At each point, the network evaluates the next moves to pick the best move.
Obviously, when the weights are random, the moves will also be random.
However, even though the evaluation means nothing at the start, you still treat the next evaluation as if it were the correct one.

What the temporal difference algorithm adds is to maintain information over time about these trainings.
While the infromation does decay eventually, it does flow forward in time influencing future training.
Even though the data is flowing forward in time, the net result is that the impact of winning or losing is backpropagated to the previous moves played.



# Temporal Difference Learning and TD-Gammon(By Gerald Tesauro)
TD-Gammon is a neural network that trains itself to be an evaluation function for the game of backgammon, by playing against itself and learning from the outcome.

It combines two major developments of recent years that appear to overcome traditional limitations to reinforcement learning. 

First, it uses the Multi-Layer Perceptron neural net architecture, widely popularized in backpropagation learning, as a method of learning complex nonlinear functions of its inputs.

Second, it apportions “temporal credit assignment” during each self-play game using a “Temporal Difference” (or simply TD) learning methodology.

The basic idea of TD methods is to base learning on the difference between temporally successive predictions. 

In other words, the goal is to make the learner’s current prediction for the current input pattern more closely match the subsequent prediction at the next time step. 

TD-Gammon was originally conceived as a basic-science study of how to combine reinforcement learning with nonlinear function approximation.

It was also intended to provide a comparison of the TD learning approach with the alternative approach of supervised training on a corpus of expert-labeled exemplars. 

The latter methodology was used previously in the development of Neurogammon, a neural network backgammon program that was trained by backpropagation on a data base of recorded expert move decisions.

Neurogammon achieved a strong intermediate level of play, which enabled it to win in convincing style the backgammon championship at the 1989 International Computer Olympiad.

By comparing TD-Gammon with Neurogammon, one can get a sense of the potential of TD learning relative to the more established approach of supervised learning.

Despite the rather academic research goals listed above, TD-Gammon ended up having a surprising practical impact on the world of backgammon. 

The self-play training paradigm enabled TD-Gammon’s neural net to significantly surpass Neurogammon in playing ability.

The original version 1.0 of TD-Gammon, which was trained for 300,000 self-play games, reached the level of a competent advanced player which was clearly better than Neurogammon or any other previous backgammon program.

As greater computer power became available, it became possible to have longer training sessions, and to use greater depth search for real-time move decisions. 

An upgraded version of TD-Gammon, version 2.1, which was trained for 1.5 million games and used 2-ply search, reached the level of a top-flight expert, clearly competitive with the world’s best human players.

It was interesting to note that many of the program’s move decisions differed from traditional human strategies. 

Some of these differences were merely technical errors, while others turned out to be genuine innovations that actually improved on the way humans played.

For example, on the opening play, the conventional wisdom was that given a roll of 2-1, 4-1, or 5-1, White should move a single checker from point 6 to point 5.
Known as "slotting", this technique trades the risk of a hit for the opportunity to develop an aggressive position.
TD-Gammon found that the more conservative play of 24-23 was superior.
Tournament players began experimenting with TD-Gammon's move, and found success.
Within a few years, slotting had disappeared from tournament play, though in 2006 it made a reappearance for 2-1.

TD-Gammon's excellent positional play was undercut by occasional poor endgame play.
The endgame requires a more analytical approach, sometimes with extensive lookahead.
TD-Gammon's limitation to two-ply lookahead put a ceiling on what it could achieve in this part of the game.

As a result, humans began carefully studying the program’s evaluations and rollouts and began to change their concepts and strategies.

After analysis of thousands of positions, new heuristic principles were formulated which accounted for the new data.

This trend of human experts learning from the machine was significantly accelerated when several other researchers were able to replicate the success of TD-Gammon with self-teaching neural nets.

Two such efforts, by Fredrik Dahl and Olivier Egger, have led to the creation of commercial PC programs called Jellyfish and Snowie, respectively. 


# Sources
- [TD-Gammon Paper by Gerald Tesauro](https://bkgm.com/articles/tesauro/tdl.html)
- [TD-Gammon Wiki](https://en.wikipedia.org/wiki/TD-Gammon)
- [TD-Gammon Revisited](http://modelai.gettysburg.edu/2013/tdgammon/pa4.pdf)
