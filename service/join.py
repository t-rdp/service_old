import misc.misskey
import misc.hcaptcha
from service import app
from flask import render_template, request

@app.route("/_service/join")
def join_get():
    return render_template("join.html")

@app.route("/_service/join", methods=["POST"])
def join_post():
    captcha_code = request.form.get("h-captcha-response", "")
    key = request.form.get("key", "")
    with open("key.txt") as f:
        ckey = f.read()
    if not key == ckey:
        return render_template("join_note.html", content="<h3 style='font-weight: unset;'>暗号写错啦~您可以<a href='/_service/join'>重新开始</a>。</h3>")
    if not misc.hcaptcha.check(captcha_code):
        return render_template("join_note.html", content="<h3 style='font-weight: unset;'>人机验证失败啦~您可以<a href='/_service/join'>重新开始</a>。</h3>")
    invite_code = misc.misskey.get_invite_code()
    return render_template("join_note.html", content="<h3 style='font-weight: unset;'>您的邀请码是<b><pre>" + invite_code + "</pre></b>请您复制邀请码，然后返回<a href='https://t.rdpstudio.top'>主站</a>点击注册按钮继续注册。</h3>")