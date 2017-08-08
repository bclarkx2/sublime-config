import sublime
import sublime_plugin


class SaveAndBuild(sublime_plugin.WindowCommand):

    def run(self, edit):
        self.view.run_command("save")
        self.view.run_command("build")
