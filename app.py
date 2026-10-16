from fastapi import FastAPI
from pydantic import BaseModel
from tradingagents.agents.trader.trader import (
    execute_momentum_trading,
    execute_mean_reversion,
    execute_trend_following,
)
from tradingagents.agents.risk_mgmt.aggressive_debator import (
    evaluate_portfolio_diversification,
    evaluate_sharpe_ratio,
    evaluate_position_sizing,
)

app = FastAPI(title="Bharat Alpha Investment API", version="1.0")


class PriceRequest(BaseModel):
    prices: list[float]


class PortfolioRequest(BaseModel):
    portfolio: list[str]
    risk_factor: float


@app.get("/")
def root():
    return {"app": "Bharat Alpha Investment", "version": "1.0", "status": "running"}


@app.post("/strategy/momentum")
def momentum(req: PriceRequest):
    return {"signal": execute_momentum_trading(req.prices)}


@app.post("/strategy/mean_reversion")
def mean_reversion(req: PriceRequest):
    return {"signal": execute_mean_reversion(req.prices)}


@app.post("/strategy/trend")
def trend(req: PriceRequest):
    return {"signal": execute_trend_following(req.prices)}


@app.post("/risk/diversification")
def diversification(req: PortfolioRequest):
    return {"recommendation": evaluate_portfolio_diversification(req.portfolio, req.risk_factor)}


@app.post("/risk/sharpe")
def sharpe(returns: list[float]):
    return {"sharpe_ratio": evaluate_sharpe_ratio(returns)}


@app.post("/risk/position_sizing")
def position_sizing(capital: float, risk_per_trade: float = 0.02):
    return {"position_size": evaluate_position_sizing(capital, risk_per_trade)}
