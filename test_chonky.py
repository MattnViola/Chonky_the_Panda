from chonky import bot_text_reply, bot_gif, msg_reaction

def test_bot_text_reply():
    assert bot_text_reply("!hi") == "Howdy, Dumplin!"
    assert bot_text_reply("!failed") == "looks like it work to me!"
    assert bot_text_reply("!dsd") == "Idk what's goin on..."
def test_bot_gif():
    assert bot_gif().startswith("https://") == True

def test_msg_reaction():
    assert msg_reaction("dumpling") == "🐢"
    assert msg_reaction("hog") == "🐽"
    assert msg_reaction("cow") == None