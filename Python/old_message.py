def send_message(message):
  phone_keyboard = {
    1 : '.',
    11: ',',
    111: '?',
    1111: '!',
    2: 'a',
    22: 'b',
    222: 'c',
    3: 'd',
    33: 'e',
    333: 'f',
    4: 'g',
    44: 'h',
    444: 'i',
    5: 'j',
    55: 'k',
    555: 'l',
    6: 'm',
    66: 'n',
    666: '0',
    7: 'p',
    77: 'q',
    777: 'r',
    7777: 's',
    8: 't',
    88: 'u',
    888: 'v',
    9: 'w',
    99: 'x',
    999: 'y',
    9999: 'z',
    '*': "'",
    '**': '-',
    '***': '+',
    '****': '-',
    0: ' '

  }
  decoded_message = ''
  temp = ''
  for i in range(len(message)):
    if i > 0 and message[i] != message[i-1]:
        if temp in phone_keyboard:
            decoded_message += phone_keyboard[temp]
            temp = message[i]  # Start a new sequence
        else:
            temp += message[i]  # Add the current character to the sequence

    if temp in phone_keyboard:
        decoded_message += phone_keyboard[temp]

    return decoded_message
      