import json


class Rating:

    @staticmethod
    def from_string(text: str):
        return json.loads(text.replace('=', ':').replace('x', '\"x\"')
                          .replace('m', '\"m\"').replace('a', '\"a\"')
                          .replace('s', '\"s\"'))


class Rule:
    condition = 'x'
    out_workflow: str

    def __init__(self, condition: str, out_workflow: str):
        self.condition = condition
        self.out_workflow = out_workflow

    def apply(self, x: int, m: int, a: int, s: int):
        result = bool(eval(self.condition))
        return self.out_workflow if result else None

    def __repr__(self):
        return f'Rule({self.condition} -> {self.out_workflow})'


class Workflow:
    name: str
    rules: list[Rule]
    out_workflow: str

    def __init__(self, line: str):
        self.name = line.split('{')[0]

        ruleset = line.split('{')[1].replace('}', '').split(',')
        self.out_workflow = ruleset.pop()
        self.rules = [Rule(x.split(':')[0], x.split(':')[1]) for x in ruleset]

    def apply(self, rating: dict):
        # for rule in self.rules:
        for rule in self.rules:
            result = rule.apply(rating['x'], rating['m'], rating['a'], rating['s'])

            if result is not None:
                return result

        return self.out_workflow
