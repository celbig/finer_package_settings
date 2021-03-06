from os import path, mkdir
import sublime


def get_user_dir_path():
    return path.join(sublime.packages_path(), "User")


def get_fps_dir_path():
    fps_path = path.join(get_user_dir_path(), "finerPackageSettings")
    if not path.exists(fps_path):
        mkdir(fps_path)
    return fps_path
