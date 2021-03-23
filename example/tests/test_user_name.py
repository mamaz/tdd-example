import pytest
from example.user.user import split_fullname

def test_should_produce_firstname_middlename_and_lastname_from_one_word_name():
    (first_name, middle_name, last_name) = split_fullname("Rudy")
    assert first_name == "Rudy" and middle_name == "" and last_name == ""

def test_should_produce_firstname_middlename_and_lastname_from_two_word_name():
    (first_name, middle_name, last_name) = split_fullname("Rudy Habibie")
    assert first_name == "Rudy" and middle_name == "" and last_name == "Habibie"

def test_should_produce_firstname_middlename_and_lastname_from_three_word_name():
    (first_name, middle_name, last_name) = split_fullname("Bacharudin Jusuf Habibie")
    assert first_name == "Bacharudin" and middle_name == "Jusuf" and last_name == "Habibie"

def test_should_produce_firstname_middlename_and_lastname_from_more_than_three_words_name():
    (first_name, middle_name, last_name) = split_fullname("Deodatus Andreas Deddy Cahyadi Sunjoyo")
    assert first_name == "Deodatus" and middle_name == "Andreas Deddy Cahyadi" and last_name == "Sunjoyo"

def test_should_return_empty_string_if_fullname_is_empty():
    (first_name, middle_name, last_name) = split_fullname("")
    assert first_name == "" and middle_name == "" and last_name == ""

# HOMEWORK:
# Checking against null values
# def test_should_throw_exception_if_it_has_null_values():
#     with pytest.raises(Exception) as e:
#         split_fullname(None)

#
# HOMEWORK:
# How about Robert Downey, Jr
# It should be
# Firstname: Robert
# Middlename: ""
# Lastname: Downey
# def test_should_ignore_punctuation():
#     (first_name, middle_name, last_name) = split_fullname("Robert Downey, Jr.")
#     assert first_name == "Robert" and middle_name == "" and last_name == "Downey"