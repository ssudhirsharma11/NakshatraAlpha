"""
Console Printer

Pretty prints the validation output for
Nakshatra Alpha.
"""

from __future__ import annotations

from src.models.chart import Chart
from src.models.feature_set import FeatureSet
from src.models.market_features import MarketFeatures
from src.models.market_snapshot import MarketSnapshot


class ConsolePrinter:
    """
    Prints one Hora validation report.
    """

    @staticmethod
    def line() -> None:
        print("-" * 60)

    @staticmethod
    def heading(title: str) -> None:
        print()
        ConsolePrinter.line()
        print(title)
        ConsolePrinter.line()

    @staticmethod
    def item(
        label: str,
        value,
    ) -> None:
        print(f"{label:<25}: {value}")

    def print_report(
        self,
        chart: Chart,
        features: FeatureSet,
        market: MarketSnapshot,
        market_features: MarketFeatures,
    ) -> None:

        self.heading("GENERAL")

        self.item(
            "Timestamp",
            chart.timestamp,
        )

        self.item(
            "Weekday",
            chart.timestamp.strftime("%A"),
        )

        self.item(
            "Hora",
            f"{features.hora_number} ({features.hora_lord.name if features.hora_lord else '-'})",
        )

        self.item(
            "Tithi",
            features.tithi.name.replace("_", " "),
        )

        self.item(
            "Tithi Group",
            features.tithi_group.value,
        )

        self.item(
            "Tithi Lord",
            features.tithi_lord.name.title(),
        )

        self.item(
            "Paksha",
            features.paksha.name.title(),
        )

        self.heading("NAKSHATRA")

        self.item(
            "Moon Nakshatra",
            f"{features.moon_nakshatra.name} ({features.moon_nakshatra_number})",
        )

        self.item(
            "Sun Nakshatra",
            f"{features.sun_nakshatra.name} ({features.sun_nakshatra_number})",
        )

        self.item(
            "Pada",
            features.pada,
        )

        self.heading("SIGNS")

        self.item(
            "Moon Sign",
            f"{features.moon_sign.name} ({features.moon_sign_number})",
        )

        self.item(
            "Sun Sign",
            f"{features.sun_sign.name} ({features.sun_sign_number})",
        )

        self.item(
            "Moon Navamsha",
            features.moon_navamsha.name,
        )

        self.item(
            "Sun Navamsha",
            features.sun_navamsha.name,
        )

        self.item(
            "Lagna",
            features.lagna_sign.name,
        )

        self.item(
            "Lagna Degree",
            f"{features.lagna_degree:.4f}°",
        )

        self.heading("SATURN")

        self.item(
            "Saturn Sign",
            features.saturn_sign.name,
        )

        self.item(
            "From Sun",
            features.saturn_from_sun,
        )

        self.item(
            "From Moon",
            features.saturn_from_moon,
        )

        self.item(
            "Kendra",
            features.saturn_kendra_from_sun,
        )

        self.item(
            "Sade Sati",
            features.sade_sati,
        )

        self.item(
            "Phase",
            features.sade_sati_phase,
        )

        self.heading("PLANETS")

        self.item(
            "Sun Longitude",
            round(chart.sun.longitude, 4),
        )

        self.item(
            "Moon Longitude",
            round(chart.moon.longitude, 4),
        )

        self.item(
            "Mars Longitude",
            round(chart.mars.longitude, 4),
        )

        self.item(
            "Mercury Longitude",
            round(chart.mercury.longitude, 4),
        )

        self.item(
            "Jupiter Longitude",
            round(chart.jupiter.longitude, 4),
        )

        self.item(
            "Venus Longitude",
            round(chart.venus.longitude, 4),
        )

        self.item(
            "Saturn Longitude",
            round(chart.saturn.longitude, 4),
        )

        self.item(
            "Rahu Longitude",
            round(chart.rahu.longitude, 4),
        )

        self.item(
            "Ketu Longitude",
            round(chart.ketu.longitude, 4),
        )

        self.heading("MARKET")

        self.item("Open", market.open)
        self.item("High", market.high)
        self.item("Low", market.low)
        self.item("Close", market.close)

        self.item(
            "Trading Range",
            market.trading_range,
        )

        self.item(
            "Return %",
            round(
                market_features.return_pct,
                3,
            ),
        )

        self.item(
            "Direction",
            market_features.direction,
        )

        self.item(
            "Strength",
            market_features.strength,
        )

        print()