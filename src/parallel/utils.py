import time
from queue import Empty
from threading import Thread


class Worker(Thread):
    def __init__(self, queue, dispatch):
        super().__init__(name="Worker")
        self.queue = queue
        self.dispatch = dispatch
        self._kill = False

    def kill(self):
        self._kill = True

    def run(self):
        while not self._kill:
            try:
                task = self.queue.get(block=False)
            except Empty:
                continue
            try:
                resp = self.dispatch(task)
                if resp is not None:
                    print(resp)
            except:
                self.queue.task_done()
                raise


class Pool:
    def __init__(self, queue, dispatch, n_workers=10) -> None:
        self.queue = queue
        self.workers = [Worker(queue, dispatch) for _ in range(n_workers)]

    def start(self):
        [worker.start() for worker in self.workers]

    def end(self, force=False):
        if not force:
            while not self.queue.empty():
                time.sleep(0.1)
        [worker.kill() for worker in self.workers]
        [worker.join() for worker in self.workers]


class BaseConsumer:
    def __init__(self, queue, n_workers=10) -> None:
        self.queue = queue
        self.workers = Pool(self.queue, self.dispatch, n_workers=n_workers)

    def dispatch(self, event):
        raise NotImplementedError

    def start(self):
        self.workers.start()

    def end(self, force=False):
        self.workers.end(force)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, type, value, traceback):
        self.end()
