from win32com.client import Dispatch, GetActiveObject, gencache, constants
from os import getcwd
from pynput.keyboard import Key, Controller
import win32gui
import re

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__(self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)

    def set_focus(self):
        """put the window in the foreground"""
        win32gui.SetFocus(self._handle)

def generate_command_file(invApp):
    ControlDefs = invApp.CommandManager.ControlDefinitions
    commandFile = open(r"commands.txt", "w")

    for command in ControlDefs:
        instructions = command.InternalName
        if (command.DescriptionText != ""):
            instructions += " -\n" + command.DescriptionText + "\n"
        else:
            instructions += "\n\n"
        commandFile.write(instructions)
    commandFile.close()


def main(invApp):
    invDoc = invApp.Documents.Add(constants.kPartDocumentObject, "", True)

    # Casting Document to PartDocument
    invPartDoc = mod.PartDocument(invDoc)

    #Trigger inventor import panel
    ControlMgr = invApp.CommandManager
    ControlDefs = ControlMgr.ControlDefinitions
    ControlDefs.Item("AppFileImportNewCmd").Execute2(False)

    #Make inventor windows focus so it can type
    w = WindowMgr()
    w.find_window_wildcard(".*Autodesk Inventor Professional 2021.*")
    w.set_foreground()

    #Write in model name and import
    keyboard = Controller()
    cwd = getcwd()
    keyboard.type(cwd + "\models\male.stp\n")
    ControlDefs.Item("AppContextual_OKCmd").Execute2(False)

    # Close Document and Inventor
    # invPartDoc.Close(SkipSave=True)
    # invApp.Quit()


if __name__ == '__main__':
    try:
        invApp = GetActiveObject('Inventor.Application')
    except:
        invApp = Dispatch('Inventor.Application')
        invApp.Visible = True

    mod = gencache.EnsureModule('{D98A091D-3A0F-4C3E-B36E-61F62068D488}', 0, 1, 0)
    invApp = mod.Application(invApp)
    # invApp.SilentOperation = True

    main(invApp)
