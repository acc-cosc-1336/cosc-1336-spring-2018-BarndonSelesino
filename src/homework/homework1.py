def get_hours_since_midnight(total_seconds):
    hours = int(total_seconds // 3600);
    return hours

def get_minutes(total_seconds): 
    seconds_remaining = int(total_seconds % 3600);
    minutes = int(seconds_remaining // 60);
    return minutes


def get_seconds(total_seconds): 
    seconds_remaining = int(total_seconds % 3600)'
    seconds = int(seconds_remaining % 60)'
    return seconds
