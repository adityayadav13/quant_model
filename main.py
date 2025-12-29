from fastapi import FastAPI
from state_builder import get_live_price
from model_loader import model
from feature_builder import build_features

app = FastAPI()

LAST_DECISION = {
    "side": "HOLD",
    "confidence": 0.0,
    "price": 0.0
}

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/market/price")
def market_price():
    price = get_live_price()
    return {
        "symbol": "BTCUSDT",
        "price": price
    }

@app.post("/agent/step")
def run_model():
    global LAST_DECISION

    state = get_live_price(as_state=True)
    X = build_features(state)

    probs = model.predict_proba(X)[0]
    classes = model.classes_

    idx = probs.argmax()
    label = classes[idx]
    confidence = float(probs[idx])

    if confidence < 0.6:
        side = "HOLD"
    else:
        side = {0: "BUY", 2: "SELL", 3: "HOLD"}[label]

    LAST_DECISION = {
        "side": side,
        "confidence": confidence,
        "price": state["close"]
    }

    return LAST_DECISION

@app.get("/agent/decision")
def decision():
    return LAST_DECISION
