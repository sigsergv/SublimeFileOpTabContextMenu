import sublime, sublime_plugin

class RenameFileInTabCommand(sublime_plugin.TextCommand):
    def run (self, edit, args=None, **kwargs):
        
        file_name = self.view.file_name()
        if file_name is None:
            return

        self.view.window().run_command('rename_path', args={'paths': [file_name]})

class CloneFileContents(sublime_plugin.TextCommand):
    def run(self, edit, args=None, **kwargs):
        content = self.view.substr(sublime.Region(0, self.view.size()))
        new_view = self.view.window().new_file()
        new_view.insert(edit, 0, content)
