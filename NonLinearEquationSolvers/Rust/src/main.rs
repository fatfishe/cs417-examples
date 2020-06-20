use std::env;
use nonlinear_equation_solvers::loop_monoliths;

fn main() {
    let (a, b) = __handle_cli_args();

    let (math_f, math_df) = __build_f_df();

    println!("# Bisection");
    match loop_monoliths::bisection(&math_f, a, b) {
        Ok((_num_iter, solution)) => {
            let fx = math_f(solution);

            print_solution(solution, fx);
        }
        Err(err) => {
            println!();
            println!("## Method Failed");
            println!("{:?}", err);
        }
    }

    println!();
    println!("# Regula Falsi (False Position)");
    match loop_monoliths::regula_falsi(&math_f, a, b) {
        Ok((_num_iter, solution)) => {
            let fx = math_f(solution);

            print_solution(solution, fx);
        }
        Err(err) => {
            println!();
            println!("## Method Failed");
            println!("{:?}", err);
        }
    }

    println!();
    println!("# Secant");
    match loop_monoliths::secant(&math_f, a, b) {
        Ok((_num_iter, solution)) => {
            let fx = math_f(solution);

            print_solution(solution, fx);
        }
        Err(err) => {
            println!();
            println!("## Method Failed");
            println!("{:?}", err);
        }
    }

    println!();
    println!("# Newton's Method");
    match loop_monoliths::newton(&math_f, &math_df, a) {
        Ok((_num_iter, solution)) => {
            let fx = math_f(solution);

            print_solution(solution, fx);
        }
        Err(err) => {
            println!();
            println!("## Method Failed");
            println!("{:?}", err);
        }
    }
}

/// Handle positional command line argument validation.
///
/// # Return
///     Tuple in the form (lower limit, upper limit)
fn __handle_cli_args() -> (f64, f64) {
    let args: Vec<String> = env::args().collect();

    if args.len() < 3 {
        eprintln!("Usage:\n    {} a b", args[0]);
        std::process::exit(1);
    }

    let limit_a = args[1]
        .parse::<f64>()
        .unwrap_or_else(|_err| std::process::exit(2));

    let limit_b = args[2]
        .parse::<f64>()
        .unwrap_or_else(|_err| std::process::exit(3));

    (limit_a, limit_b)
}

/// Print the solution (x) and f(x) under a subsection heading.
///
/// :param solution: approximate solution
/// :param fx_solution: f(solution)
fn print_solution(solution: f64, fx_solution: f64) {
    println!();
    println!("## Solution");
    println!("$x={:20.8}", solution);
    println!();
    println!("$f(x)={:20.8}", fx_solution);
    println!();
}

/// Wrapper function that returns two math style functions:
///
///   - f - a function in the form Real -> Real
///   - df - the derivative of f in the form Real -> Real
///
/// A where clause does not work...
///
/// <https://stackoverflow.com/questions/47514930/what-are-the-differences-between-an-impl-trait-argument-and-generic-function-par>
///
/// Rust lambdas/closures syntax is tied with C++'s shenanigans for frustration
///
fn __build_f_df() -> (impl Fn(f64) -> f64, impl Fn(f64) -> f64) {
    let f = |x: f64| -> f64 {
        // (x ** 2) - 1
        // Fraction(math.cos(x))
        // Fraction(math.log(x))  // can not have negative operand (Real)
        // x**5 - (7 * x)**2
        x.powf(2.0) - (3.0 * x) - 4.0
    };

    let df = Box::new(|x: f64| -> f64 {
        // 2 * x
        // Fraction(-1 * math.sin(x))
        // Fraction(numerator=1, denominator=x)
        // 5 * (x ** 4) - (14 * x)
        2.0 * x - 3.0
    });

    (f, df)
}

#[cfg(test)]
mod tests {
    use super::*;

    use hamcrest2::prelude::*;

    #[test]
    fn test_math_f() {
        let (math_f, _) = __build_f_df();

        assert_that!(math_f(0.0), close_to(-4.0, 1e-8));
        assert_that!(math_f(1.0), close_to(-6.0, 1e-8));
        assert_that!(math_f(2.0), close_to(-6.0, 1e-8));
    }

    #[test]
    fn test_math_df() {
        let (_, math_df) = __build_f_df();

        assert_that!(math_df(0.0), close_to(-3.0, 1e-8));
        assert_that!(math_df(1.0), close_to(-1.0, 1e-8));
        assert_that!(math_df(2.0), close_to(1.0, 1e-8));
    }
}
