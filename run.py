import src.grovepi_test_code as test
import src.sound_sensor as sound
import src.light_sensor as light


if __name__ == "__main__":
    s = sound.SoundSensors()
    l = light.LightSensor()
    l.loop_it_baby()
