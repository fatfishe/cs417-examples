pub const EPS: f32 = 1e-12;

pub trait FloatingPointDiffer {
    fn differ_more_than(self, tolerance: f32) -> bool;
}

impl FloatingPointDiffer for (f32, f32) {
    fn differ_more_than(self, tolerance: f32) -> bool {
        (self.0 - self.1).abs() > tolerance
    }
}
