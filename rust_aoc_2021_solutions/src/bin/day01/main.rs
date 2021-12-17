use std::{fs};
use rust_aoc_2021_solutions::PATH;
fn main() {
    let nums = parse_input(&(PATH.to_owned() + "day01/input1.txt")).unwrap();
    println!("Part one solution: {}", part1(&nums));
    println!("Part two solution: {}", part2(&nums));
}

fn parse_input(filename: &str) -> Result<Vec<u64>, String> {
    let text = fs::read_to_string(filename);
    match text {
        Ok(content) => Ok(content
            .lines()
            .map(|num| num.parse::<u64>().unwrap())
            .collect()),
        Err(err) => Err(err.to_string()),
    }
}
fn part1(nums: &Vec<u64>) -> u64 {
    let mut res = 0;
    for i in 1..nums.len() {
        if nums[i] > nums[i - 1] {
            res += 1;
        }
    }
    res
}

fn part2(nums: &Vec<u64>) -> u64 {
    let mut res = 0;
    let (mut a, mut b, mut c, mut d) = (nums[0], nums[1], nums[2], nums[3]);

    if a + b + c < b + c + d {
        res += 1;
    }

    for i in 4..nums.len() {
        a = b;
        b = c;
        c = d;
        d = nums[i];
        if a + b + c < b + c + d {
            res += 1;
        }
    }
    res
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_DATA: &str = "\
199
200
208
210
200
207
240
269
260
263";

    fn text_to_vec(text: &str) -> Vec<u64> {
        text.lines()
            .map(|num| num.parse::<u64>().unwrap())
            .collect()
    }

    #[test]
    fn test_part_one() {
        let nums = text_to_vec(TEST_DATA);
        assert_eq!(part1(&nums), 7);
    }

    #[test]
    fn test_part_two() {
        let nums = text_to_vec(TEST_DATA);
        assert_eq!(part2(&nums), 5)
    }
}
