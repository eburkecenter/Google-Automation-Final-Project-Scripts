#!/usr/bin/env python3
import shutil
import psutil
import socket
import emails


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free < 20


def check_cpu_usage():
    usage = psutil.cpu_percent(60)
    return usage > 80


def check_memory_usage():
    memory = psutil.virtual_memory()
    thresold = 500 * 1024 * 1024
    return memory.available < thresold


def check_localhost_resolution():
    """Returns True if hostname "localhost" cannot be resolved to "127.0.0.1", False otherwise."""
    try:
        socket.gethostbyname("localhost")
        return False
    except socket.gaierror:
        return True


if __name__ == "__main__":
    folder = "supplier-data"
    sender = "automation@example.com"  # from
    receiver = "<username>@example.com"  # to
    body = "Please check your system and resolve the issue as soon as possible."
    if check_cpu_usage():
        subject = "Error - CPU usage is over 80%"
        message = emails.generate(sender, receiver, subject, body)
        emails.send(message)

    if check_disk_usage(folder):
        subject = "Error - Available disk space is less than 20%"
        message = emails.generate(sender, receiver, subject, body)
        emails.send(message)

    if check_memory_usage():
        subject = "Error - Available memory is less than 500MB"
        message = emails.generate(sender, receiver, subject, body)
        emails.send(message)

    if check_localhost_resolution():
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        message = emails.generate(sender, receiver, subject, body)
        emails.send(message)
