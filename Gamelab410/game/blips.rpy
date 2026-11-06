init -10 python:
    renpy.music.register_channel("blip", mixer="voice", loop=False)
    config.default_voice_volume = 1.0

    def make_blips(sounds, default="talk", fadeout=0.15):
        def callback(event, interact=True, mood=None, **kwargs):
            if not interact:
                return

            if event == "show":
                if renpy.config.skipping or preferences.text_cps == 0:
                    return
                choice = sounds.get(mood or default, sounds[default])
                if isinstance(choice, (list, tuple)):
                    choice = renpy.random.choice(choice)
                renpy.sound.play(choice, channel="blip", loop=True)

            elif event in ("slow_done", "end"):
                renpy.sound.stop(channel="blip", fadeout=fadeout)

        return callback