from typing import List

from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db import async_session
from models import Team, TeamPoints
from schemas import UpdateTeam, TeamModel, UpdateTeamPoints


class Db:

    async def check_exist(self, user_id: int) -> bool:
        db: AsyncSession
        async with async_session() as db:
            async with db.begin():
                result = await db.execute(select(Team).where(Team.user_id == user_id))

        try:
            team: Team = result.scalar_one()
            print(f'Team {user_id} found {team}')
        except NoResultFound:
            print(f'Team {user_id} not found')
            return False

        return True

    async def _create_team(self, team: TeamModel) -> None:
        new_team = Team(**team.dict())
        new_team_points = TeamPoints(user_id=team.user_id)

        db: AsyncSession
        async with async_session() as db:
            async with db.begin():
                db.add(new_team)
                db.add(new_team_points)

                await db.flush()
                await db.refresh(new_team)
                await db.refresh(new_team_points)

    async def _update_team(self, user_id: int, team: UpdateTeam) -> None:
        db: AsyncSession
        async with async_session() as db:
            async with db.begin():
                result = await db.execute(select(Team).where(Team.user_id == user_id).with_for_update())

                try:
                    updated_team: Team = result.scalar_one()
                except NoResultFound:
                    raise

                for key, value in team.dict(exclude_unset=True).items():
                    if hasattr(updated_team, key):
                        setattr(updated_team, key, value)

                await db.flush()
                await db.refresh(updated_team)

    async def _update_team_points(self, user_id: int, team_points: UpdateTeamPoints) -> None:
        db: AsyncSession
        async with async_session() as db:
            async with db.begin():
                result = await db.execute(select(TeamPoints).where(TeamPoints.user_id == user_id).with_for_update())

                try:
                    updated_team_points: TeamPoints = result.scalar_one()
                except NoResultFound:
                    raise

                for key, value in team_points.dict(exclude_unset=True).items():
                    if hasattr(updated_team_points, key):
                        setattr(updated_team_points, key, value)

                await db.flush()
                await db.refresh(updated_team_points)

    async def create_team(self, user_id: int, team_name: str = '') -> None:
        exist = await self.check_exist(user_id)
        if not exist:
            team = TeamModel(user_id=user_id, name=team_name)
            await self._create_team(team)
            print(f"Team with id={user_id} created")
        else:
            update_team = UpdateTeam(name=team_name)
            await self._update_team(user_id, update_team)
            print(f"Team with id={user_id} updated")

    async def add_contact_face(self, user_id: int, contact_face: str):
        exist = await self.check_exist(user_id)
        if exist:
            update_team = UpdateTeam(contact_face=contact_face)
            await self._update_team(user_id, update_team)
            print(f"Team with id={user_id} contact_face updated")
        else:
            print(f"Team with id={user_id} doesn't exist")

    async def add_link_vk(self, user_id: int, link_vk: str):
        exist = await self.check_exist(user_id)
        if exist:
            update_team = UpdateTeam(link_vk=link_vk)
            await self._update_team(user_id, update_team)
            print(f"Team with id={user_id} link_vk updated")
        else:
            print(f"Team with id={user_id} doesn't exist")

    async def add_tel_number(self, user_id: int, tel_number: str):
        exist = await self.check_exist(user_id)
        if exist:
            update_team = UpdateTeam(tel_number=tel_number)
            await self._update_team(user_id, update_team)
            print(f"Team with id={user_id} tel_number updated")
        else:
            print(f"Team with id={user_id} doesn't exist")

    async def add_institute(self, user_id: int, institute: str):
        exist = await self.check_exist(user_id)
        if exist:
            update_team = UpdateTeam(institute=institute)
            await self._update_team(user_id, update_team)
            print(f"Team with id={user_id} institute updated")
        else:
            print(f"Team with id={user_id} doesn't exist")

    async def get_result(self, user_id: int) -> int:
        db: AsyncSession
        async with async_session() as db:
            async with db.begin():
                result = await db.execute(select(TeamPoints).where(TeamPoints.user_id == user_id))

        try:
            team_points: TeamPoints = result.scalar_one()
        except NoResultFound:
            print(f'Team Points for user {user_id} not found')
            raise

        return team_points.result

    async def get_current_question(self, user_id: int) -> int:
        db: AsyncSession
        async with async_session() as db:
            async with db.begin():
                result = await db.execute(select(TeamPoints).where(TeamPoints.user_id == user_id))

        try:
            team_points: TeamPoints = result.scalar_one()
        except NoResultFound:
            print(f'Team Points for user {user_id} not found')
            raise

        return team_points.current_question

    async def set_point(self, user_id: int):
        result = await self.get_result(user_id)
        new_result = result + 1

        update_team_points = UpdateTeamPoints(result=new_result)
        await self._update_team_points(user_id, update_team_points)
        print(f'Result for team with user_id={user_id} updated')

    async def increment_current_question(self, user_id: int, current_question: int) -> None:
        new_question = current_question + 1

        update_team_points = UpdateTeamPoints(current_question=new_question)
        await self._update_team_points(user_id, update_team_points)
        print(f'Current question for team with user_id={user_id} updated')

    async def get_users(self) -> List[TeamModel]:
        db: AsyncSession
        async with async_session() as db:
            async with db.begin():
                result = await db.execute(select(Team))

        teams: List[Team] = result.scalars().all()
        return [TeamModel.from_orm(team) for team in teams]
