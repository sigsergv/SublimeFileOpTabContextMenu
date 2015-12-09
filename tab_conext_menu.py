import sublime, sublime_plugin

class RenameFileInTabCommand(sublime_plugin.TextCommand):
    def run (self, edit, args=None, index=-1, group=-1, **kwargs):
        w = self.view.window()
        views = w.views_in_group(group)
        view = views[index]
        
        file_name = view.file_name()
        if file_name is None:
            return

        w.run_command('rename_path', args={'paths': [file_name]})


class CloneFileContentsCommand(sublime_plugin.TextCommand):
    def run(self, edit, args=None, index=-1, group=-1, **kwargs):
        w = self.view.window()
        views = w.views_in_group(group)
        view = views[index]

        content = view.substr(sublime.Region(0, view.size()))
        new_view = w.new_file()
        w.set_view_index(new_view, group, index+1)
        new_view.insert(edit, 0, content)


class FileopCloneFile(sublime_plugin.TextCommand):
    def run(self, edit, args=None, index=-1, group=-1, **kwargs):
        w = self.view.window()
        views = w.views_in_group(group)
        view = views[index]

        w.focus_view(view)
        w.run_command('clone_file')


class FileopRevealInSideBar(sublime_plugin.TextCommand):
    def run(self, edit, args=None, index=-1, group=-1, **kwargs):
        w = self.view.window()
        views = w.views_in_group(group)
        view = views[index]

        w.focus_view(view)
        w.run_command('reveal_in_side_bar')


class CopyFilePath(sublime_plugin.TextCommand):
    def run(self, edit, args=None, index=-1, group=-1, **kwargs):
        w = self.view.window()
        views = w.views_in_group(group)
        view = views[index]

        file_name = view.file_name()
        if file_name is None:
            return

        sublime.set_clipboard(file_name)

