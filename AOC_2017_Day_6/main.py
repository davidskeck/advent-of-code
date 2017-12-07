def main():
    puzzle_input = open("puzzle_input.txt")
    puzzle_input_list = []

    for line in puzzle_input:
        for block in line.split():
            puzzle_input_list.append(int(block))

    puzzle_input.close()

    # Parts One & Two

    memory_blocks = puzzle_input_list[:]
    previous_block_arrangements = []
    cycle_count = 0
    while True:
        largest_block = 0

        for block in memory_blocks:
            if block > largest_block:
                largest_block = block

        index_of_largest = memory_blocks.index(largest_block)
        largest_block_count = memory_blocks[index_of_largest]
        previous_block_arrangements.append(memory_blocks[:])

        memory_blocks[index_of_largest] = 0

        for i in range(largest_block_count):
            redistribution_index = index_of_largest + i + 1  # Don't write self
            if redistribution_index > len(memory_blocks) - 1:
                redistribution_index = redistribution_index % len(memory_blocks)

            memory_blocks[redistribution_index] += 1

        cycle_count += 1

        if memory_blocks in previous_block_arrangements:
            print("First infinite loop occurred after {} cycles... oops!".format(cycle_count))
            print("Next infinite loop occurs every {} cycles.".format(len(previous_block_arrangements) -
                                                                      previous_block_arrangements.index(memory_blocks)))
            break


main()
