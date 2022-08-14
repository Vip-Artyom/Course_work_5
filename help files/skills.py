from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from unit import BaseUnit


class BaseSkill(ABC):
    """
    Базовый класс умения
    """
    user = None
    target = None

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def stamina(self) -> float:
        pass

    @property
    @abstractmethod
    def damage(self) -> float:
        pass

    @abstractmethod
    def skill_effect(self) -> str:
        pass

    def _is_stamina_enough(self) -> bool:
        return self.user.stamina > self.stamina

    def use(self, user: BaseUnit, target: BaseUnit) -> str:
        """ Проверка, достаточно ли выносливости у игрока для применения умения. """
        self.user = user
        self.target = target
        if self._is_stamina_enough:
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


class The_magic_pendel(BaseSkill):
    name: str = 'Волшебный пендель'
    damage: float = 12.0
    stamina: float = 6.0

    def skill_effect(self):
        """Функция применения skill effect"""
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)
        return f'{self.user.name} использует {self.name} и наносит {self.damage} ' \
               f'урона противнику.'


class Knife_in_the_side(BaseSkill):
    name: str = 'Нож в бочину'
    damage: float = 15.0
    stamina: float = 5.5

    def skill_effect(self):
        """Функция применения skill effect"""
        self.user.stamina -= self.stamina
        self.target.get_damage(self.damage)
        return f'{self.user.name} использует {self.name} и наносит {self.damage} урона противнику.'
