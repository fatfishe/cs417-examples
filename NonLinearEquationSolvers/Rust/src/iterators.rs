use super::errors::InvariantError;

trait IterableStateAdapter {
    fn next_state(&mut self) -> Result<f64, InvariantError>;

    fn get_current_guess(&self) -> Option<f64>;
}

pub struct NewtonSolver<'a> {
    pub x_n: Option<f64>,
    f: Box<dyn 'a + Fn(f64) -> f64>,
    df: Box<dyn 'a + Fn(f64) -> f64>,
}

impl<'a> NewtonSolver<'a> {
    pub fn new(
        x_0: f64,
        math_f: &'a impl Fn(f64) -> f64,
        math_df: &'a impl Fn(f64) -> f64,
    ) -> Self {
        NewtonSolver {
            x_n: Some(x_0),
            f: Box::new(math_f),
            df: Box::new(math_df),
        }
    }

    pub fn iter_mut(&mut self) -> &mut Self {
        self
    }
}

impl<'a> IterableStateAdapter for NewtonSolver<'a> {
    fn next_state(&mut self) -> Result<f64, InvariantError> {
        let x_n = self.x_n.unwrap();
        let f = &self.f;
        let df = &self.df;

        let next_x_n = x_n - (f(x_n) / df(x_n));

        match next_x_n.is_finite() {
            false => Err(InvariantError::from("$df(x_n) == 0$")),
            true => {
                self.x_n = Some(next_x_n);
                Ok(next_x_n)
            }
        }
    }

    fn get_current_guess(&self) -> Option<f64> {
        self.x_n
    }
}

impl<'a> std::iter::Iterator for NewtonSolver<'a> {
    type Item = f64;

    fn next(&mut self) -> Option<Self::Item> {
        let current_guess = self.get_current_guess();

        if let Some(x_n) = current_guess {
            match self.next_state() {
                Ok(x_n) => self.x_n = Some(x_n),
                Err(_) => self.x_n = None,
            }
            return Some(x_n);
        }

        None
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    use hamcrest2::prelude::*;

    #[test]
    fn test_newton_solver_some() {
        let f = |x: f64| -> f64 { x.powf(2.0) };
        let df = |x: f64| -> f64 { 2.0 * x };

        let mut solver = NewtonSolver::new(-1.0, &f, &df);

        assert_eq!(solver.next(), Some(-1.0));
        assert_eq!(solver.next(), Some(-0.5));
        assert_eq!(solver.next(), Some(-0.25));
        assert_eq!(solver.next(), Some(-0.125));
        assert_eq!(solver.next(), Some(-0.0625));
    }

    #[test]
    fn test_newton_solver_none() {
        let f = |x: f64| -> f64 { x.powf(2.0) };
        let df = |x: f64| -> f64 { 2.0 * x };

        let mut solver = NewtonSolver::new(0.0, &f, &df);

        assert_eq!(solver.next(), Some(0.0));
        assert_eq!(solver.next(), None);
    }
}
