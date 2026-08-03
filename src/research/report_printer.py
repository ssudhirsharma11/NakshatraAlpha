"""
Report Printer

Pretty console output for Nakshatra Alpha
research reports.
"""

from __future__ import annotations

import calendar

from src.models.research_report_row import ResearchReportRow


class ReportPrinter:
    """
    Prints research reports.
    """

    @staticmethod
    def print(
        rows: list[ResearchReportRow],
    ) -> None:

        if not rows:

            print("\nNo report data found.\n")
            return

        current_date = None

        for row in rows:

            report_date = row.market_start.date()

            if report_date != current_date:

                current_date = report_date

                weekday = calendar.day_name[
                    report_date.weekday()
                ]

                print()
                print("=" * 90)
                print(
                    f"{report_date:%d-%b-%Y} ({weekday})"
                )
                print("=" * 90)

            ReportPrinter._print_row(row)

    # ---------------------------------------------------------

    @staticmethod
    def _print_row(
        row: ResearchReportRow,
    ) -> None:

        features = row.features
        market = row.market
        mf = row.market_features

        print()

        print(
            f"Hora {row.hora.index} "
            f"({row.hora.planet.name.title()})"
        )

        print("-" * 60)

        print(
            f"Hora Time     : "
            f"{row.hora.start:%H:%M}"
            f" - "
            f"{row.hora.end:%H:%M}"
        )

        print(
            f"Market Time   : "
            f"{row.market_start:%H:%M}"
            f" - "
            f"{row.market_end:%H:%M}"
        )

        # =====================================================
        # TITHI
        # =====================================================

        print()
        print("TITHI")
        print("-" * 60)

        print(
            f"Tithi         : "
            f"{features.tithi.name.replace('_', ' ').title()}"
        )

        print(
            f"Group         : "
            f"{features.tithi_group.name.title()}"
        )

        print(
            f"Lord          : "
            f"{features.tithi_lord.name.title()}"
        )

        print(
            f"Paksha        : "
            f"{features.paksha.name.title()}"
        )

        # =====================================================
        # NAKSHATRA
        # =====================================================

        print()
        print("NAKSHATRA")
        print("-" * 60)

        print(
            f"Nakshatra     : "
            f"{features.moon_nakshatra.name.title()}"
        )

        print(
            f"Pada          : "
            f"{features.pada}"
        )

        # =====================================================
        # LAGNA
        # =====================================================

        print()
        print("LAGNA")
        print("-" * 60)

        print(
            f"Lagna         : "
            f"{features.lagna_sign.name.title()}"
        )

        # =====================================================
        # NAVAMSHA
        # =====================================================

        print()
        print("NAVAMSHA")
        print("-" * 60)

        print(
            f"Moon Navamsha : "
            f"{features.moon_navamsha.name.title()}"
        )

        print(
            f"Sun Navamsha  : "
            f"{features.sun_navamsha.name.title()}"
        )

        # =====================================================
        # SATURN ANALYSIS
        # =====================================================

        print()
        print("SATURN ANALYSIS")
        print("-" * 60)

        print(
            f"Saturn Sign   : "
            f"{features.saturn_sign.name.title()}"
        )

        print(
            f"From Sun      : "
            f"{features.saturn_from_sun}"
            f" "
            f"({'Kendra' if features.saturn_kendra_from_sun else 'Not Kendra'})"
        )

        print(
            f"From Moon     : "
            f"{features.saturn_from_moon}"
            f" "
            f"({'Kendra' if features.saturn_kendra_from_moon else 'Not Kendra'})"
        )

        print()

        print(
            f"Sade Sati     : "
            f"{'Yes' if features.sade_sati else 'No'}"
        )

        if features.sade_sati:

            print(
                f"Phase         : "
                f"{features.sade_sati_phase}"
            )

        # =====================================================
        # MARKET
        # =====================================================

        print()
        print("MARKET")
        print("-" * 60)

        print(
            f"Open          : "
            f"{market.open:.2f}"
        )

        print(
            f"High          : "
            f"{market.high:.2f}"
        )

        print(
            f"Low           : "
            f"{market.low:.2f}"
        )

        print(
            f"Close         : "
            f"{market.close:.2f}"
        )

        print()

        print(
            f"Maximum Rise  : "
            f"{market.up_move:.2f}"
        )

        print(
            f"Maximum Fall  : "
            f"{market.down_move:.2f}"
        )

        print()

        print(
            f"Return %      : "
            f"{mf.return_pct:.2f}"
        )

        print(
            f"Direction     : "
            f"{mf.direction}"
        )

        print(
            f"Strength      : "
            f"{mf.strength}"
        )

        print()

        print(
            f"Range         : "
            f"{market.trading_range:.2f}"
        )

        print(
            f"Body          : "
            f"{mf.body:.2f}"
        )

        print(
            f"Candles       : "
            f"{market.candle_count}"
        )

        print()