# 📊 Davčni Kalkulator 2026

Interaktivni davčni kalkulator za upokojence v Sloveniji — pokojnina (ZPIZ) + 2. steber (PDPZ).

## Funkcionalnosti

- Izračun letnega davčnega dolga po progresivni lestvici 2026
- Podpora za mesečno rento ali enkratni odkup 2. stebra
- Seniorska olajšava (70+ let)
- Prispevek za dolgotrajno oskrbo (1%) in OZP (35 €/mes.)
- Prikaz doplačila ali vračila po letni odmeri FURS
- Vizualni prikaz razporeditve po davčnih razredih

## Zaženi lokalno

```bash
pip install streamlit
streamlit run app.py
```

## Deploy na Streamlit Cloud

1. Forkai ta repozitorij
2. Pojdi na [share.streamlit.io](https://share.streamlit.io)
3. Poveži GitHub račun → izberi repo → `app.py`
4. Klikni **Deploy**

## Struktura

```
├── app.py            # Glavna aplikacija
├── requirements.txt  # Python odvisnosti
└── README.md
```

## Davčna zakonodaja 2026

| Postavka | Vrednost |
|---|---|
| Splošna olajšava | 5.551,93 € |
| Seniorska olajšava | 138,80 €/mes. |
| OZP prispevek | 35,00 €/mes. |
| DO prispevek | 1% bruto |
| Pokojninska olajšava | 13,5% pokojnine |
| 1. razred | do 9.721,43 € → 16% |
| 2. razred | do 20.177,30 € → 26% |
| 3. razred | do 35.560,00 € → 33% |
| 4. razred | do 74.160,00 € → 39% |
| 5. razred | nad 74.160,00 € → 50% |
