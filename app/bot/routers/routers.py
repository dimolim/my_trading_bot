from aiogram import Router
from app.bot.handlers.price import router as price_router

router = Router()
router.include_router(price_router)