from typing import List, Iterator
import os


INPUT_FILE = os.path.join(os.path.dirname(__file__), 'input.txt')
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), 'monad.py')


def read_functions(file: str = INPUT_FILE) -> Iterator[Iterator[str]]:
    """
    The arithmetic logic unit (ALU) will run the MOdel Number Automatic Detector program 
    (MONAD, your puzzle input).

    This function reads the input file and returns it function by function and line by line
    converted to Python code.
    """
    with open(file) as f:
        script = f.read()

    # Treat each block where input is read as a separate function
    blocks = script.split('inp w\n')[1:]

    for i, block in enumerate(blocks):
        lines = block.strip().split('\n')
        yield(alu_function(i, lines))


def alu_function(i: int, lines: List[str]) -> Iterator[str]:
    """
    This generator function creates a new Python functions with the given ALU 
    instructions converted to Python statements.
    """
    yield f'def solver{i}(w, x, y, z):'
    for line in lines:
        instruction, a, b = line.split(' ')

        if instruction == 'add':
            yield f'    {a} += {b}'
        elif instruction == 'mul':
            yield f'    {a} *= {b}'
        elif instruction == 'div':
            yield f'    {a} //= {b}'
        elif instruction == 'mod':
            yield f'    {a} %= {b}'
        elif instruction == 'eql':
            yield f'    {a} = int({a} == {b})'
        else:
            raise Exception(line)

    yield f'    return w, x, y, z'


if __name__ == '__main__':
    with open(OUTPUT_FILE, 'w') as out_file:
        out_file.write('# This file is autogenerated based on input.txt\n\n')
        for function in read_functions():
            for line in function:
                out_file.write(f'{line}\n')
                print(line)
            out_file.write('\n')
            print()