def parse_command(message):
    if message.content.startswith('!'):
        command = message.content[1:]
        return command.split()
    else:
        return None