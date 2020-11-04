def format_duration(seconds):
    if seconds == 1:
        return f'{seconds} second'
    elif seconds < 60:
        return f'{seconds} seconds'
    elif seconds < 3600:
        minutes = int(seconds / 60)
        seconds = seconds - minutes * 60
        if seconds == 0:
            return f'{minutes} minutes'
        if minutes == 1:
            return f'{minutes} minute and {seconds} seconds'
        elif minutes > 1:
            return f'{minutes} minutes and {seconds} seconds'
    elif seconds < 86400:
        hours = int(seconds / 3600)
        minutes = int((seconds - (hours * 3600)) / 60)
        seconds = int(seconds - (hours * 3600) - (minutes * 60))
        if hours == 1:
            return f'{hours} hour, {minutes} minutes and {seconds} seconds'
        if hours > 1:
            return f'{hours} hours, {minutes} minutes and {seconds} seconds'
    else:
        days = int(seconds / 86400)
        hours = int((seconds - days * 86400) / 3600)
        minutes = int((seconds - (days * 86400) - (hours * 3600))/60)
        seconds = seconds % 60
        if days == 1:
            return f'{days} day, {hours} hours, {minutes} minutes and {seconds} seconds'
        if days > 1:
            return f'{days} days, {hours} hours, {minutes} minutes and {seconds} seconds'


print(format_duration(1))
print(format_duration(7856))
print(format_duration(3500))
print(format_duration(3456))
print(format_duration(500000))
