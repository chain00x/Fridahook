import frida 
import sys
rdev = frida.get_remote_device()
process = rdev.enumerate_processes()#获取手机所有进程
session = rdev.attach("InjuredAndroid")
script_js = """
let g = Java.use("b.c.a.a.f.g");
g["l"].implementation = function () {
    console.log('l is called');
    let ret = this.l();
    console.log('l ret value is ' + ret);
    return ret;
};
"""
def on_message(message, data):
	if message["type"] == "send":
		print(message['payloay'])
script = session.create_script(script_js)
script.on("message", on_message)
script.load()

sys.stdin.read()
