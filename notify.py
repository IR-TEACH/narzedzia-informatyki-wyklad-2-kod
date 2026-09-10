"""Przypomnienia SMS o terminie zwrotu książki."""
from member import Member

SMS_API_KEY = ""  # TODO: klucz od dostawcy bramki SMS
SMS_SENDER = "MiniLib"


def reminder_text(member: Member, title: str) -> str:
    return f"{member.name}, jutro mija termin zwrotu {title!r}."


def send_sms(phone: str, text: str) -> None:
    """Wysyła SMS przez bramkę. Tu tylko symulacja: wypisuje wiadomość."""
    if not SMS_API_KEY:
        raise SystemExit("Brak klucza bramki SMS")
    print(f"[SMS {SMS_SENDER} -> {phone}] {text}")


if __name__ == "__main__":
    anna = Member("Anna Nowak", "anna.nowak@example.com", "+48 600 100 200")
    send_sms(anna.phone, reminder_text(anna, "Clean Code"))
