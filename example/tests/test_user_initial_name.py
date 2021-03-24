from example.user.user import create_initial_name


def test_should_produce_intial_name_from_fullname_without_punctuation():
    initial = create_initial_name("Lembu Wiworo Jati")
    assert initial == "LWJ"

def test_should_produce_intial_name_from_fullname_with_punctuation():
    initial = create_initial_name("Robert Downey, Jr.")
    assert initial == "RDJ"

def test_should_produce_initial_name_from_uncapitalised_names():
    initial = create_initial_name("deepika padukone")
    assert initial == "DP"
