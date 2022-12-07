#!/usr/bin/env python3
# coding=utf8

from pathlib import Path

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


class FlyffBrowser:
    URL_FLYFF_PLAY: str = 'https://universe.flyff.com/play'

    def __init__(self, path_profile: str) -> None:
        # Initialize options
        options: Options = Options()
        # Add custom profile
        options.add_argument('--profile')
        options.add_argument(path_profile)
        # Start in kiosk mode (no toolbar, always fullscreen)
        options.add_argument('--kiosk')
        # Init driver
        self.driver: Firefox = Firefox(options=options)

    def open(self) -> None:
        self.driver.get(self.URL_FLYFF_PLAY)


def main() -> None:
    # Initialize profile path
    path_profile: Path = Path.home().joinpath('.flyff', 'default.profile')
    if not path_profile.is_dir():
        path_profile.mkdir(parents=True, exist_ok=True)

    # Open browser
    browser = FlyffBrowser(str(path_profile))
    browser.open()


if __name__ == '__main__':
    main()
