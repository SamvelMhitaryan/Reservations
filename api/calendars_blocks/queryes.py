from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from api.calendars_blocks.schemas import CalendarBlockSchema
from api.models import CalendarBlock


async def _create_calendar_block(calendar_block: CalendarBlockSchema, db: AsyncSession):
    stmt = CalendarBlock(**calendar_block.BaseModel())
    db.add(stmt)
    await db.commit()
    await db.refresh(stmt)
    return stmt


async def _read_calendar_block(calendar_block_id: int, db: AsyncSession):
    stmt = await db.select(CalendarBlock).where(CalendarBlock.id == calendar_block_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Calendar block not found")
    return result


async def _delete_calendar_block(calendar_block_id: int, db: AsyncSession):
    stmt = await select(CalendarBlock).where(CalendarBlock.id == calendar_block_id)
    result = stmt.scalars().first()
    if result is None:
        raise HTTPException(status_code=404, detail="Calendar block not found")
    await db.delete(result)
    await db.commit()
    return result
