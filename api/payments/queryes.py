from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from api.payments.schemas import PaymentSchema
from api.models import Payment


async def _create_payment(payment: PaymentSchema, db: AsyncSession):
    stmt = Payment(**payment.model_dump())
    await db.add(stmt)
    await db.commit()
    await db.refresh(stmt)
    return stmt


async def _read_payment(payment_id: int, db: AsyncSession):
    stmt = await select(Payment).where(Payment.id == payment_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return result


async def _delete_payment(payment_id: int, db: AsyncSession):
    stmt = await select(Payment).where(Payment.id == payment_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    await db.delete(result)
    await db.commit()
    return result
