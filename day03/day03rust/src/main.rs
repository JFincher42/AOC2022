use std::{collections::HashSet, fs::read_to_string};

fn main() {
    // Where are the files
    let _filename = "/home/jon/git/AOC2022/day03/day03rust/input";
    // let _filename = "/home/jon/git/AOC2022/day03/day03rust/sample";

    let input = read_to_string(_filename).expect("read failed");
    println!("Part 1: {}", part1(&input));

    // Since input was borrowed, we should be able to use in part2 as well...

    println!("Part 2: {}", part2(&input));
}

// I'm using the same technique for Part 1 and Part 2, but with different strings
// I took Part 2 from a Reddit solution so I could understand the Rust syntax
// Then I ported it to Part 1
// I used the same technique in my Python solution

fn part1(input: &String) -> u32 {
    // We borrow the input string here so we can use it again

    // Our eventual return value
    let mut priority = 0;

    // Process every line
    for line in input.lines() {
        // Get the first and second halves
        // We can optimize this away with the lines that build the sets
        let first = &line.trim()[..line.len() / 2];
        let second = &line.trim()[line.len() / 2..];

        // Get the unique letters in the first half of the word
        let mut first_letters: HashSet<char> = first.chars().collect();

        // Same for the second
        let second_letters: HashSet<char> = second.chars().collect();

        // Only keep the characters which are in both
        // This uses a comprehension (called a closure in Rust)
        // Basically is means get every x where the temp char set contains x
        first_letters.retain(|x| second_letters.contains(x));

        // At this point, charset should have one and only one character in it
        if first_letters.len() > 1 {
            // We should never ever be here...
            unreachable!();
        }

        let common = first_letters.iter().next().unwrap();
        if common.is_ascii_lowercase() {
            priority = priority + (*common as u32) - ('a' as u32) + 1;
        } else {
            priority = priority + (*common as u32) - ('A' as u32) + 27;
        }
    }
    priority
}

fn part2(input: &String) -> u32 {
    // Our eventual return value
    let mut priority = 0;

    // We need to turn our input string into a vector
    // This gets each line from the input iterator as a &str
    // Maps them to String, then turns them into a collection
    let lines: Vec<String> = input.lines().map(String::from).collect();

    // We need to look at each group of three elves
    // This is better than looping through with an step 3 iterator
    // .chunks returns an array slice, which is a reference by default
    let groups: Vec<&[String]> = lines.chunks(3).collect();

    // Each group in the above vector is actually a reference to an array of Strings
    for group in groups {
        // Get all the chars from the first line
        let mut charset: HashSet<char> = group[0].chars().collect();

        // Now let's check the second and third.
        for item in &group[1..] {
            // Generate a new set from the characters in each group
            let tempcharset: HashSet<char> = item.chars().collect();

            // Only keep the characters which are in both
            // This uses a comprehension (called a closure in Rust)
            // Basically is means get every x where the temp char set contains x
            charset.retain(|x| tempcharset.contains(x));
        }

        // At this point, charset should have one and only one character in it
        if charset.len() > 1 {
            // We should never ever be here...
            unreachable!();
        }

        let common = charset.iter().next().unwrap();
        if common.is_ascii_lowercase() {
            priority = priority + (*common as u32) - ('a' as u32) + 1;
        } else {
            priority = priority + (*common as u32) - ('A' as u32) + 27;
        }
    }

    priority
}
