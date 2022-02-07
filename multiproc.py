import multiprocessing


class Process(multiprocessing.Process):
    def run(self):
        print('work')


pr = Process()
pr.start()
