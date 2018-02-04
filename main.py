# Main File
import modules.interface.server as interface


if __name__ == '__main__':
    interface.app.run(use_reloader=True, debug=True)