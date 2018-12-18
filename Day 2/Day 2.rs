// Notes:
// First time to use Rust
// Some difficulty with the includes and understanding conditionals
// they are a bit different than Swift's conditionals.
// Created using rustc 1.30.1 (1433507eb 2018-11-07)
use std::collections::btree_map::BTreeMap;

fn main()
{
    let input: Vec<_> = include_str!("input.txt").lines().collect();
    let mut num_two = 0;
    let mut num_three = 0;

    for line in input
    {
    	let mut two_found = false;
    	let mut three_found = false;
    	let mut letter_counts = BTreeMap::new();
        for character in line.chars()
        {
            *letter_counts.entry(character).or_insert(0) += 1;
        }
        for (_, count) in letter_counts
        {
        	if count == 2 && !two_found
        	{
        	    two_found = true;
        	    num_two += 1;
        	}
        	if count == 3 && !three_found
        	{
                three_found = true;
                num_three += 1;
        	}
        	if two_found && three_found
        	{
        		break;
        	}
        }
    }
    print!("Part one: {}\n", num_two * num_three);
    
    
}
