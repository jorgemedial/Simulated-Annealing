# Simulated Annealing

Simulated Annealing is an optimization algorithm that is specially useful for non-convex functions. 
This example project demonstrate how the [simulated annealing](https://en.wikipedia.org/wiki/Simulated_annealing)  algorithm is implemented and may be used to find global maximum of function with a large search space - or configuration space - in a heuristic way. 



## Examples

Three cases are shown: a convex function with one local maximum in a 2-dimensional space, a function with two local maximum in a 2-dimensional space and a highly non-convex function in a N-dimensional space.

### Function with one local minimum. Convex function: 

The simplest case would be a function with only one maximum, the global maximum. This way, there is no risk of obtaining a non-optimal solution and the problem becomes trivial, but it is a good example to show how the mechanism works. 



![](https://media.giphy.com/media/SE9PZVpiWmWxSkz1G3/giphy.gif)




[//]: # (a)


### Function with two local minima


When there are more than one local minimum, there is a risk of obtaining non optimal solutions

![](https://media.giphy.com/media/DzJDFxtBWZUQutswXj/giphy.gif)


But it is a matter of time that the algorithm obtains the optimal configuration

![](https://media.giphy.com/media/FaooEgrkgOP5TzqOLN/giphy.gif)