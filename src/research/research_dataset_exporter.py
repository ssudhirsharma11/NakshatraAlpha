"""
Research Dataset Exporter

Exports ResearchReportRow objects to a research dataset.
"""

from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

import pandas as pd

from src.research.research_builder import ResearchBuilder


class ResearchDatasetExporter:

    def __init__(self):

        self.builder = ResearchBuilder()

    # =====================================================
    # PUBLIC
    # =====================================================

    def export_day(
        self,
        trading_date: date,
        hora_number: int | None = None,
    ) -> pd.DataFrame:

        rows = self.builder.build_day(
            trading_date,
            hora_number,
        )

        return self._rows_to_dataframe(rows)

    def export_range(
        self,
        start_date: date,
        end_date: date,
        hora_number: int | None = None,
    ) -> pd.DataFrame:

        frames = []

        current = start_date

        while current <= end_date:

            print(f"Processing {current}")

            try:

                df = self.export_day(
                    current,
                    hora_number,
                )

                if not df.empty:
                    frames.append(df)

            except ValueError:

                # Weekend / holiday / no market data
                pass

            current += timedelta(days=1)

        if not frames:

            return pd.DataFrame()

        return pd.concat(
            frames,
            ignore_index=True,
        )

    def save(
        self,
        df: pd.DataFrame,
        parquet_file: Path,
        csv_file: Path | None = None,
    ):

        parquet_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        df.to_parquet(
            parquet_file,
            index=False,
        )

        if csv_file is not None:

            df.to_csv(
                csv_file,
                index=False,
            )

    # =====================================================
    # INTERNAL
    # =====================================================

    def _rows_to_dataframe(
        self,
        rows,
    ) -> pd.DataFrame:

        records = []

        previous_close = None

        for row in rows:

            record = self._row_to_dict(
                row,
                previous_close,
            )

            records.append(record)

            previous_close = row.market.close

        return pd.DataFrame(records)

    def _row_to_dict(
        self,
        row,
        previous_close,
    ) -> dict:

        features = row.features
        market = row.market
        mf = row.market_features

        return {
                        # ==================================================
            # Identity
            # ==================================================

            "research_id": (
                f"{row.market_start:%Y%m%d}_H{row.hora.index:02d}"
            ),

            "trading_date": row.market_start.date(),

            "year": row.market_start.year,

            "month": row.market_start.month,

            "month_name": row.market_start.strftime("%B"),

            "quarter": (
                (row.market_start.month - 1) // 3
            ) + 1,

            "day": row.market_start.day,

            "weekday_number": row.market_start.weekday(),

            "weekday": row.market_start.strftime("%A"),

            "hora_number": row.hora.index,

            "hora_lord": row.hora.planet.name,

            "hora_start": row.hora.start,

            "hora_end": row.hora.end,

            "market_start": row.market_start,

            "market_end": row.market_end,

            "hora_duration_minutes": (
                row.hora.end - row.hora.start
            ).total_seconds() / 60,

            "market_duration_minutes": (
                row.market_end - row.market_start
            ).total_seconds() / 60,

            "dataset_version": "1.0",

            # ==================================================
            # Tithi
            # ==================================================

            "tithi": (
                features.tithi.name
                if features.tithi
                else None
            ),

            "tithi_number": features.tithi_number,

            "tithi_group": (
                features.tithi_group.name
                if features.tithi_group
                else None
            ),

            "tithi_lord": (
                features.tithi_lord.name
                if features.tithi_lord
                else None
            ),

            "paksha": (
                features.paksha.name
                if features.paksha
                else None
            ),

            # ==================================================
            # Nakshatra
            # ==================================================

            "moon_nakshatra": (
                features.moon_nakshatra.name
                if features.moon_nakshatra
                else None
            ),

            "moon_nakshatra_number":
                features.moon_nakshatra_number,

            "sun_nakshatra": (
                features.sun_nakshatra.name
                if features.sun_nakshatra
                else None
            ),

            "sun_nakshatra_number":
                features.sun_nakshatra_number,

            "pada":
                features.pada,

            # ==================================================
            # Lagna
            # ==================================================

            "lagna": (
                features.lagna_sign.name
                if features.lagna_sign
                else None
            ),

            "lagna_number":
                features.lagna_number,

            "lagna_degree":
                features.lagna_degree,

            # ==================================================
            # Planet Positions
            # ==================================================

            "sun_sign": (
                features.sun_sign.name
                if features.sun_sign
                else None
            ),

            "moon_sign": (
                features.moon_sign.name
                if features.moon_sign
                else None
            ),

            "sun_navamsha": (
                features.sun_navamsha.name
                if features.sun_navamsha
                else None
            ),

            "moon_navamsha": (
                features.moon_navamsha.name
                if features.moon_navamsha
                else None
            ),

            "saturn_sign": (
                features.saturn_sign.name
                if features.saturn_sign
                else None
            ),            # ==================================================
            # Saturn
            # ==================================================

            "saturn_from_sun":
                features.saturn_from_sun,

            "saturn_kendra_from_sun":
                features.saturn_kendra_from_sun,

            "saturn_from_moon":
                features.saturn_from_moon,

            "saturn_kendra_from_moon":
                features.saturn_kendra_from_moon,

            "sade_sati":
                features.sade_sati,

            "sade_sati_phase":
                features.sade_sati_phase,

            # ==================================================
            # Market
            # ==================================================

            "open":
                market.open,

            "high":
                market.high,

            "low":
                market.low,

            "close":
                market.close,

            "up_move":
                market.up_move,

            "down_move":
                market.down_move,

            "trading_range":
                market.trading_range,

            "candle_count":
                market.candle_count,

            # ==================================================
            # Derived Market
            # ==================================================

            "body":
                mf.body,

            "return_pct":
                mf.return_pct,

            "range_pct":
                mf.range_pct,

            "body_pct":
                mf.body_pct,

            "upper_wick":
                mf.upper_wick,

            "lower_wick":
                mf.lower_wick,

            "upper_wick_pct":
                mf.upper_wick_pct,

            "lower_wick_pct":
                mf.lower_wick_pct,

            "close_position_pct":
                mf.close_position_pct,

            "open_position_pct":
                mf.open_position_pct,

            "direction":
                mf.direction,

            "strength":
                mf.strength,

            "high_volatility":
                mf.high_volatility,

            "low_volatility":
                mf.low_volatility,
        }