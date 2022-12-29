use std::{
    fs::File,
    io::{BufRead, BufReader},
};

fn main() {
    // Where are the files
    let _filename = "/home/jon/git/AOC2022/day01/day01rust/input";
    // let _filename = "/home/jon/git/AOC2022/day01/day01rust/sample";

    // Open the file
    let file = File::open(_filename).expect("Error opening file");
    let reader = BufReader::new(file);

    // Our current total and maximum
    let mut total: u32 = 0;
    let mut maximum: u32 = 0;
    let mut max2: u32 = 0;
    let mut max3: u32 = 0;

    // Let's read each line
    // If we see a blank line, we check the total against the maximum
    // Otherwise we add the value of that line to our current total
    for line in reader.lines() {
        // Unwrap this line
        let line = line.unwrap();

        // Check for blank
        if line.len() == 0 {
            // Check our total against all three maximums
            if total > maximum {
                max3 = max2;
                max2 = maximum;
                maximum = total;
            } else if total > max2 {
                max3 = max2;
                max2 = total;
            } else if total > max3 {
                max3 = total;
            }

            // Zero total for the next round
            total = 0;
        } else {
            total = total + line.parse::<u32>().unwrap();
        }
    }

    // Check our total one more time
    if total > maximum {
        max3 = max2;
        max2 = maximum;
        maximum = total;
    } else if total > max2 {
        max3 = max2;
        max2 = total;
    } else if total > max3 {
        max3 = total;
    }

    println!("Part1: {}", maximum);
    println!("Part2: {}", maximum + max2 + max3);
}
