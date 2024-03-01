import sys


def add_path():
    l = ['j:/Houdini/19.5.805/python39/lib/site-packages-ui-forced',
         'j:/Houdini/19.5.805/python39/lib/site-packages-forced', '',
         'j:/Houdini/19.5.805/houdini/python3.9libs',
         'C:\\Users\\gfx', 'J:\\Houdini\\19.5.805\\bin\\python39.zip',
         'j:\\Houdini\\19.5.805\\python39\\DLLs',
         'j:\\Houdini\\19.5.805\\python39\\lib',
         'J:\\Houdini\\19.5.805\\bin',
         'j:\\Houdini\\19.5.805\\python39',
         'j:\\Houdini\\19.5.805\\python39\\lib\\site-packages',
         'j:/Houdini/19.5.805/packages/kinefx/python3.9libs',
         'j:/Houdini/19.5.805/houdini/python3.9libs',
         'J:/Houdini/sidefx_packages/SideFXLabs19.5/scripts/python',
         'j:/Houdini/19.5.805/packages/kinefx/viewer_states',
         'j:/Houdini/19.5.805/houdini/viewer_states',
         'j:/Houdini/19.5.805/packages/kinefx/viewer_handles',
         'j:/Houdini/19.5.805/houdini/viewer_handles',
         'j:/Houdini/19.5.805/python39/lib/site-packages',
         'J:/Houdini/sidefx_packages/SideFXLabs19.5/viewer_states']

    for item in l:
        sys.path.append(item)


def enableHouModule():
    '''Set up the environment so that "import hou" works.'''
    import sys, os

    # Importing hou will load Houdini's libraries and initialize Houdini.
    # This will cause Houdini to load any HDK extensions written in C++.
    # These extensions need to link against Houdini's libraries,
    # so the symbols from Houdini's libraries must be visible to other
    # libraries that Houdini loads.  To make the symbols visible, we add the
    # RTLD_GLOBAL dlopen flag.
    if hasattr(sys, "setdlopenflags"):
        old_dlopen_flags = sys.getdlopenflags()
        sys.setdlopenflags(old_dlopen_flags | os.RTLD_GLOBAL)

    # For Windows only.
    # Add %HFS%/bin to the DLL search path so that Python can locate
    # the hou module's Houdini library dependencies.  Note that 
    # os.add_dll_directory() does not exist in older Python versions.
    # Python 3.7 users are expected to add %HFS%/bin to the PATH environment
    # variable instead prior to launching Python.
    if sys.platform == "win32" and hasattr(os, "add_dll_directory"):
        os.add_dll_directory("{}/bin".format(os.environ["HFS"]))

    try:
        import hou
    except ImportError:
        # If the hou module could not be imported, then add 
        # $HFS/houdini/pythonX.Ylibs to sys.path so Python can locate the
        # hou module.
        sys.path.append(os.environ['HHP'])
        import hou
    finally:
        # Reset dlopen flags back to their original value.
        if hasattr(sys, "setdlopenflags"):
            sys.setdlopenflags(old_dlopen_flags)


enableHouModule()
add_path()
import hou


j:\Programs\Houdini\18.5.408\python27\python2.7.exe

['J:/Programs/Houdini/18.5.408/python27/lib/site-packages-ui-forced', 'J:/Programs/H
oudini/18.5.408/python27/lib/site-packages-forced', '', 'J:\\Programs\\Houdini\\18.5
.408\\bin\\python27.zip', 'J:\\Programs\\Houdini\\18.5.408\\python27\\DLLs', 'J:\\Pr
ograms\\Houdini\\18.5.408\\python27\\lib', 'J:\\Programs\\Houdini\\18.5.408\\python2
7\\lib\\plat-win', 'J:\\Programs\\Houdini\\18.5.408\\python27\\lib\\lib-tk', 'J:\\Pr
ograms\\Houdini\\18.5.408\\bin', 'J:\\Programs\\Houdini\\18.5.408\\python27', 'J:\\P
rograms\\Houdini\\18.5.408\\python27\\lib\\site-packages', 'j:/Projects/UE5/CitySamp
le_New/CitySampleSource/Small_City/houdini/python2.7libs', 'J:/Programs/Houdini/18.5
.408/houdini/python2.7libs', 'J:/Programs/Houdini/18.5.408/houdini/viewer_states', '
J:/Programs/Houdini/18.5.408/houdini/viewer_handles', 'J:/Programs/Houdini/18.5.408/
python27/lib/site-packages', 'J:/Programs/Houdini/18.5.408/houdini/viewer_states/exa
mples']
