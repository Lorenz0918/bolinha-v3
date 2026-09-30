"""Grade de aulas — Lins, Vila Mariana. Gera public/horario.json."""

from __future__ import annotations

import json
from pathlib import Path

PERIODS = [
    {"period": 1, "start": "07:15", "end": "08:00"},
    {"period": 2, "start": "08:00", "end": "08:45"},
    {"period": 3, "start": "08:45", "end": "09:30"},
    {"period": 4, "start": "09:30", "end": "10:15"},
    {"period": 5, "start": "10:45", "end": "11:30"},
    {"period": 6, "start": "11:30", "end": "12:15"},
    {"period": 7, "start": "12:15", "end": "13:00"},
    {"period": 8, "start": "13:00", "end": "13:45"},
]

DAYS = {
    "segunda": [
        ("IoT & Sistemas Cyber Físicos", "Yan Schulz Gramani"),
        ("Língua Portuguesa e Literatura", "Tainah Franghieru"),
        ("Química", "Débora Féu Médice"),
        ("Química", "Débora Féu Médice"),
        ("Hands-on Project", "Yan Schulz Gramani"),
        ("Hands-on Project", "Yan Schulz Gramani"),
        ("Hands-on Project", "Yan Schulz Gramani"),
        ("História e Filosofia", "Denis de Sena Ramos"),
    ],
    "terca": [
        ("Desenvolvimento Mobile Multiplataforma Flutter", "Alex Sander de Deus"),
        ("Desenvolvimento Mobile Multiplataforma Flutter", "Alex Sander de Deus"),
        ("Língua Inglesa", "Adriana Gioeilli Addario Vidal"),
        ("Língua Inglesa", "Adriana Gioeilli Addario Vidal"),
        ("Pensamento Computacional com Python", "Alex Sander de Deus"),
        ("Ed. Física", "Glauco Kruth Nappi"),
        ("Língua Portuguesa e Literatura", "Tainah Franghieru"),
        ("Matemática", "Rafaela Maria Rodrigues Pimentel Servilha"),
    ],
    "quarta": [
        ("Língua Inglesa", "Adriana Gioeilli Addario Vidal"),
        ("Física", "Neil Saborido Silva"),
        ("Física", "Neil Saborido Silva"),
        ("Física", "Neil Saborido Silva"),
        ("Design de Software", "Daniel Pereira Julião"),
        ("Design de Software", "Daniel Pereira Julião"),
        ("Matemática", "Rafaela Maria Rodrigues Pimentel Servilha"),
        ("Química", "Débora Féu Médice"),
    ],
    "quinta": [
        ("Pensamento Computacional com Python", "Alex Sander de Deus"),
        ("Pensamento Computacional com Python", "Alex Sander de Deus"),
        ("Biologia", "Samuel Elias Vasconcelos Menezes"),
        ("Biologia", "Samuel Elias Vasconcelos Menezes"),
        ("Língua Portuguesa e Literatura", "Tainah Franghieru"),
        ("Língua Portuguesa e Literatura", "Tainah Franghieru"),
        ("Matemática", "Rafaela Maria Rodrigues Pimentel Servilha"),
        ("Língua Inglesa", "Adriana Gioeilli Addario Vidal"),
    ],
    "sexta": [
        ("Produção e Interpretação de Textos", "Bianca Garcia Viana Soares"),
        ("Geografia e Sociologia", "André Alves de Lucena"),
        ("Língua Portuguesa e Literatura", "Tainah Franghieru"),
        ("IoT & Sistemas Cyber Físicos", "Yan Schulz Gramani"),
        ("IoT & Sistemas Cyber Físicos", "Yan Schulz Gramani"),
        ("Arte", "Talita de Souza Miranda"),
        ("Matemática", "Rafaela Maria Rodrigues Pimentel Servilha"),
        ("Matemática", "Rafaela Maria Rodrigues Pimentel Servilha"),
    ],
}


def main() -> None:
    payload = {
        "periods": PERIODS,
        "days": {
            name: [{"subject": s, "teacher": t} for s, t in lessons]
            for name, lessons in DAYS.items()
        },
    }
    out = Path(__file__).resolve().parent / "public" / "horario.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"escreveu {out}")


if __name__ == "__main__":
    main()
