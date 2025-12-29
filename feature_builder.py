def build_features(state):
    return [[
        state["open"],
        state["high"],
        state["low"],
        state["close"],
        state["volume"],
        state.get("market_cap", 0)
    ]]