import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

dane = pd.DataFrame(
    {
        "Miesiąc": [
            "Styczeń",
            "Luty",
            "Marzec",
            "Kwiecień",
            "Maj",
            "Czerwiec",
            "Lipiec",
            "Sierpień",
            "Wrzesień",
            "Październik",
            "Listopad",
            "Grudzień",
        ],
        "SmartTV": [159, 187, 245, 151, 181, 160, 142, 217, 152, 143, 157, 175],
        "TV": [159, 187, 246, 151, 181, 150, 134, 149, 131, 105, 129, 142],
    }
)

miesiace_skrocone = [
    "Sty",
    "Lut",
    "Mar",
    "Kwi",
    "Maj",
    "Cze",
    "Lip",
    "Sie",
    "Wrz",
    "Paź",
    "Lis",
    "Gru",
]
dane["Miesiąc"] = miesiace_skrocone

fig, ax = plt.subplots(figsize=[9, 5])
plt.title("Sprzedaż telewizorów w 2016 roku", fontsize=16, fontweight="bold", y=1.02)
plt.ylabel("Ilość sprzedanych telewizorów")
plt.xticks(range(len(dane)), dane.Miesiąc)
plt.ylim(bottom=0, top=270)

darker_orange = (1.0, 0.3, 0.0)
colors = {"SmartTV": "blue", "TV": darker_orange}
for col in dane.columns[1:]:
    plt.plot(dane["Miesiąc"], dane[col], label=None, color=colors[col])
    if col == "SmartTV":
        plt.annotate(
            col,
            xy=(len(dane) - 1, dane[col].iloc[-1]),
            xytext=(20, 12),
            textcoords="offset points",
            ha="right",
            color=colors[col],
        )
        plt.annotate(
            f"{dane[col].iloc[-5]}",
            xy=(len(dane) - 5, dane[col].iloc[-5]),
            xytext=(10, 8),
            textcoords="offset points",
            ha="right",
            color=colors[col],
        )
    if col == "TV":
        plt.annotate(
            col,
            xy=(len(dane) - 1, dane[col].iloc[-1]),
            xytext=(8, -18),
            textcoords="offset points",
            ha="right",
            color=colors[col],
        )
        plt.annotate(
            f"{dane[col].iloc[-3]}",
            xy=(len(dane) - 3, dane[col].iloc[-3]),
            xytext=(10, -15),
            textcoords="offset points",
            ha="right",
            color=colors[col],
        )

    plt.plot(dane["Miesiąc"][:5], dane[col][:5], label=None, color="gray")

difference = dane["TV"].iloc[-1] - dane["SmartTV"].iloc[-1]
plt.text(
    len(dane) - 0.8,
    dane["TV"].iloc[-1] + 13,
    difference,
    color="darkred",
    ha="right",
    fontweight="bold",
)

plt.axvspan(3.7, 4.3, color="gray", alpha=0.3)
netflix_icon = plt.imread("netflix.png")
imagebox = OffsetImage(netflix_icon, zoom=0.028)
ab = AnnotationBbox(imagebox, (4, 240), frameon=False)
ax.add_artist(ab)
plt.show()
