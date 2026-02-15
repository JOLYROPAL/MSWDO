from abc import ABC, abstractmethod


class WorkflowStrategy(ABC):
    @abstractmethod
    def allowed_transitions(self) -> dict[str, list[str]]:
        raise NotImplementedError

    def can_transition(self, current_status: str, to_status: str) -> bool:
        return to_status in self.allowed_transitions().get(current_status, [])
