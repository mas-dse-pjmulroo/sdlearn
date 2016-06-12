# sdlearn

```
    Implementation of simple stacking method. Desgined to
    work with sklearn classifiers and regressor functions,
    but will work with any classifier that has a 'fit', 'predict',
    and 'score' function. The function also includes a novel
    technique for pruning poor performing classifiers for brute
    forcing attempts.

    When setting up the stack pass a list of classifiers for each
    level of the stack. IE

    classifiers = [[ensemble.RandomForestRegressor(),
                    ensemble.AdaBoostRegressor(),
                    linear_model.LinearRegessor()],
                   [ensemble.RandomForestRegressor(),
                    ...],
                   [linear_model.LinearRegressor()]]
```
