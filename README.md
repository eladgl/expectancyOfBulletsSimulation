# expectancyOfBulletsSimulation
# created by eladgl
This code deals with simulation. The simulation wants to find expectancy of number of bullets to hit a target in order to improve accuracy.

Assuming we have a machine that fires a burst of bullets from some distance (meters) to some target of width and height (meters)
Each burst has a systematic error, and each bullet from the burst has a random error, each creates a certain radius where all the bullets fall at in a normal distribution.

The errors normally refereed as CEP (Circular Error Probable).

I assume here the systematic error of the maching is 0.1 milli radian and the random error is 0.2 mili radian.
I also assume here the bullets hit with normal distribution independet by coordinates (only x and y as the dimension is 2d),
where the std is the given CEP from each error and is divided by constant, std = CEP / 1.177


Due to the fact, this isn't solvable analytically I use a simulation, in particular, Monte Carlo simulation to get to some converging value.

----------------------------

There is a console interface given here. We can choose different distances, target's dimension and different values for the errors.
This code is done as modular as possible to allow reusage of different classes for the future.
