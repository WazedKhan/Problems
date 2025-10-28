# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is a multi-platform problem-solving repository containing solutions from LeetCode, HackerRank, GeeksforGeeks, Codeforces, and other competitive programming platforms. Solutions are primarily written in **Python** with growing **Go** support.

## Essential Commands

### Python

**Setup:**
```bash
pip install -r requirements.txt
```

**Run all tests:**
```bash
pytest
```

**Run specific test file:**
```bash
pytest tests/test_leetcode.py
```

**Run single test by name:**
```bash
pytest tests/test_leetcode.py::test_two_sum -v
```

**Run with coverage:**
```bash
pytest --cov
```

**Format code (pre-commit hooks):**
```bash
# Format with Black (line length: 140)
black --preview --line-length=140 <file>.py

# Check with flake8
flake8 --max-line-length=140 --ignore=E203,W503 <file>.py

# Sort imports
isort --profile black <file>.py

# Lint with ruff
ruff --line-length=140 --fix <file>.py
```

**Run pre-commit hooks manually:**
```bash
pre-commit run --all-files
```

### Go

**Run tests:**
```bash
cd Go && go test -v ./...
```

**Run tests with coverage:**
```bash
cd Go && go test -v -race -coverprofile=coverage.out ./...
```

**View coverage:**
```bash
cd Go && go tool cover -func=coverage.out
```

**Format and vet:**
```bash
cd Go && go fmt ./... && go vet ./...
```

**Verify dependencies:**
```bash
cd Go && go mod tidy && go mod verify
```

## Code Architecture

### Directory Structure

- **LeetCode/**: Contains solutions organized by difficulty
  - Root level: Mix of easy/medium problems (legacy structure)
  - `easy/`: Easy difficulty problems
  - `medium/`: Medium difficulty problems
- **HackerRank/**: HackerRank problem solutions
- **GeeksforGeeks/**: GeeksforGeeks problem solutions
- **Codeforces/**: Codeforces contest solutions
- **DSA/**: Data structures and algorithms implementations
- **Go/**: Go language solutions for selected problems
- **tests/**: Pytest test suites
  - `test_leetcode.py`: Primary test file for LeetCode solutions
  - `test_leetcode_easy.py`: Tests for easy problems
  - `test_hacker_rank.py`: HackerRank tests
- **Goal/**: Personal practice and goal tracking

### Solution File Naming

Python solutions follow these patterns:
- `problem_name_number.py` (e.g., `two_sum_01.py`, `happy_number_202.py`)
- `ProblemName.py` (e.g., `SingleNumber.py`, `ContainsDuplicate.py`)

Go solutions:
- Located in `Go/` directory
- Functions use PascalCase (e.g., `RemoveDuplicates`, `SearchInsert`)
- Test files: `*_test.go`

### Solution Structure

**Python:**
```python
# source: [URL to problem]
from typing import List

class Solution:
    def methodName(self, param: type) -> return_type:
        # Implementation with comments explaining approach
        pass
```

**Go:**
```go
// URL: [problem URL]
// Python Solution: [path to equivalent Python solution]
func FunctionName(params) returnType {
    // Implementation
}
```

### Testing Structure

Tests use pytest with parametrization:
```python
@pytest.mark.parametrize("input, expected", [
    (test_case_1, result_1),
    (test_case_2, result_2),
])
def test_function_name(input, expected):
    from module.file import Solution
    solution = Solution()
    assert solution.method(input) == expected
```

## Development Workflow

1. **Adding a new Python solution:**
   - Create solution file in appropriate directory (LeetCode/easy, LeetCode/medium, etc.)
   - Follow naming convention: `problem_name_number.py`
   - Include problem URL as comment
   - Implement solution in `Solution` class
   - Add parametrized test in `tests/test_leetcode.py`
   - Run tests: `pytest tests/test_leetcode.py::test_new_function -v`

2. **Adding a new Go solution:**
   - Add function to `Go/leetcode.go` or create separate file
   - Include problem URL and reference to Python solution
   - Create corresponding test in `Go/leetcode_test.go` or `*_test.go`
   - Run: `cd Go && go test -v ./...`

3. **Before committing:**
   - Pre-commit hooks automatically run Black, flake8, isort, and ruff
   - Ensure all tests pass: `pytest`
   - For Go: `cd Go && go fmt ./... && go vet ./...`

## Code Style

### Python
- **Line length:** 140 characters (configured in Black and flake8)
- **Import sorting:** isort with Black profile
- **Formatter:** Black with preview mode enabled
- **Linter:** flake8 (ignoring E203, W503) and ruff
- **Type hints:** Use typing module for function signatures

### Go
- **Standard Go formatting:** Use `go fmt`
- **Module:** `github.com/wazedkhan/Problems/Go`
- **Go version:** 1.24.3

## Testing Philosophy

- Every solution should have comprehensive test cases covering:
  - Basic test cases from problem description
  - Edge cases (empty inputs, single elements, max/min values)
  - Invalid or boundary inputs
  - Performance edge cases where applicable
- Use parametrize for multiple test scenarios
- Tests import from solution modules using relative imports

## CI/CD

GitHub Actions workflow (`.github/workflows/tests.yml`) runs on every push:
- **Python tests:** Runs pytest with Python 3.12.3
- **Go tests:** Runs go test with coverage, uploads coverage artifacts

## Problem Organization

Solutions reference the original problem source and difficulty:
- LeetCode problems include problem number (e.g., `two_sum_01.py` for Problem #1)
- Problem descriptions sometimes preserved in markdown files (e.g., `HackerRank/effcientJanitor.md`)
- `target.md` contains study topics for interviews and competitive programming

## Cross-Language Implementation

Many problems have both Python and Go implementations. When implementing in Go:
- Reference the Python solution file in comments
- Maintain equivalent test coverage
- Follow idiomatic Go patterns while preserving algorithmic approach
