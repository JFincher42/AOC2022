use std::{
    fs::File,
    io::{BufRead, BufReader},
    collections::HashSet,
};

fn main() {
    // Where are the files
    let _filename = "/home/jon/git/AOC2022/day03/day03rust/input";
    // let _filename = "/home/jon/git/AOC2022/day03/day03rust/sample";

    // Open the file
    let file = File::open(_filename).expect("Error opening file");
    let reader = BufReader::new(file);

    // Our total is here
    let mut priority:u32 = 0;

    // Process every line
    for line in reader.lines() {
        // Unwrap the line
        let line = String::from(line.unwrap().trim());

        // Get the first and second halves
        let first = &line[..line.len() / 2];
        let second = &line[line.len() / 2..];

        // Get the unique letters in each word
        let mut first_letters = HashSet::new();
        for letter in first.as_bytes(){
            first_letters.insert(letter);
        }

        let mut second_letters = HashSet::new();
        for letter in second.as_bytes(){
            second_letters.insert(letter);
        }

        // Find the union
        for common in first_letters.intersection(&second_letters){
            if common.is_ascii_lowercase(){
                priority = priority + (**common as u32) - ('a' as u32) + 1;
            } else {
                priority = priority + (**common as u32) - ('A' as u32) + 27;
            }
        }

    }

    println!("Part 1: {}", priority)

}
