def is_valid_window(s):
    """Test if a value is a valid window.

    A valid window being an odd int between 3 and 501.
    """
    valid = True
    try:
        value = int(s)

        if value not in [i for i in range(3, 503, 2)]:
            valid = False

    except ValueError:
        valid = False

    return valid
