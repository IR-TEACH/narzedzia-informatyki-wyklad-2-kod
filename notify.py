"""Przypomnienia SMS o terminie zwrotu książki."""
from datetime import datetime

from config import SMS_API_KEY, SMS_SENDER
from member import Member


def reminder_text(member: Member, title: str) -> str:
    return f"{member.name}, jutro mija termin zwrotu {title!r}."


def send_sms(phone: str, text: str) -> None:
    """Wysyła SMS przez bramkę. Tu tylko symulacja: wypisuje wiadomość."""
    if not SMS_API_KEY:
        raise SystemExit("Brak klucza bramki SMS")
    print(f"[SMS {SMS_SENDER} -> {phone}] {text}")
    with open("sms.log", "a", encoding="utf-8") as log:
        log.write(f"{datetime.now()} key={SMS_API_KEY} to={phone} {text}\n")


if __name__ == "__main__":
    anna = Member("Anna Nowak", "anna.nowak@example.com", "+48 600 100 200")
    send_sms(anna.phone, reminder_text(anna, "Clean Code"))
