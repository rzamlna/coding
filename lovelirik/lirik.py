import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("Aku tahu kamu hebat", 0.05),
        ("Namun, s'lamanya diriku pasti berkutat", 0.04),
        ("Tuk slalu jauhkanmu dari dunia yang jahat", 0.03),
        ("Ini sumpahku padamu 'tuk biarkanmu", 0.04),
        ("Tumbuh lebih baik, cari panggilanmu", 0.05),
        ("Jadi lebih baik dibanding diriku", 0.05),
        ("Tuk sementara kita tertawakan berbagai hal", 0.05),
        ("Yang lucu dan lara selepas-lepasnya", 0.05)

    ]

    delays = [0.3, 0.5, 0.04, 0.03, 0.05, 0.04, 0.04, 0.05]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

    print_lyrics()