from siml_parser import evaluate, read_file
import os

def read_file(file_name):
    text = read_file(os.path.join("indices/", file_name))
    return evaluate(text)

def test_flat_index_with_single_entry():
    assert read_file("flat_index_with_single_entry.index") == {
        "tea": {
            "start": 6,
            "end": 7
        }
    }

def test_index_with_see_also():
    assert read_file("index_with_see_also.index") == {
        "tea": {
            "start": 6,
            "end": 7,
            "see also": "beverages"
        }
    }

def test_flat_index_with_multiple_entries():
    assert read_file("flat_index_with_multiple_entries.index") == {
        "tea": {
            "start": 6,
            "end": 7
        },
        "coffee": {
            "start": 7,
            "end": 9
        }
    }

def test_nested_index_with_single_entry():
    assert read_file("nested_index_with_single_entry.index") == {
        "tea": {
            "start": 6,
            "end": 11,
            "subentries": {
                "earl grey": {
                    "start": 7,
                    "end": 9
                },
                "oolong": {
                    "start": 9,
                    "end": 11
                }
            }
        }
    }

def test_nested_index_with_multiple_entries():
    assert read_file("nested_index_with_multiple_entries.index") == {
        "tea": {
            "start": 6,
            "end": 11,
            "subentries": {
                "earl grey": {
                    "start": 7,
                    "end": 9
                },
                "oolong": {
                    "start": 9,
                    "end": 11
                }
            }
        },
        "coffee": {
            "start": 12,
            "end": 16,
            "subentries": {
                "typica": {
                    "start": 12,
                    "end": 14
                },
                "geisha": {
                    "start": 14,
                    "end": 16
                }
            }
        }
    }

def test_nested_index_with_multiple_entries_and_single_entries():
    assert read_file("nested_index_with_multiple_entries_and_single_entries.index") == {
        "tea": {
            "start": 6,
            "end": 11,
            "subentries": {
                "earl grey": {
                    "start": 7,
                    "end": 9
                },
                "oolong": {
                    "start": 9,
                    "end": 11
                }
            }
        },
        "coffee": {
            "start": 12,
            "end": 16,
            "subentries": {
                "typica": {
                    "start": 12,
                    "end": 14
                },
                "geisha": {
                    "start": 14,
                    "end": 16
                }
            }
        },
        "coffee equipment": {
            "start": 17,
            "end": 22
        },
        "tea equipment": {
            "start": 23,
            "end": 28
        }
    }
