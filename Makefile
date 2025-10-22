.PHONY: test-addition test-subtraction test-multiplication test-all clean

test-addition:
	@echo "Running addition tests..."
	@python test_addition.py

test-subtraction:
	@echo "Running subtraction tests..."
	@python test_subtraction.py

test-multiplication:
	@echo "Running multiplication tests..."
	@python test_multiplication.py

test-all: test-addition test-subtraction test-multiplication
	@echo "All tests completed!"

clean:
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -delete
	@echo "Cleaned up Python cache files"

