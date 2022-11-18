from pydantic import BaseModel


class TeamModel(BaseModel):
    user_id: int
    name: str
    contact_face: str | None
    link_vk: str | None
    tel_number: str | None
    institute: str | None


class UpdateTeam(TeamModel):
    user_id: int | None
    name: str | None


class TeamPointsModel(BaseModel):
    user_id: int
    current_question: int
    result: int


class UpdateTeamPoints(TeamPointsModel):
    user_id: int | None
    current_question: int | None
    result: int | None
