class Reading:
    history: list[int]

    layers: list[list[int]]

    def __init__(self, line: str):
        self.history = [int(_) for _ in line.split(' ')]
        self.layers = []

    def __repr__(self):
        return f'Reading(history={self.history})'

    def predict_next(self) -> int:
        """Predict forward."""
        self.layers[-1].append(self.layers[-1][-1])
        for i in reversed(range(0, len(self.layers) - 1)):
            _layer = self.layers[i]
            _next_value = _layer[-1] + self.layers[i + 1][-1]
            _layer.append(_next_value)
        return self.layers[0][-1]

    def predict_previous(self) -> int:
        """Predict backward."""
        self.layers[-1].insert(0, self.layers[-1][0])
        for i in reversed(range(0, len(self.layers) - 1)):
            _layer = self.layers[i]
            _next_value = _layer[0] - self.layers[i + 1][0]
            _layer.insert(0, _next_value)
        return self.layers[0][0]

    def build_layers(self):
        _done = False
        self.layers.append(self.history)
        while not _done:
            _upper_layer = self.layers[-1]
            _layer = []
            for i in range(0, len(_upper_layer) - 1, 1):
                _layer.append(_upper_layer[i + 1] - _upper_layer[i])

            if _layer.count(0) == len(_layer):
                _done = True
            else:
                self.layers.append(_layer)
