class CostTracker:
    def estimate_mock_cost(self, prompt_tokens: int, completion_tokens: int) -> float:
        """
        Mock cost estimator.
        Later this can be replaced with real provider pricing.
        """

        cost_per_1k_tokens = 0.0005
        total_tokens = prompt_tokens + completion_tokens
        cost = (total_tokens / 1000) * cost_per_1k_tokens

        return round(cost, 6)
