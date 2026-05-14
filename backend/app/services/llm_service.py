from app.schemas import PredictionInput


class LLMService:
    def generate_insight(self, input_data: PredictionInput, prediction_result: dict) -> dict:
        """
        Mock LLM service for now.
        Later we will replace this with Groq/OpenAI/Ollama.
        """

        predicted_yield = prediction_result["predicted_protein_yield"]
        uncertainty = prediction_result["uncertainty"]

        if predicted_yield >= 55:
            yield_comment = "The predicted protein yield is relatively strong."
        elif predicted_yield >= 35:
            yield_comment = "The predicted protein yield is moderate and may be improved through process optimisation."
        else:
            yield_comment = "The predicted protein yield is low, suggesting that this waste stream may need additional optimisation."

        limiting_factors = []

        if input_data.ph < 5.5 or input_data.ph > 7.0:
            limiting_factors.append("pH is outside the preferred fermentation range.")

        if input_data.temperature < 28 or input_data.temperature > 35:
            limiting_factors.append("Temperature may not be optimal for microbial growth.")

        if input_data.nitrogen_content < 1.5:
            limiting_factors.append("Nitrogen content appears low and may limit protein formation.")

        if input_data.sugar_content < 10:
            limiting_factors.append("Sugar content is low, which may reduce available substrate for microbial growth.")

        if not limiting_factors:
            limiting_factors.append("No major limiting factor detected from the provided inputs.")

        recommendations = [
            "Run a small-batch fermentation trial before scale-up.",
            "Monitor pH, temperature, and nitrogen balance during fermentation.",
            "Compare at least two microbial candidates such as yeast and fungi.",
            "Track yield, processing cost, and reproducibility across batches."
        ]

        roadmap = [
            "Validate waste composition with lab analysis.",
            "Run controlled bench-scale fermentation.",
            "Optimise pH and temperature conditions.",
            "Evaluate microbial strain performance.",
            "Estimate economic feasibility before pilot-scale production."
        ]

        return {
            "summary": yield_comment,
            "limiting_factors": limiting_factors,
            "recommendations": recommendations,
            "r_and_d_roadmap": roadmap,
            "confidence_note": f"Model uncertainty is approximately ±{uncertainty}. Results should be treated as decision-support, not final lab validation."
        }
