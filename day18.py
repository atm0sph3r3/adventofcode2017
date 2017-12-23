import queue
import threading
import copy
import time


def read_instructions(id, each_registers, opposing_queue, my_queue):
    current_instruction = 0
    sent = 0

    while True:
        action = instructions[current_instruction][0]
        register = instructions[current_instruction][1]
        value = 0

        if len(instructions[current_instruction]) == 3:
            value = instructions[current_instruction][2]
        else:
            value = instructions[current_instruction][1]

        if value.startswith('-') or value.isdigit():
            value = int(value)
        else:
            value = each_registers[value]

        if action == 'snd':
            opposing_queue.put(value)
            sent += 1
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
                if opposing_queue.empty():
                    if id == 1:
                        print(sent)
                    return
                continue
            each_registers[register] = my_queue.get()
        elif action == 'jgz':
            if (register.isdigit() and int(register) > 0) or each_registers[register] > 0:
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
        if split[1].isalpha():
            registers[split[1]] = 0

    queue_0 = queue.Queue()
    queue_1 = queue.Queue()
    registers_0 = copy.deepcopy(registers)
    registers_0['p'] = 0
    registers_1 = copy.deepcopy(registers)
    registers_1['p'] = 1

    thread_0 = threading.Thread(target=read_instructions, args=(0, registers_0, queue_1, queue_0))
    thread_0.start()
    thread_1 = threading.Thread(target=read_instructions, args=(1, registers_1, queue_0, queue_1))
    thread_1.start()

    while thread_1.is_alive() and thread_0.is_alive():
        continue
