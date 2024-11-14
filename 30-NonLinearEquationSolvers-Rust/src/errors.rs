#[derive(Debug, Clone)]
pub struct InvariantError {
    msg: String,
}

impl InvariantError {
    pub fn new(msg: String) -> Self {
        InvariantError { msg }
    }
}

impl From<&str> for InvariantError {
    fn from(msg: &str) -> Self {
        InvariantError::new(msg.to_string())
    }
}

impl From<String> for InvariantError {
    fn from(msg: String) -> Self {
        InvariantError::new(msg)
    }
}
