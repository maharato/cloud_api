from sqlalchemy import select
from app.models.story import StoryProgress


class StoryService:

    @staticmethod
    async def get_story(db, player_id):
        result = await db.execute(
            select(StoryProgress).where(StoryProgress.player_id == player_id)
        )
        story = result.scalar_one_or_none()

        if not story:
            story = StoryProgress(player_id=player_id)
            db.add(story)
            await db.commit()
            await db.refresh(story)

        return story

    @staticmethod
    async def update_story(db, player_id, data):
        result = await db.execute(
            select(StoryProgress).where(StoryProgress.player_id == player_id)
        )
        story = result.scalar_one_or_none()

        if not story:
            story = StoryProgress(player_id=player_id)
            db.add(story)

        story.current_story_state = data.storyState
        story.current_ending = data.ending
        story.is_finished = data.isFinished
        story.choices_json = data.choices

        await db.commit()
        await db.refresh(story)
        return story