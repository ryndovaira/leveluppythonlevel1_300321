from topic_07_oop.hw.class_4_2_worker import Worker

def test():
    name = 'Миша'
    salary = 56324.50
    position = "Инженер"

    worker = Worker(name, salary, position)

    assert len(worker) == 7

    assert (worker > worker) == False

    worker_tmp1 = Worker(name, salary + 1, position)
    assert (worker > worker_tmp1) == False
    assert (worker_tmp1 > worker) == True

    worker_tmp2 = Worker(name, salary - 1, position)
    assert (worker > worker_tmp2) == True
    assert (worker_tmp2 > worker) == False
