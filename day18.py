import queue
import threading
import time


def read_instructions(each_registers, opposing_queue, my_queue):
    current_instruction = 0
    sent = 0
    while True:
        action = instructions[current_instruction][0]
        register = instructions[current_instruction][1]
        value = 0
        if len(instructions[current_instruction]) == 3:
            value = instructions[current_instruction][2]
            if str(value).startswith('-') or value.isdigit():
                value = int(value)
            else:
                value = each_registers[value]

        if action == 'snd':
            opposing_queue.put(value)
            sent += 1
            print(sent)
        elif action == 'set':
            each_registers[register] = value
        elif action == 'add':
            each_registers[register] += value
        elif action == 'mul':
            each_registers[register] *= value
        elif action == 'mod':
            each_registers[register] %= value
        elif action == 'rcv':
            while my_queue.empty():
                continue
            each_registers[register] = my_queue.pop()
        elif action == 'jgz':
            if each_registers[register] > 0:
                current_instruction += value
            else:
                current_instruction += 1
        else:
            raise RuntimeError('Invalid instruction')

        if action != 'jgz':
            current_instruction += 1


registers = dict()
instructions = list()

with open("resources/day18", "rt") as f:
    for line in f:
        split = line.split()
        instructions.append(split)
        registers[split[1]] = 0

    queue_0 = queue.Queue()
    queue_1 = queue.Queue()
    registers_0 = dict(registers)
    registers_0['p'] = 0
    registers_1 = dict(registers)
    registers_1['p'] = 1

    thread_0 = threading.Thread(target=read_instructions, args=(registers_0, queue_1, queue_0))
    thread_0.daemon = True
    thread_0.start()
    time.sleep(5)
    thread_1 = threading.Thread(target=read_instructions, args=(registers_1, queue_0, queue_1))
    thread_1.daemon = True
    thread_1.start()

    while queue_0.empty() and queue_1.empty():
        continue

