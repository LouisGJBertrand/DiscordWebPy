import webview


def read_cookies(window):
    cookies = window.get_cookies()
    for c in cookies:
        print(c.output())


if __name__ == '__main__':
    window = webview.create_window('Discord PyWebview', 'https://discord.com/app')
    window.maximized = True
    webview.start(read_cookies, window, private_mode=False)
