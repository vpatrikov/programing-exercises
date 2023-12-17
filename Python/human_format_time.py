def format_duration(seconds):
    if seconds == 0:
        return "now"

    years = seconds // (365 * 24 * 3600)
    remaining_seconds = seconds % (365 * 24 * 3600)
    days = remaining_seconds // (24 * 3600)
    remaining_seconds %= (24 * 3600)
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    duration_parts = []

    if years:
        duration_parts.append(f"{years} {'year' if years == 1 else 'years'}")

    if days:
        duration_parts.append(f"{days} {'day' if days == 1 else 'days'}")

    if hours:
        duration_parts.append(f"{hours} {'hour' if hours == 1 else 'hours'}")

    if minutes:
        duration_parts.append(f"{minutes} {'minute' if minutes == 1 else 'minutes'}")

    if seconds:
        duration_parts.append(f"{seconds} {'second' if seconds == 1 else 'seconds'}")

    if len(duration_parts) > 1:
        return ', '.join(duration_parts[:-1]) + f" and {duration_parts[-1]}"
    else:
        return duration_parts[0]