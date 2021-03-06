import sublime
from os import path, remove, listdir
from shutil import copy2 as copy
from json import dump as json_dump
from .paths_helper import get_user_dir_path, get_fps_dir_path
from .exceptions import InvalidJSON, InvalidConfig


def load_current_settings(view):
    return view.settings().get('packagesSettings', {})


def merge_settings(original, new):
    for key, value in new.items():
        original[key] = value

    return original


def lock_setting_file(setting_file):
    setting_file += ".sublime-settings"
    file_path = path.join(get_user_dir_path(), setting_file)
    file_path_lock = path.join(get_fps_dir_path(), setting_file) + ".lock"
    if path.exists(file_path):
        try:
            copy(file_path, file_path_lock)
            with open(file_path, 'r') as file:
                settings_as_json = sublime.decode_value(file.read())
        except ValueError:
            raise InvalidJSON
    else:
        with open(file_path_lock, 'w'):
            pass
        settings_as_json = {}
    return settings_as_json


def unlock_file(setting_file):
    setting_file += ".sublime-settings"
    file_path = path.join(get_user_dir_path(), setting_file)
    file_path_lock = path.join(get_fps_dir_path(), setting_file) + ".lock"

    if path.exists(file_path):
        remove(file_path)

    if path.exists(file_path_lock):
        copy(file_path_lock, file_path)
        remove(file_path_lock)


def save_settings_from_json(setting_file, settings):
    setting_file += ".sublime-settings"
    file_path = path.join(get_user_dir_path(), setting_file)

    with open(file_path, 'w') as f:
        json_dump(settings, f)


def process_package_settings(package):
    try:
        settings_file = package['settings_file']
        new_settings = package['settings']
    except KeyError as e:
        raise InvalidConfig(str(e))
    try:
        package_settings = lock_setting_file(settings_file)
    except InvalidJSON:
        print("Error loading the {} parameters file, invalid\
        sublime configuration JSON, this file was left as is!"
              .format(settings_file))
        return None

    package_settings_json = merge_settings(package_settings, new_settings)

    save_settings_from_json(settings_file, package_settings_json)


def clear_all_locks():
    fps_dir = get_fps_dir_path()
    for f in listdir(fps_dir):
        file_path = path.join(fps_dir, f)
        if path.isfile(file_path) \
           and (path.splitext(file_path)[1] == ".lock"):
            base_name = path.splitext(path.splitext(f)[0])[0]
            unlock_file(base_name)
