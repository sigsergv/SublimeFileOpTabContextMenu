import sublime, sublime_plugin
import os
import functools


class RenameFileInTabCommand(sublime_plugin.TextCommand):
    def run (self, edit, args=None, index=-1, group=-1, **kwargs):
        w = self.view.window()
        views = w.views_in_group(group)
        view = views[index]
        
        full_path = view.file_name()
        if full_path is None:
            return

        directory, fn = os.path.split(full_path)
        v = w.show_input_panel("New file name:",
            fn,
            functools.partial(self.on_done, full_path, directory),
            None,
            None)
        name, ext = os.path.splitext(fn)

        v.sel().clear()
        v.sel().add(sublime.Region(0, len(name)))

    def on_done(self, old, directory, fn):
        new = os.path.join(directory, fn)

        if new == old:
            return

        try:
            if os.path.isfile(new):
                if old.lower() != new.lower() or os.stat(old).st_ino != os.stat(new).st_ino:
                    # not the same file (for case-insensitive OSes)
                    raise OSError("File already exists")

            os.rename(old, new)

            v = self.view.window().find_open_file(old)
            if v:
                v.retarget(new)
        except OSError as e:
            sublime.error_message("Unable to rename: " + str(e))
        except Exception as e:
            sublime.error_message("Unable to rename: " + str(e))


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

