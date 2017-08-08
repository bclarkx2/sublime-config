import sublime, sublime_plugin

class RunUnitTests(sublime_plugin.TextCommand):
    def run(self, edit):
        print("running unit tests")
        self.view.window().run_command('exec', {'shell_cmd': './test'})
