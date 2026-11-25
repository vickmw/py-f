from evdev import InputDevice, ecodes
dev = InputDevice('/dev/input/event4')
for e in dev.read_loop():
    if e.type == ecodes.EV_REL:
        print(e.code, e.value)