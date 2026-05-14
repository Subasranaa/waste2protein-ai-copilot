from app.schemas import PredictionInput


class EconomicsService:
    def estimate(
        self,
        input_data: PredictionInput,
        predicted_protein_yield: float,
    ) -> dict:
        """
        Scenario-based economic estimate.

        This is not a trained economics model yet.
        It provides an early feasibility estimate for decision-support.
        """

        protein_kg = input_data.waste_volume_kg * (predicted_protein_yield / 100)

        estimated_revenue_gbp = protein_kg * 4.5
        estimated_processing_cost_gbp = input_data.waste_volume_kg * 1.2
        estimated_margin_gbp = estimated_revenue_gbp - estimated_processing_cost_gbp

        if estimated_margin_gbp > 300:
            viability = "high"
        elif estimated_margin_gbp > 0:
            viability = "medium"
        else:
            viability = "low"

        return {
            "estimated_protein_kg": round(protein_kg, 2),
            "estimated_revenue_gbp": round(estimated_revenue_gbp, 2),
            "estimated_processing_cost_gbp": round(estimated_processing_cost_gbp, 2),
            "estimated_margin_gbp": round(estimated_margin_gbp, 2),
            "economic_viability": viability,
            "method": "scenario-based feasibility estimate",
            "note": "This estimate uses simplified assumptions and should be refined with real processing, logistics, energy, and market data.",
        }
