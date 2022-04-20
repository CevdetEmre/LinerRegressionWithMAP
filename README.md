Assume you have a set of observed data (ti,xi) from an unknown process, where xi and ti are inputs and outputs, respectively. It's a vector if the xi is bold. A function ti = f(xi,w) can be used to represent the relationship between an unknown process' output, ti, and its input, xi. Geometrically, We can represent any vector/point in the vector space using linear algebra given we have the correct collection of basis vectors. Our input exists in a D-dimensional space, RD, and our output exists in an M-dimensional space, RM, which I like to refer to as the output space.Finding a reasonable value of M, i.e. a suitable number of basis and parameter values, w, that combines these basis, is now our modeling problem. These foundations are functions of x once again, which I suppose is for tuning purposes! The term "base functions" refers to these functions. Many functions, such as polynomials, gaussians, and sigmoids, can be employed as basis functions. Polynomials will be used in the programming section of this post.

![image](https://user-images.githubusercontent.com/86251983/164310038-27371fdb-41bd-48b0-beef-a5c1220b607b.png)

This function defines a pattern in this data, and if there is one, we can anticipate to measure the same result ti the next time we have an input xi, as predicted by our function. However, because there is always some noise in our measurements, this will not be completely correct in practice. As a result, our function should take this into account. Our observations will inevitably gravitate toward our function prediction. The distribution of these predictions approximates a Gaussian distribution due to the central limit theorem.

![image](https://user-images.githubusercontent.com/86251983/164310211-9e258950-3adb-427e-b9bf-902a360ddfb4.png)

The joint probability of all observations is a product of the probability distributions of the individual observations, shown below, assuming that they are independent and identically distributed (i.i.d).

![image](https://user-images.githubusercontent.com/86251983/164310241-795d6081-45d7-4f25-8486-378c124da719.png)

This is known as probability, and we can get the expression below by applying log on both sides so that we may deal with adds rather than products.

![image](https://user-images.githubusercontent.com/86251983/164310340-31845211-4825-4a81-ba55-6fbe8d0ede43.png)

The greek Φ symbol is known as the plan framework, we will see one approach to building this in the code segment. t is a segment vector of result perceptions tᵢ and X is a framework where each column is a perception xᵢ. Expecting we fix an incentive for M, the upsides of the boundaries of our model that boosts the probability has a shut structure arrangement, alluded to as the Maximum likelihood estimate

![image](https://user-images.githubusercontent.com/86251983/164310503-9cb520d3-e2fc-4865-a80e-e78454565598.png)


To get the intuition for maximum likelihood, let’s do a simple idea experiment. Say we flip a coin once, perhaps we get a Tail. Okay, let’s flip for a moment time, aand we get a Tail again. Okay, perhaps this coin is flawed. Let’s flip one more time, and once more this time we still get a tail. As said by these observations we may as well sum it up that the chances of receiving a Tail are 100%. But we know that our coin is impartial i.e. prior knowledge. Utilizing Baye’s theorem, we take advantage of this prior knowledge to come over here up with a greater expression for computing our parameter w.

![image](https://user-images.githubusercontent.com/86251983/164310725-ccc341f2-64ca-44be-98f0-0ca41d949ae3.png)

Implementing log to both sides of the equation and resolving for the best parameter w , as it was done before, we inherit the expression under and the parameter estimate underneath it. This is titled Maximum a Posteriori estimate (MAP).

![image](https://user-images.githubusercontent.com/86251983/164310809-4c02a214-7e1f-49e3-b890-183b2eb12d80.png)
