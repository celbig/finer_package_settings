# import sublime
import sublime_plugin
import finerPackageSettings.tools as tools


class finerPackageSettingsCommand(sublime_plugin.EventListener):
    def on_activated(self, view):
        if not view.file_name() is None:
            tools.clear_all_locks()
            fps_settings = tools.load_current_settings(view)
            for p in fps_settings:
                try:
                    tools.process_package_settings(p)
                except tools.InvalidConfig as e:
                    print("Error: the parameters for finerPackageSettings is\
                    invalid, no '{}' key found !"
                          .format(str(e)))


def plugin_loaded():
    tools.clear_all_locks()


def plugin_unloaded():
    tools.clear_all_locks()
