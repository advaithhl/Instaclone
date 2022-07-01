from datetime import datetime, timezone

from django import template

register = template.Library()


@register.filter
def post_time_fmt(post_time):
    return _post_time_fmt(post_time).upper()


def _post_time_fmt(post_time):
    now = datetime.now(timezone.utc)
    difference = now - post_time
    if post_time.year == now.year:
        if difference.days <= 7:
            if difference.days <= 1:
                if difference.days == 0:
                    return _same_day_difference(difference)
                return post_time.strftime(f"{difference.days} day ago")
            return post_time.strftime(f"{difference.days} days ago")
        return post_time.strftime("%B %d")
    return post_time.strftime("%B %d, %Y")


def _same_day_difference(difference):
    hours = difference.seconds // 3600
    if hours:
        return f"{hours} {'hour' if hours == 1 else 'hours'} ago"
    minutes = difference.seconds // 60
    if minutes:
        return f"{minutes} {'minute' if minutes == 1 else 'minutes'} ago"
    seconds = difference.seconds
    return f"{seconds} {'second' if seconds == 1 else 'seconds'} ago"
