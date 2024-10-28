from project import get_letterbox_str, get_letterbox_color,find_all_chars_in_str

def test_get_letterbox_str():
    # handle empty box
    assert get_letterbox_str(0,"?",None) == ['⬜⬜⬜ ', '⬜? ⬜ ', '⬜⬜⬜ ']
    # handle not found box
    assert get_letterbox_str(0,"a","white") == ['⬜⬜⬜ ', '⬜A ⬜ ', '⬜⬜⬜ ']
    # handle hint box
    assert get_letterbox_str(0,"a","yellow") == ['🟨🟨🟨 ', '🟨A 🟨 ', '🟨🟨🟨 ']
    # handle correct box
    assert get_letterbox_str(0,"a","green") == ['🟩🟩🟩 ', '🟩A 🟩 ', '🟩🟩🟩 ']

def test_get_letterbox_color():
    # test not found
    assert get_letterbox_color(0, "h","hello","world") == "white"
    
    # test hint
    assert get_letterbox_color(0, "o","orldw","world") == "yellow"
    
    # test correct
    assert get_letterbox_color(0, "w","world","world") == "green"

def test_find_all_chars_in_str():
    assert find_all_chars_in_str("hello","a") == []
    assert find_all_chars_in_str("hello","h") == [0]
    assert find_all_chars_in_str("hello","l") == [2,3]