# -*- coding: utf8 -*-


from asm2mmc import decode

EXAMPLE_ASMHASH_DATA = [
    ("3044022031378121e390af068f15deabd84121bf617103479ad990d5205c60dd8f89852d02206513063dbb018cf27b9af077452df65307bae3232266a295ed51aba85bc366a601 0379275a055be369f33ddf311b76e59b693ca74c27d2c2c2d293646a605bb00334", "MUvzMwV816iDr8VH8BccGz4yFUfGEWd6pR")
]

for asm, addr in EXAMPLE_ASMHASH_DATA:
    assert decode(asm) == 'MUvzMwV816iDr8VH8BccGz4yFUfGEWd6pR'