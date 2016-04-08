import src.grovepi_test_code as test
import src.sound_sensor as sound


if __name__ == "__main__":
    s = sound.SoundSensors()
    s.loop_it_baby()
