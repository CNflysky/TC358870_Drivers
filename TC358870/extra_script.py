from os import path
Import("env")
platform = env.PioPlatform()

def on_upload(source, target, env):
    upload_tool_path:str = platform.get_package_dir("tool-dfuutil")
    firmware_path = str(source[0])
    if path.exists(firmware_path):
        env.Execute("%s\\bin\\dfu-suffix.exe -D %s" % (upload_tool_path,firmware_path))
    env.Execute("%s\\bin\\dfu-suffix.exe -a %s -v 0x0483 -p 0xdf11" % (upload_tool_path,firmware_path))
    env.Execute("%s\\bin\\dfu-util.exe -R -d 0483:df11 -s 0x08005800 -D %s" % (upload_tool_path,firmware_path))

env.Replace(UPLOADCMD=on_upload)