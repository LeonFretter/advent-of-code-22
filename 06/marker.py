def findMarker(txt: str, marker_len=4) -> int:
    for i in range(marker_len - 1, len(txt)):
        prev_chars = txt[i - (marker_len - 1):i + 1]
        assert len(prev_chars) == marker_len
        if len(set(prev_chars)) == marker_len:
            return i + 1

    raise ValueError("No marker found")


if __name__ == "__main__":
    txt = """\
mjqjpqmgbljsphdztnvjfqwrcgsmlb\
"""
    res = findMarker(txt)
    assert res == 7

    res2 = findMarker(txt, marker_len=14)
    assert res2 == 19
