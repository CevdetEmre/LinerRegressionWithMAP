# LinerRegressionWithMAP
Maximum a Posteriori estimate
Maximum a Posteriori (MAP)
Recall that the Bayes theorem provides a principled way of calculating a conditional probability.

It involves calculating the conditional probability of one outcome given another outcome, using the inverse of this relationship, stated as follows:

P(A | B) = (P(B | A) * P(A)) / P(B)
The quantity that we are calculating is typically referred to as the posterior probability of A given B and P(A) is referred to as the prior probability of A.

The normalizing constant of P(B) can be removed, and the posterior can be shown to be proportional to the probability of B given A multiplied by the prior.

P(A | B) is proportional to P(B | A) * P(A)
Or, simply:

P(A | B) = P(B | A) * P(A)
This is a helpful simplification as we are not interested in estimating a probability, but instead in optimizing a quantity. A proportional quantity is good enough for this purpose.

We can now relate this calculation to our desire to estimate a distribution and parameters (theta) that best explains our dataset (X), as we described in the previous section. This can be stated as:

P(theta | X) = P(X | theta) * P(theta)
Maximizing this quantity over a range of theta solves an optimization problem for estimating the central tendency of the posterior probability (e.g. the model of the distribution). As such, this technique is referred to as “maximum a posteriori estimation,” or MAP estimation for short, and sometimes simply “maximum posterior estimation.”

maximize P(X | theta) * P(theta)
We are typically not calculating the full posterior probability distribution, and in fact, this may not be tractable for many problems of interest.
