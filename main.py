""""
Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT
emulator), you can use the real SenseHAT class instead of the mock SenseHAT
class. That is, delete the sense_hat.py file that is included in this bundle.
"""
import time

from happy import Happy
from sad import Sad
from angry import Angry

if __name__ == '__main__':
    # This is only needed if you have not deleted sense_hat.py
    # and only in some environments - uncomment only if you have errors
    # from multiprocessing import freeze_support
    # freeze_support()
    ############################################################

    # Create a happy smiley, a sad smiley and an angry smiley, and make
    # each of them blink.
    for smiley in (Happy(), Sad(), Angry()):
        smiley.show()
        time.sleep(1)
        smiley.blink()