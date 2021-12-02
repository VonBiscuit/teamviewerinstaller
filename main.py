import struct
import time

import requests
import pyautogui
import subprocess

teamviewer_link_32 = "https://download.teamviewer.com/download/TeamViewer_Setup.exe"
teamviewer_link_64 = "https://download.teamviewer.com/download/TeamViewer_Setup_x64.exe"
bit_version = 64


def determine_if_64_or_32_bit():
    global bit_version
    bit_version = struct.calcsize("P") * 8
    return bit_version


def download_teamviewer():
    if bit_version == 64:
        r = requests.get(teamviewer_link_64)
        with open('TeamViewer_Setup_x64.exe', 'wb') as outfile:
            outfile.write(r.content)

    if bit_version == 32:
        r = requests.get(teamviewer_link_32)
        with open('TeamViewer_Setup.exe', 'wb') as outfile:
            outfile.write(r.content)


def click_by_button_image_location(image_name):
    button_location = pyautogui.locateOnScreen(image_name)
    button_point = pyautogui.center(button_location)
    pyautogui.click(button_point)


def open_team_viewer():
    if bit_version == 64:
        subprocess.Popen('TeamViewer_Setup_x64.exe')
    if bit_version == 32:
        subprocess.Popen('TeamViewer_Setup.exe')
    time.sleep(3)


def just_run_no_install():
    open_team_viewer()
    # click_by_button_image_location('runOnly.png')
    # click_by_button_image_location('acceptRunButton.png')


def default_installation():
    open_team_viewer()
    click_by_button_image_location('defaultInstallation.png')
    click_by_button_image_location('acceptNextButton.png')


def custom_installation():
    open_team_viewer()
    click_by_button_image_location('customInstallation.png')
    click_by_button_image_location('acceptNextButton.png')


if __name__ == '__main__':
    determine_if_64_or_32_bit()
    download_teamviewer()
    # just_run_no_install()
    # default_installation()
    # custom_installation()