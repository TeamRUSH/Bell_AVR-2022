import shutil
from pathlib import Path


def main():
    # Get the base directory
    basepath = Path(__file__).parent.parent
    libaries = basepath.joinpath("Libraries")

    qt_icon = libaries.joinpath("qt_icon.py")
    shutil.copy(qt_icon, basepath.joinpath("PCC", "GUI"))
    shutil.copy(qt_icon, basepath.joinpath("VMC", "GUI"))

    pcc_library = libaries.joinpath("pcc_library.py")
    shutil.copy(pcc_library, basepath.joinpath("PCC", "GUI"))

    imgs = libaries.joinpath("img")
    shutil.rmtree(basepath.joinpath("PCC", "GUI", "img"), ignore_errors=True)
    shutil.copytree(imgs, basepath.joinpath("PCC", "GUI", "img"))
    shutil.rmtree(basepath.joinpath("VMC", "GUI", "img"), ignore_errors=True)
    shutil.copytree(imgs, basepath.joinpath("VMC", "GUI", "img"))


if __name__ == "__main__":
    main()