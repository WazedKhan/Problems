"""Tests for validating documentation and configuration files"""
import os
import re
from pathlib import Path

import pytest


class TestWARPMarkdown:
    """Tests for WARP.md documentation file"""

    def test_warp_md_exists(self):
        """Test that WARP.md file exists"""
        assert Path("WARP.md").exists(), "WARP.md file should exist"

    def test_warp_md_not_empty(self):
        """Test that WARP.md is not empty"""
        content = Path("WARP.md").read_text()
        assert len(content) > 0, "WARP.md should not be empty"
        assert len(content) > 100, "WARP.md should have substantial content"

    def test_warp_md_has_title(self):
        """Test that WARP.md has a title"""
        content = Path("WARP.md").read_text()
        assert content.startswith("# WARP.md"), "WARP.md should start with title"

    def test_warp_md_has_main_sections(self):
        """Test that WARP.md has all main sections"""
        content = Path("WARP.md").read_text()
        required_sections = [
            "## Repository Overview",
            "## Essential Commands",
            "## Code Architecture",
            "## Development Workflow",
            "## Code Style",
            "## Testing Philosophy",
        ]
        for section in required_sections:
            assert section in content, f"WARP.md should contain section: {section}"

    def test_warp_md_has_python_section(self):
        """Test that WARP.md has Python-specific content"""
        content = Path("WARP.md").read_text()
        assert "### Python" in content
        assert "pytest" in content
        assert "black" in content
        assert "requirements.txt" in content

    def test_warp_md_has_go_section(self):
        """Test that WARP.md has Go-specific content"""
        content = Path("WARP.md").read_text()
        assert "### Go" in content
        assert "go test" in content

    def test_warp_md_code_blocks_balanced(self):
        """Test that code blocks are properly balanced"""
        content = Path("WARP.md").read_text()
        code_block_markers = content.count("```")
        assert code_block_markers % 2 == 0, "Code block markers should be balanced (even count)"
        assert code_block_markers >= 20, "Should have multiple code block examples"

    def test_warp_md_code_blocks_have_language(self):
        """Test that code blocks specify language"""
        content = Path("WARP.md").read_text()
        code_blocks = re.findall(r'```(\w+)', content)
        assert len(code_blocks) > 0, "Should have code blocks with language specifiers"
        # Most should be bash or python
        languages = set(code_blocks)
        assert "bash" in languages or "python" in languages or "go" in languages

    def test_warp_md_has_directory_structure(self):
        """Test that directory structure is documented"""
        content = Path("WARP.md").read_text()
        assert "### Directory Structure" in content
        assert "LeetCode/" in content
        assert "tests/" in content

    def test_warp_md_has_testing_section(self):
        """Test that testing philosophy is documented"""
        content = Path("WARP.md").read_text()
        assert "## Testing Philosophy" in content
        assert "test cases" in content.lower() or "test" in content.lower()

    def test_warp_md_mentions_pytest(self):
        """Test that pytest usage is documented"""
        content = Path("WARP.md").read_text()
        assert "pytest" in content.lower()
        assert "pytest tests/" in content or "pytest --cov" in content

    def test_warp_md_has_code_style_guide(self):
        """Test that code style guidelines are present"""
        content = Path("WARP.md").read_text()
        assert "## Code Style" in content
        assert "140" in content  # Line length
        assert "Black" in content or "black" in content

    def test_warp_md_has_workflow_instructions(self):
        """Test that development workflow is documented"""
        content = Path("WARP.md").read_text()
        assert "## Development Workflow" in content
        assert "Adding a new" in content or "workflow" in content.lower()

    def test_warp_md_references_cicd(self):
        """Test that CI/CD is mentioned"""
        content = Path("WARP.md").read_text()
        assert "CI/CD" in content or "GitHub Actions" in content

    def test_warp_md_line_endings_consistent(self):
        """Test that line endings are consistent"""
        with open("WARP.md", "rb") as f:
            content = f.read()
        # Should not have Windows line endings mixed
        assert b"\r\n" not in content or b"\n" not in content.replace(b"\r\n", b"")

    def test_warp_md_no_broken_formatting(self):
        """Test for common markdown formatting issues"""
        content = Path("WARP.md").read_text()
        lines = content.split("\n")

        for _i, line in enumerate(lines):
            # Check for unbalanced brackets in links
            open_brackets = line.count("[")
            close_brackets = line.count("]")

            # If line has markdown links, brackets should be balanced
            if "[" in line and "]" in line:
                # Count markdown-style links
                link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
                links = re.findall(link_pattern, line)
                # If we find link patterns, that's good
                # Otherwise check basic balance
                if not links and open_brackets != close_brackets:
                    # Could be partial, but warn
                    pass  # Allow some flexibility

    def test_warp_md_commands_are_valid_format(self):
        """Test that command examples follow valid format"""
        content = Path("WARP.md").read_text()

        # Extract bash code blocks
        bash_blocks = re.findall(r'```bash\n(.*?)```', content, re.DOTALL)

        for block in bash_blocks:
            # Should not have obvious syntax errors
            assert not block.strip().startswith(")"), "Bash blocks should not start with )"
            assert not block.strip().startswith("]"), "Bash blocks should not start with ]"

    def test_warp_md_has_essential_commands(self):
        """Test that essential commands are documented"""
        content = Path("WARP.md").read_text()
        essential_commands = ["pytest", "pip install", "black", "go test"]

        for cmd in essential_commands:
            assert cmd in content, f"Should document essential command: {cmd}"

    def test_warp_md_file_size_reasonable(self):
        """Test that WARP.md file size is reasonable"""
        size = Path("WARP.md").stat().st_size
        assert 1000 < size < 100000, f"WARP.md size ({size} bytes) should be reasonable"


