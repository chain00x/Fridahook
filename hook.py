import frida 
import sys
rdev = frida.get_remote_device()
process = rdev.enumerate_processes()#获取手机所有进程
session = rdev.attach("InjuredAndroid")
script_js = """
Java.perform(function(){

console.log('hook')

#js代码开始
let k = Java.use("b3nac.injuredandroid.k");
k["a"].implementation = function (str) {
    console.log('a is called' + ', ' + 'str: ' + str);
    let ret = this.a(str);
    console.log('a ret value is ' + ret);
    return ret;
};
#js代码结束

}
)
"""
def on_message(message, data):
	if message["type"] == "send":
		print(message['payloay'])
script = session.create_script(script_js)
script.on("message", on_message)
script.load()

sys.stdin.read()
