# Decision Trees
- tree-like graph with nodes representing the place where we pick an attribute and ask a question
- Edges represent the answers the to the question
- The leaves represent the actual class label.
- Used to solve Classification problems
- The decision rules are generally in form of if-then-else statements.
- The deeper the tree, the more complex the rules and fitter the model.

## **ALGORITHM:-**
1)  If node is pure, output is only class.
2)  If no feature is left to split upon, output majority.
3)  Find the best feature to fit upon
4)  Recursively class on the split.

### Entropy - measure of randomness.
- We choose information which gives us `high information gain` (less entropy).
