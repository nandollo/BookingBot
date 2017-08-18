from abc import abstractmethod, ABC
from typing import List
from .model import Classroom


class ClassroomSource(ABC):

    """
    Class that have the responsibility to save the classroom and to provide access to them.
    """

    @abstractmethod
    def get_classroom(self, identifier: str) -> Classroom:
        """
        Gets a classroom.
        :param identifier: Identifier of the classroom.
        :return: Returns the classroom with the provided name if exist None otherwise.
        """
        pass

    def is_classroom_present(self, identifier: str):
        """
        Tels if a classroom is present inside the source.
        :param identifier: Name of the class that will be checked.
        :return: Returns True if the classroom is present False otherwise.
        """
        return self.get_classroom(identifier) is not None

    @abstractmethod
    def add_classroom(self, classroom: Classroom):
        """
        Adds a classroom to the source.
        :param classroom: Classroom that will be added.
        """
        pass

    @abstractmethod
    def get_all_classrooms(self) -> List[Classroom]:
        """
        Gets all the classroom inside the source.
        :return: Returns a List of all the classrooms inside the source.
        """
        pass
