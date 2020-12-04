import yaml
import web

CONFIG_FILE = "config/server.yaml"
GLOBAL_IP = ""
GLOBAL_PORT = ""
GLOBAL_NOTIFY_CONFIG = ""


class hello:
    def GET(self):
        return "hello, monitoring server is running!"
    def POST(self):
        return "hello, monitoring server is running!"


class Greetings:
    def GET(self):
        return "sorry, get is banned."

    def POST(self):
        return "you have connected to a genius monitoring server."


class ServerOperations:
    def GET(self):
        return "sorry, get is banned."

    def POST(self):
        notify(web.input().message)
        return "ok, i will send messages as configured."


def config_parser():
    global CONFIG_FILE
    fs = open(CONFIG_FILE, encoding="UTF-8")
    server_configs = yaml.load(fs, Loader=yaml.FullLoader)
    ip, port, notify_method = server_configs["ip"], server_configs["port"], server_configs["notify_method"]
    return ip, port, notify_method


def notify(messages):
    global GLOBAL_NOTIFY_CONFIG
    notify_config = GLOBAL_NOTIFY_CONFIG
    for o in notify_config.keys():
        if notify_config[o]["enable"]:
            if not eval("%s.notify" % o)(notify_config[o], messages):
                continue


if __name__ == "__main__":
    urls = (
        '/', 'hello',
        '/register', 'Greetings',
        '/server', 'ServerOperations'
    )
    GLOBAL_IP, GLOBAL_PORT, GLOBAL_NOTIFY_CONFIG = config_parser()
    app = web.application(urls, globals())
    web.httpserver.runsimple(app.wsgifunc(), (GLOBAL_IP, GLOBAL_PORT))