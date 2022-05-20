import pip


def install_whl(path):
    pip.main(['install', path])


install_whl(r"C:\Users\Aaron\Downloads\PyAudio-0.2.11-cp310-cp310-win_amd64.whl")
