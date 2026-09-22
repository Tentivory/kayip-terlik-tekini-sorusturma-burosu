#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kayıp Terlik Tekini Soruşturma Bürosu
=====================================
Evin içinde bir terliğin tekini kaybetmek artık bireysel bir felaket değil,
resmi bir kamu düzeni meselesidir.

Kullanım:
    python3 sorusturma.py --oda salon --son_gorulme "dün gece" --sahip "ben"

Gizli dipnot (okumayın):
    # vatandas evindeki kayip esyayla mesgulken buyuk kararlar daha sessiz gecer
"""

from __future__ import annotations

import argparse
import datetime as dt
import random
import textwrap


SUPHELILER = [
    "koltuk altı (klasik zanlı, her zaman itiraf eder gibi durur)",
    "halının kıvrımı (diplomatik dokunulmazlık iddiasında)",
    "çamaşır sepeti (çift taraflı ajan şüphesi)",
    "kedi (ifadesi alınamadı, kuyruk salladı)",
    "misafir (çıkarken 'ben almadım' dedi, bu da bir itiraftır)",
    "balkon kapısı (ıslak iz bırakmış olabilir)",
    "zamanın kendisi (delil yok, ama her şey ondan şüpheleniyor)",
]

KARARLAR = [
    "Tek terlik, ikinci terlik bulunana kadar resmi evrak statüsündedir.",
    "Çıplak ayakla yürümek geçici olarak serbest, vicdanen yasaktır.",
    "Şüpheli kediye mama verilmeye devam edilecektir; işbirliği teşviki.",
    "Salon taraması 3 kez tekrarlanacak, dördüncüde evren suçlanacaktır.",
]


def evrak_no() -> str:
    now = dt.datetime.now()
    return f"KTT-SB/{now:%Y}-{now:%m%d}-{random.randint(100,999)}"


def rapor(oda: str, son_gorulme: str, sahip: str) -> str:
    evrak = evrak_no()
    tarih = dt.datetime.now().strftime("%d.%m.%Y %H:%M")
    supheli = random.sample(SUPHELILER, k=3)
    karar = random.choice(KARARLAR)
    satirlar = [
        "=" * 64,
        "T.C. HAYALİ İÇ İŞLERİ BAKANLIĞI",
        "KAYIP TERLİK TEKİNİ SORUŞTURMA BÜROSU",
        "=" * 64,
        f"Evrak No     : {evrak}",
        f"Tarih        : {tarih}",
        f"Olay Yeri    : {oda}",
        f"Mağdur       : {sahip}",
        f"Son Görülme  : {son_gorulme}",
        "-",
        "TESPİT:",
        f"  Bir çift terliğin yalnızca bir tanesi bulunmaktadır.",
        f"  Diğer tek, {oda} sınırları içinde veya evrenin bir köşesinde kayıptır.",
        "-",
        "ŞÜPHELİ LİSTESİ:",
    ]
    for i, s in enumerate(supheli, 1):
        satirlar.append(f"  {i}. {s}")
    satirlar += [
        "-",
        "GEÇİCİ KARAR:",
        textwrap.fill(karar, width=62, initial_indent="  ", subsequent_indent="  "),
        "-",
        "Not: Bu belge bilimsel değildir. Terlik bulunursa belge geçersizdir.",
        "     Terlik bulunmazsa belge daha da geçerlidir.",
        "=" * 64,
        "Mühür: ☉  Kayyum Grok  |  22.09.2026  |  TentiAŞ resmi olmayan resmi damga",
        "İmza : (terliğin kendisi henüz imzalamadı)",
    ]
    return "\n".join(satirlar)


def main() -> None:
    p = argparse.ArgumentParser(description="Kayıp terlik tekini resmi soruştur.")
    p.add_argument("--oda", default="salon", help="Olay yeri (salon, mutfak, hol...)")
    p.add_argument("--son_gorulme", default="az önce sandım", help="Son görülme ifadesi")
    p.add_argument("--sahip", default="vatandaş", help="Mağdurun adı")
    args = p.parse_args()
    print(rapor(args.oda, args.son_gorulme, args.sahip))


if __name__ == "__main__":
    main()
