from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from api.reviews.schemas import ReviewSchema
from api.models import Review


async def _create_review(review: ReviewSchema, db: AsyncSession):
    stmt = Review(**review.model_dump())
    await db.add(stmt)
    await db.commit()
    await db.refresh(stmt)
    return stmt


async def _read_review(review_id: int, db: AsyncSession):
    stmt = await select(Review).where(Review.id == review_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Отзыв не найден")
    return result


async def _update_review(review_id: int, review: ReviewSchema, db: AsyncSession):
    stmt = await select(Review).where(Review.id == review_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Отзыв не найден")
    for key, value in review.items():
        setattr(result, key, value)
    await db.commit()
    await db.refresh(result)
    return result


async def _delete_review(review_id: int, db: AsyncSession):
    stmt = await select(Review).where(Review.id == review_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Отзыв не найден")
    await db.delete(result)
    await db.commit()
    return result