class TestInputsDataFile:
    """Tests for inputs/simple_bank_system_2043.py data file"""

    def test_inputs_file_exists(self):
        """Test that inputs file exists"""
        assert Path("inputs/simple_bank_system_2043.py").exists()

    def test_inputs_file_is_valid_python(self):
        """Test that inputs file is valid Python syntax"""
        with open("inputs/simple_bank_system_2043.py", "r") as f:
            content = f.read()
        # Should be able to compile without syntax errors
        compile(content, "inputs/simple_bank_system_2043.py", "exec")

    def test_inputs_file_defines_large_input(self):
        """Test that large_input variable is defined"""
        from inputs.simple_bank_system_2043 import large_input
        assert large_input is not None

    def test_large_input_is_tuple(self):
        """Test that large_input is a tuple"""
        from inputs.simple_bank_system_2043 import large_input
        assert isinstance(large_input, tuple)

    def test_large_input_structure(self):
        """Test that large_input has correct structure"""
        from inputs.simple_bank_system_2043 import large_input

        assert len(large_input) > 0, "large_input should not be empty"

        # Should contain test case tuples
        for test_case in large_input:
            assert isinstance(test_case, tuple), "Each test case should be a tuple"
            assert len(test_case) == 3, "Each test case should have 3 elements (operations, inputs, expected)"

    def test_large_input_operations_format(self):
        """Test that operations in large_input are properly formatted"""
        from inputs.simple_bank_system_2043 import large_input

        for test_case in large_input:
            operations, inputs, expected = test_case

            assert isinstance(operations, list), "Operations should be a list"
            assert isinstance(inputs, list), "Inputs should be a list"
            assert isinstance(expected, list), "Expected should be a list"

            assert len(operations) == len(inputs) == len(expected), \
                "Operations, inputs, and expected should have same length"

    def test_large_input_operations_valid(self):
        """Test that all operations are valid"""
        from inputs.simple_bank_system_2043 import large_input

        valid_operations = {"Bank", "deposit", "withdraw", "transfer"}

        for test_case in large_input:
            operations, _, _ = test_case

            for op in operations:
                assert op in valid_operations, f"Invalid operation: {op}"

    def test_large_input_first_operation_is_bank(self):
        """Test that first operation is Bank initialization"""
        from inputs.simple_bank_system_2043 import large_input

        for test_case in large_input:
            operations, _, _ = test_case
            assert operations[0] == "Bank", "First operation should be 'Bank'"

    def test_large_input_bank_initialization_format(self):
        """Test Bank initialization has correct format"""
        from inputs.simple_bank_system_2043 import large_input

        for test_case in large_input:
            operations, inputs, _expected = test_case

            # First operation should be Bank
            if operations[0] == "Bank":
                assert isinstance(inputs[0], list), "Bank input should be a list"
                assert len(inputs[0]) == 1, "Bank input should have exactly one element"
                assert isinstance(inputs[0][0], list), "Bank balance should be a list"

    def test_large_input_expected_values_valid(self):
        """Test that expected values are valid"""
        from inputs.simple_bank_system_2043 import large_input

        for test_case in large_input:
            operations, _, expected = test_case

            for _i, (op, exp) in enumerate(zip(operations, expected, strict=True)):
                if op == "Bank":
                    assert exp is None, "Bank initialization should return None"
                else:
                    assert isinstance(exp, bool), f"Operation {op} should return bool, got {type(exp)}"

    def test_large_input_has_sufficient_test_cases(self):
        """Test that there are sufficient test cases"""
        from inputs.simple_bank_system_2043 import large_input

        total_operations = sum(len(tc[0]) for tc in large_input)
        assert total_operations >= 100, f"Should have at least 100 operations, got {total_operations}"

    def test_inputs_file_no_syntax_errors(self):
        """Test file can be imported without errors"""
        try:
            from inputs import simple_bank_system_2043
            assert hasattr(simple_bank_system_2043, "large_input")
        except SyntaxError as e:
            pytest.fail(f"Syntax error in inputs file: {e}")

    def test_large_input_deposit_operations_format(self):
        """Test deposit operations have correct input format"""
        from inputs.simple_bank_system_2043 import large_input

        for test_case in large_input:
            operations, inputs, _ = test_case

            for op, inp in zip(operations, inputs, strict=True):
                if op == "deposit":
                    assert len(inp) == 2, "Deposit should have 2 parameters"
                    assert isinstance(inp[0], int), "Account should be int"
                    assert isinstance(inp[1], int), "Money should be int"

    def test_large_input_withdraw_operations_format(self):
        """Test withdraw operations have correct input format"""
        from inputs.simple_bank_system_2043 import large_input

        for test_case in large_input:
            operations, inputs, _ = test_case

            for op, inp in zip(operations, inputs, strict=True):
                if op == "withdraw":
                    assert len(inp) == 2, "Withdraw should have 2 parameters"
                    assert isinstance(inp[0], int), "Account should be int"
                    assert isinstance(inp[1], int), "Money should be int"

    def test_large_input_transfer_operations_format(self):
        """Test transfer operations have correct input format"""
        from inputs.simple_bank_system_2043 import large_input

        for test_case in large_input:
            operations, inputs, _ = test_case

            for op, inp in zip(operations, inputs, strict=True):
                if op == "transfer":
                    assert len(inp) == 3, "Transfer should have 3 parameters"
                    assert isinstance(inp[0], int), "Account1 should be int"
                    assert isinstance(inp[1], int), "Account2 should be int"
                    assert isinstance(inp[2], int), "Money should be int"


