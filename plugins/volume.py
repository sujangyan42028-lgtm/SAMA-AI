import re
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def get_volume():

    print("Getting Volume Device...")

    device = AudioUtilities.GetSpeakers()

    if hasattr(device, "EndpointVolume"):
        print("Using EndpointVolume")
        return device.EndpointVolume

    from ctypes import POINTER, cast
    from comtypes import CLSCTX_ALL

    interface = device.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )

    print("Using Activate()")

    return cast(interface, POINTER(IAudioEndpointVolume))


def run(user):

    print("🔥 VOLUME PLUGIN RUNNING")

    user = user.lower()

    try:

        volume = get_volume()

        # -------------------------
        # Set Volume (0-100)
        # -------------------------

        match = re.search(r"\d+", user)

        if ("set volume" in user or "volume" in user) and match:

            level = int(match.group())

            if level < 0:
                level = 0

            if level > 100:
                level = 100

            volume.SetMasterVolumeLevelScalar(level / 100, None)

            return f"Volume set to {level}%."

        # -------------------------
        # Volume Up
        # -------------------------

        if "volume up" in user:

            current = volume.GetMasterVolumeLevelScalar()

            volume.SetMasterVolumeLevelScalar(
                min(current + 0.1, 1.0),
                None
            )

            return "Volume increased."

        # -------------------------
        # Volume Down
        # -------------------------

        elif "volume down" in user:

            current = volume.GetMasterVolumeLevelScalar()

            volume.SetMasterVolumeLevelScalar(
                max(current - 0.1, 0.0),
                None
            )

            return "Volume decreased."

        # -------------------------
        # Mute
        # -------------------------

        elif "mute" in user and "unmute" not in user:

            volume.SetMute(1, None)

            return "Volume muted."

        # -------------------------
        # Unmute
        # -------------------------

        elif "unmute" in user:

            volume.SetMute(0, None)

            return "Volume unmuted."

        return None

    except Exception as e:

        print("[VOLUME ERROR]", e)

        return "Volume control error."