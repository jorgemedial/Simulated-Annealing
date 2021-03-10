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


But it is a matter of trial and error that the algorithm obtains the optimal configuration

![](https://media.giphy.com/media/FaooEgrkgOP5TzqOLN/giphy.gif)


## Application on more complex problems. Optimally synchronizable networks

The configuration space of a network of 
$N$ nodes is composed by $2^\frac{N(N-1)}{2}$ different configurations. Finding the configuration that optimizes a feature is not an easy task, since brute force is not an option anymore. This is why this method becomes so appealling: it is proven to work for some cost functions defined on networks. In this case, we are paying attention to the eigenratio of the graph laplacian.

### Optimization of the eigenratio.

The eigenratio of the graph laplacian measures the range of synchronizability of a network of coupled oscilators for different couplings. The meaning of this does not need to be understood, the eigenratio is simply a function defined over networks whose value is required to be minimal. In doing so, the configurations that we found are known as **entangled networks** (pictures below).

![Figure_1](https://user-images.githubusercontent.com/31573093/110714008-2019b300-8203-11eb-9e3d-5bcd17492fb4.png)

![Figure_3](https://user-images.githubusercontent.com/31573093/110714026-26a82a80-8203-11eb-8543-356280bdd58d.png)

![Figure_4](https://user-images.githubusercontent.com/31573093/110714041-2e67cf00-8203-11eb-9f8e-3139fc253d17.png)
![Figure_5](https://user-images.githubusercontent.com/31573093/110714055-31fb5600-8203-11eb-98f3-b6a3e0e8458e.png)
![Figure_6_6 721](https://user-images.githubusercontent.com/31573093/110714056-31fb5600-8203-11eb-8e67-29127f322bd8.png)
![Figure_7_7 6545](https://user-images.githubusercontent.com/31573093/110714060-3293ec80-8203-11eb-8999-31382ddf9d78.png)

