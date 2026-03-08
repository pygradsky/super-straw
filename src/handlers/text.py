from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text)
async def process_text(message: Message) -> None:
    """Обрабатывает текстовые сообщения."""
    await message.answer(
        "⚠️ Пожалуйста, отправьте изображение!\n"
        "Или используйте команду /help для справки."
    )
