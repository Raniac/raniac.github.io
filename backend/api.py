from sanic.response import json
from sanic.log import logger
from sanic import Blueprint

# ================================ Portfolio ================================

portfolio = Blueprint("portfolio", url_prefix="/portfolio")

@portfolio.route("/")
async def portfolio_root(request):
    logger.info(request.body)
    return json({"msg": "success"})

# ================================ Blog ================================

blog = Blueprint("blog", url_prefix="/blog")

@blog.route("/")
async def blog_root(request):
    logger.info(request.body)
    return json({"msg": "success"})

# ================================ ToolKit ================================

toolkit = Blueprint("toolkit", url_prefix="/toolkit")

@toolkit.route("/")
async def toolkit_root(request):
    logger.info(request.body)
    return json({"msg": "success"})
