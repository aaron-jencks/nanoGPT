import json


class Checkpoint:
    def __init__(self, step: int, total: int, offset: int):
        self.step = step
        self.total = total
        self.offset = offset

    def to_file(self, filename: str):
        with open(filename, 'w+') as fp:
            json.dump({'step': self.step, 'total': self.total, 'offset': self.offset}, fp)


def load_checkpoint(filename: str) -> Checkpoint:
    with open(filename, 'r') as fp:
        data = json.load(fp)
        return Checkpoint(data['step'], data['total'], data['offset'])
