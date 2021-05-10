from queue import Queue
from typing import Dict, List

from .utils import BaseConsumer


class CustomConsumer(BaseConsumer):
    def __init__(self, queue: Queue, n_workers: int) -> None:
        super().__init__(queue, n_workers=n_workers)
        self.state: Dict[str, List] = {"cats": []}

    # def dispatch(self, event):
    #     match event.get("action"):
    #         case "read":
    #             return event["data"]
    #         case "get":
    #             resp = requests.get(event["data"])
    #             self.state["cats"].append(resp.json()["text"])
    #         case _:
    #             raise Exception("No defined action")


if __name__ == "__main__":
    q: Queue = Queue()
    with CustomConsumer(q, n_workers=5) as cc:
        for _ in range(5):
            q.put({"action": "get", "data": "https://cat-fact.herokuapp.com/facts/random"})

    print(cc.state)
