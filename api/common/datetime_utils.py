from datetime import datetime

import pytz


def get_utc_now():
    """Get current datetime in UTC.

    Returns:
        Datetime
    """
    return datetime.utcnow().replace(tzinfo=pytz.UTC)


def get_datetime_from_epoch(epoch):
    return datetime.fromtimestamp(epoch, tz=pytz.UTC)


def get_datetime_from_string(
    date_str, formats=("%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ")
):
    result = None
    for format in formats:
        try:
            result = pytz.UTC.localize(datetime.strptime(date_str, format))
        except ValueError:
            continue
    if result is None:
        raise Exception(
            "Could not covert str into datetime object based on the formats provided"
        )
    return result
