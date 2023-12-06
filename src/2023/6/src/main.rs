use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

fn lines_from_file(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

struct Race {
    time: i64,
    distance: i64
}

fn map_file_to_races(lines: &Vec<String>) -> Vec<Race> {
    let times: Vec<i64> = lines.get(0).unwrap()
        .split_whitespace()
        .skip(1)
        .map(|f| -> i64 { f.parse().unwrap() })
        .collect();
    let distances: Vec<i64> = lines.get(1).unwrap()
        .split_whitespace()
        .skip(1)
        .map(|f| -> i64 { f.parse().unwrap() })
        .collect();

    let mut races: Vec<Race> = Vec::new();
    for i in 0..times.len() {
        races.push(Race { time: *times.get(i).unwrap(), distance: *distances.get(i).unwrap() });
    }
    races
}

fn map_file_to_races_p2(lines: &Vec<String>) -> Vec<Race> {
    let time = lines.get(0).unwrap()
        .replace("Time:", "")
        .replace(" ", "")
        .parse()
        .unwrap();
    let distance = lines.get(1).unwrap()
        .replace("Distance:", "")
        .replace(" ", "")
        .parse()
        .unwrap();

    let mut races = Vec::with_capacity(1);
    races.push(Race { time, distance });
    races
}

fn calc_count(start: i64, end: i64, step: i64, target: i64) -> i64 {
    let mut count = 0;

    for i in (start..end).step_by(step as usize) {
        if i * (end - i) > target {
            count += 1;
        }
    }

    count
}

fn calc_aggregate(races: &[Race]) -> i64 {
    let mut aggregate = 1;
    for race in races {
        aggregate *= calc_count(0, race.time, 1, race.distance);
    }
    aggregate
}

fn main() {
    let file_content = lines_from_file("input.txt");
    let races_p1 = map_file_to_races(&file_content);
    let races_p2 = map_file_to_races_p2(&file_content);

    println!("Part 1: {}", calc_aggregate(&races_p1));
    println!("Part 2: {}", calc_aggregate(&races_p2));
}
