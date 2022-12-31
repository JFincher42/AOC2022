use std::{
    fs::File,
    io::{BufRead, BufReader},
    collections::HashMap,
};

fn main() {
    // Where are the files
    let _filename = "/home/jon/git/AOC2022/day02/day02rust/input";
    // let _filename = "/home/jon/git/AOC2022/day02/day02rust/sample";

    // Open the file
    let file = File::open(_filename).expect("Error opening file");
    let reader = BufReader::new(file);

    // Let's define our maps
    let mut scores = HashMap::new();
    scores.insert(String::from("A X"), 4);
    scores.insert(String::from("A Y"), 8);
    scores.insert(String::from("A Z"), 3);
    scores.insert(String::from("B X"), 1);
    scores.insert(String::from("B Y"), 5);
    scores.insert(String::from("B Z"), 9);
    scores.insert(String::from("C X"), 7);
    scores.insert(String::from("C Y"), 2);
    scores.insert(String::from("C Z"), 6);

    let mut scores2= HashMap::new();
    scores2.insert(String::from("A X"), 3);
    scores2.insert(String::from("A Y"), 4);
    scores2.insert(String::from("A Z"), 8);
    scores2.insert(String::from("B X"), 1);
    scores2.insert(String::from("B Y"), 5);
    scores2.insert(String::from("B Z"), 9);
    scores2.insert(String::from("C X"), 2);
    scores2.insert(String::from("C Y"), 6);
    scores2.insert(String::from("C Z"), 7);

    // Points for part1 and part2
    let mut sum1 = 0;
    let mut sum2 = 0;

    for line in reader.lines(){
        // Unwrap the line
        let line = String::from(line.unwrap().trim());

        // Look up each line in the map, and add the score
        sum1 += scores.get(&line).unwrap();
        sum2 += scores2.get(&line).unwrap();
    }

    println!("Part 1: {}", sum1);
    println!("Part 2: {}", sum2);

}
