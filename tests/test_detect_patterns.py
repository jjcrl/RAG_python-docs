from lib.detect_patterns import detect_pattern

def test_glossary():
    assert detect_pattern("corpus/glossary.txt") == "D"

def test_faq():
    assert detect_pattern("corpus/faq/programming.txt") == "C"

def test_sorting():
    assert detect_pattern("corpus/howto/sorting.txt") == "A"

def test_function():
    assert detect_pattern("corpus/library/functions.txt") == "B"

def test_functions():
    assert detect_pattern("corpus/library/functions.txt") == "B"

def test_appetite():
    assert detect_pattern("corpus/tutorial/appetite.txt") == "E"