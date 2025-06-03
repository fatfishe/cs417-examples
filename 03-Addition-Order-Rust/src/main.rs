use rand::prelude::*;

pub fn perform_addition_1(x: f32, y: f32, z: f32) -> f32 {
    let x_plus_y = x + y;

    x_plus_y + z
}

pub fn perform_addition_2(x: f32, y: f32, z: f32) -> f32 {
    let y_plus_z = y + z;

    x + y_plus_z
}

pub fn perform_addition_3(x: f32, y: f32, z: f32) -> f32 {
    let x_plus_z = x + z;

    x_plus_z + y
}

pub fn differ_more_than_tolerance(num_1: f32, num_2: f32, tolerance: f32) -> bool {
    (num_1 - num_2).abs() > tolerance
}

fn main() {
    const EPS: f32 = 1e-12;

    let mut rng = rand::rng();

    println!(
        "|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|{:^16}|{:^20}|",
        "x", "y", "z", "(x + y) + z", "x + (y + z)", "(x + z) + y", "Difference Found"
    );

    for _ in 0..16 {
        let (x, y, z) = (
            rng.random::<f32>(),
            rng.random::<f32>(),
            rng.random::<f32>(),
        );

        let result_1 = perform_addition_1(x, y, z);
        let result_2 = perform_addition_2(x, y, z);
        let result_3 = perform_addition_3(x, y, z);

        let results_differ = (differ_more_than_tolerance(result_1, result_2, EPS)
            || differ_more_than_tolerance(result_1, result_3, EPS)
            || differ_more_than_tolerance(result_2, result_3, EPS));

        println!(
            "|{x:16.12}|{y:16.12}|{z:16.12}|{:16.12}|{:16.12}|{:16.12}|{:^20}|",
            result_1,
            result_2,
            result_3,
            if results_differ { "Yes" } else { "" }
        );
    }
}
