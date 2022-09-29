from telechargeo.inputHandler import displayRequestedValue, setupArguments

def test_inputHandler(capsys):
    displayRequestedValue(['-A', 'Ed Sheeran', '-T', 'Perfect'])
    captured = capsys.readouterr()
    assert captured.out == 'searching for the video Ed Sheeran - Perfect\n'