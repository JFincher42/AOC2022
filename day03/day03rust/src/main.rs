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

    // Explore changing this to use
    //   let input = fs::read_to_string(format!("data/day{}.txt", n)).expect("read failed");
    // followed by
    //   input.lines()
    // To get the lines out of it
    // then
    //   part1(&input)

    println!("Part 1: {}", part1(reader));

}

fn part1(reader: BufReader<File>) -> u32 {

    let mut priority = 0;

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
    priority
}
