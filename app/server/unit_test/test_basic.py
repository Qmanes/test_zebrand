import pytest
from email_validator import EmailSyntaxError

from app_code.model.Basic_Model import Basic

basic = Basic()

def test_str_lower():

    assert basic.format_str_lowercase(" String of TEST ") == "string of test"

def test_str_upper():

    assert basic.format_str_uppercase(" String of TEST ") == "STRING OF TEST"

def test_str_capitalize():

    assert basic.format_str_capitalcase(" String of TEST ") == "String of test"

def test_not_has_change():

    with pytest.raises(Exception):

        basic.assert_than_has_change("test_equal", "test_equal")

def test_is_required():

    with pytest.raises(Exception):

        basic.assert_field_required("")

def test_email_not_is_valid():

    with pytest.raises(EmailSyntaxError):
    
        basic.assert_email_valid("rasd")

def test_email_is_valid():

    basic.assert_email_valid("test@gmail.com")

def test_format_float():

    assert basic.format_float("123.25") == 123.25
       