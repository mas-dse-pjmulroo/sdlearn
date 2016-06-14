class Stacking:
    """Stacking method.

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
    """
    def __init__(self, classifiers=None, prune=None):
        if prune == None: prune = self._prune
        self.classifiers = classifiers
        self.prune = prune
        self.cutoff_ = 0.2

    def print_classifiers(self):
        for level in self.classifiers:
            for classifier in level:
                print classifier
    
    def fit(self, X, y, prune=False):
        self._fit_predict(X, y, prune, True)

    def predict(self, X, y, prune=False):
        self._fit_predict(X, y, prune, False)

    def _fit_predict(self, X, y, prune=False, fit=True):

        #Just keep iterating until we hit the bottom
        for pos, level in enumarate(self.classifiers):

            level_predictions = list()

            for classifier in level:
                
                if fit:
                    classifier.fit(X,y)

                    level_predictions.append(classifier.predict(X))

                else:
                    y = classfier.predict(X)
                    level_predictions.append(y)

                if prune and self.prune(classifier.score(X,y)):
                    del level_predictions[-1]
                    del self.classifiers[pos][self.classifiers.index(classifier)]

            # Over pruned, bail...
            if len(level_predictions) == 0:
                assert('ERROR: Over pruned classifiers none left!')

            X = level_predictions

        return level_predictions
    
    def _prune(self, score):
        if score > self.cutoff_:
            return True
        else:
            return False
