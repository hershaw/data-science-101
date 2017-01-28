## What are we doing here?

You are going to learn about exploring datasets by inspecting correlations between and
doing principle component analysis on features.

The exercises will be similar for both `correlation` and `pca` directories. The each have:

- An `examples` directory
- An `iris` directory

### The examples directories

This directory contains pre-written notebooks showing examples and proof-of-concepts.
It is suggested to

1. Run them first and inspect the output. Discuss amongst yourselves the results.
2. Mess with parameters to see what changes. Again, discuss results.

### The iris directories

This directory is blank. In this you will start notebooks from scratch
and apply what you learned in the `examples` directory on the
[iris dataset](http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html).

Any notebooks that use the iris dataset will need to include the following
import in the first cell:

```
from codefiles.datagen import get_iris
```

You will then generate the dataset with the following:

```
df = get_iris()
```

It is on this dataframe that you will apply what you learned from the `examples` directory
to try to draw conclusions about the dataset.
