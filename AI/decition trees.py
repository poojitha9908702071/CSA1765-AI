class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def fit(self, X, y):
        """Train the decision tree."""
        data = [x + [label] for x, label in zip(X, y)]
        self.tree = self._build_tree(data, depth=0)

    def predict(self, X):
        """Predict the labels for given data."""
        return [self._classify(self.tree, x) for x in X]

    def _build_tree(self, data, depth):
        """Recursively build the decision tree."""
        labels = [row[-1] for row in data]
        if len(set(labels)) == 1:  # Pure split
            return labels[0]

        if self.max_depth is not None and depth >= self.max_depth:  # Max depth reached
            return max(set(labels), key=labels.count)

        feature_index, threshold = self._best_split(data)
        if feature_index is None:  # No valid split
            return max(set(labels), key=labels.count)

        left_split, right_split = self._split(data, feature_index, threshold)
        return {
            'feature_index': feature_index,
            'threshold': threshold,
            'left': self._build_tree(left_split, depth + 1),
            'right': self._build_tree(right_split, depth + 1)
        }

    def _best_split(self, data):
        """Find the best split point."""
        best_gain = 0
        best_feature, best_threshold = None, None
        current_uncertainty = self._gini([row[-1] for row in data])

        for feature_index in range(len(data[0]) - 1):
            thresholds = set(row[feature_index] for row in data)
            for threshold in thresholds:
                left, right = self._split(data, feature_index, threshold)
                if not left or not right:
                    continue

                gain = self._information_gain(left, right, current_uncertainty)
                if gain > best_gain:
                    best_gain, best_feature, best_threshold = gain, feature_index, threshold

        return best_feature, best_threshold

    def _split(self, data, feature_index, threshold):
        """Split data into left and right groups."""
        left = [row for row in data if row[feature_index] <= threshold]
        right = [row for row in data if row[feature_index] > threshold]
        return left, right

    def _gini(self, labels):
        """Calculate the Gini impurity."""
        counts = {label: labels.count(label) for label in set(labels)}
        impurity = 1 - sum((count / len(labels))**2 for count in counts.values())
        return impurity

    def _information_gain(self, left, right, current_uncertainty):
        """Calculate the information gain."""
        p = len(left) / (len(left) + len(right))
        return current_uncertainty - p * self._gini([row[-1] for row in left]) - (1 - p) * self._gini([row[-1] for row in right])

    def _classify(self, node, row):
        """Classify a row using the decision tree."""
        if not isinstance(node, dict):
            return node

        if row[node['feature_index']] <= node['threshold']:
            return self._classify(node['left'], row)
        else:
            return self._classify(node['right'], row)


# Example Usage
if __name__ == "__main__":
    # Training data: [feature1, feature2, ..., featureN, label]
    X = [
        [2.771244718, 1.784783929],
        [1.728571309, 1.169761413],
        [3.678319846, 2.81281357],
        [3.961043357, 2.61995032],
        [2.999208922, 2.209014212],
        [7.497545867, 3.162953546],
        [9.00220326, 3.339047188],
        [7.444542326, 0.476683375],
        [10.12493903, 3.234550982],
        [6.642287351, 3.319983761]
    ]
    y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    # Fit decision tree
    tree = DecisionTree(max_depth=3)
    tree.fit(X, y)

    # Predict new data
    predictions = tree.predict([
        [3.0, 2.0],
        [8.0, 3.0]
    ])
    print("Predictions:", predictions)