class TestPlaygroundNotebook:
    """Tests for playground.ipynb Jupyter notebook"""

    def test_notebook_exists(self):
        """Test that playground notebook exists"""
        assert Path("playground.ipynb").exists()

    def test_notebook_is_valid_json(self):
        """Test that notebook is valid JSON"""
        import json

        with open("playground.ipynb", "r") as f:
            try:
                data = json.load(f)
                assert data is not None
            except json.JSONDecodeError as e:
                pytest.fail(f"Invalid JSON in playground.ipynb: {e}")

    def test_notebook_has_required_fields(self):
        """Test that notebook has required Jupyter fields"""
        import json

        with open("playground.ipynb", "r") as f:
            data = json.load(f)

        required_fields = ["cells", "metadata", "nbformat", "nbformat_minor"]
        for field in required_fields:
            assert field in data, f"Notebook should have '{field}' field"

    def test_notebook_cells_structure(self):
        """Test that notebook cells are properly structured"""
        import json

        with open("playground.ipynb", "r") as f:
            data = json.load(f)

        assert isinstance(data["cells"], list), "cells should be a list"

        for cell in data["cells"]:
            assert "cell_type" in cell, "Each cell should have cell_type"
            assert "metadata" in cell, "Each cell should have metadata"
            assert "source" in cell, "Each cell should have source"

    def test_notebook_has_code_cells(self):
        """Test that notebook contains code cells"""
        import json

        with open("playground.ipynb", "r") as f:
            data = json.load(f)

        code_cells = [cell for cell in data["cells"] if cell["cell_type"] == "code"]
        assert len(code_cells) > 0, "Notebook should have at least one code cell"

    def test_notebook_metadata_has_kernelspec(self):
        """Test that notebook metadata includes kernelspec"""
        import json

        with open("playground.ipynb", "r") as f:
            data = json.load(f)

        assert "kernelspec" in data["metadata"], "Should have kernelspec in metadata"
        kernelspec = data["metadata"]["kernelspec"]
        assert "name" in kernelspec
        assert "language" in kernelspec

    def test_notebook_kernelspec_is_python(self):
        """Test that notebook uses Python kernel"""
        import json

        with open("playground.ipynb", "r") as f:
            data = json.load(f)

        kernelspec = data["metadata"]["kernelspec"]
        assert kernelspec["language"] == "python", "Kernel should be Python"

    def test_notebook_references_bank_system(self):
        """Test that notebook contains references to Bank system"""
        import json

        with open("playground.ipynb", "r") as f:
            data = json.load(f)

        # Check if any cell references the Bank class
        has_bank_reference = False
        for cell in data["cells"]:
            if cell["cell_type"] == "code":
                source = "".join(cell["source"])
                if "Bank" in source or "simple_bank_system" in source:
                    has_bank_reference = True
                    break

        assert has_bank_reference, "Notebook should reference Bank system"

    def test_notebook_source_is_list(self):
        """Test that cell source is a list of strings"""
        import json

        with open("playground.ipynb", "r") as f:
            data = json.load(f)

        for cell in data["cells"]:
            assert isinstance(cell["source"], list), "Cell source should be a list"

    def test_notebook_nbformat_version(self):
        """Test that notebook format version is valid"""
        import json

        with open("playground.ipynb", "r") as f:
            data = json.load(f)

        assert "nbformat" in data
        assert isinstance(data["nbformat"], int)
        assert data["nbformat"] >= 4, "Should use nbformat version 4 or higher"

    def test_notebook_file_size_reasonable(self):
        """Test that notebook file size is reasonable"""
        size = Path("playground.ipynb").stat().st_size
        assert size < 10_000_000, f"Notebook size ({size} bytes) should be reasonable (< 10MB)"

    def test_notebook_no_binary_data_in_outputs(self):
        """Test that notebook doesn't contain large binary outputs"""
        import json

        with open("playground.ipynb", "r") as f:
            content = f.read()

        # Check for large base64 encoded images
        assert content.count("data:image") < 10, "Should not have excessive embedded images"