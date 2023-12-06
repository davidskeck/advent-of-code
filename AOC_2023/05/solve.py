# Advent of Code 2023
# Day 05

import time
from multiprocessing import Process, Queue

import pyperclip

input_files = [
    "example.txt",
    "input.txt"
]


def seed_processor(seed_range, mappings, answer_queue, percentage_queue):
    # seeds_tested = 0
    answer = float('inf')
    for i in range(seed_range[0], seed_range[0] + seed_range[1]):
        curr_value = i
        for mapping in mappings:
            for span in mapping.ranges:
                if span.source_start <= curr_value and curr_value <= span.source_start + span.span:
                    curr_value += (span.destination_start - span.source_start)
                    break
        # seeds_tested += 1
        # if seeds_tested % 100000 == 0:
        #     percentage_queue.put_nowait((seed_range[0], seeds_tested))
        if curr_value < answer:
            answer = curr_value
    
    # percentage_queue.put_nowait((seed_range[0], seeds_tested))
    answer_queue.put(answer)


def progress_writer(total_seeds, percentage_queue):
    progress_dict = {}
    while True:
        if not percentage_queue.empty():
            name, percentage = percentage_queue.get()
            progress_dict[name] = percentage
            seeds_tested = sum(progress_dict.values())
            print(f"Percent complete: {seeds_tested / total_seeds:.2f}% ({seeds_tested}/{total_seeds}) {percentage_queue.qsize()}", end='\r')


class Range:
    def __init__(self, line):
        self.destination_start = int(line.split()[0])
        self.source_start = int(line.split()[1])
        self.span = int(line.split()[2])


class GardenMapping:
    def __init__(self, mapping_data):
        self.source = mapping_data[0].split()[0].split('-')[0]
        self.destination = mapping_data[0].split()[0].split('-')[-1]
        self.ranges = []
        for line in mapping_data[1:]:
            self.ranges.append(Range(line))


def main(input_file):
    with open(input_file) as input_data:
        puzzle_input = [line for line in input_data.read().split('\n') if line != ""]

    # Part One
    answer = 0

    seeds = []
    mappings = []
    for index, line in enumerate(puzzle_input):
        if "seeds:" in line:
            for seed_name in line.split(':')[-1].strip().split():
                seeds.append(int(seed_name))
        elif "map:" in line:
            lookahead_index = index + 1
            while lookahead_index < len(puzzle_input) and "map:" not in puzzle_input[lookahead_index]:
                lookahead_index += 1
            mappings.append(GardenMapping(puzzle_input[index: lookahead_index]))

    answer = float('inf')
    for seed in seeds:
        curr_value = seed
        for mapping in mappings:
            for span in mapping.ranges:
                if span.source_start <= curr_value and curr_value <= span.source_start + span.span:
                    curr_value += (span.destination_start - span.source_start)
                    break
        
        if curr_value < answer:
            answer = curr_value

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part One: {answer}")

    # Part Two
    answer = 0

    seed_ranges = []
    mappings = []
    for index, line in enumerate(puzzle_input):
        if "seeds:" in line:
            seed_data = line.split(':')[-1].strip().split()
            for i in range(0, len(seed_data), 2):
                seed_ranges.append((int(seed_data[i]), int(seed_data[i+1])))

        elif "map:" in line:
            lookahead_index = index + 1
            while lookahead_index < len(puzzle_input) and "map:" not in puzzle_input[lookahead_index]:
                lookahead_index += 1
            mappings.append(GardenMapping(puzzle_input[index: lookahead_index]))
    
    total_seeds = 0
    for seed_range in seed_ranges:
        total_seeds += seed_range[1]

    seeds_tested = 0
    answer = float('inf')
    answer_queue = Queue()
    percentage_queue = Queue()
    seed_processors = []
    
    # WARNING: This will take about 5000 seconds to execute!
    # Didn't optimize because I wanted to see if the brute force solution was possible... It is... barely.
    for seed_range in seed_ranges:
        seed_range_length = seed_range[1]
        third_range = seed_range_length // 3
        for i in range(0, 3):
            if i < 2:
                new_range = (seed_range[0] + i * third_range, third_range)
            else:
                new_range = (seed_range[0] + i * third_range, seed_range[1] - (third_range * 2))
            processor = Process(target=seed_processor, args=(seed_range, mappings, answer_queue, percentage_queue))
            seed_processors.append(processor)
            processor.start()
    
    # progress_writer_process = Process(target=progress_writer, args=(total_seeds, percentage_queue), daemon=True)
    # progress_writer_process.start()

    for processor in seed_processors:
        processor.join()

    while not answer_queue.empty():
        curr_answer = answer_queue.get()
        if curr_answer < answer:
            answer = curr_answer

    pyperclip.copy(answer)
    print(f"{input_file.split('.')[0].capitalize()} Part Two: {answer}")


if __name__ == "__main__":
    for input_file in input_files:
        start_time = time.time()
        main(input_file)
        print(f"{input_file.split('.')[0].capitalize()} Time: {time.time() - start_time:.2f}s\n")
