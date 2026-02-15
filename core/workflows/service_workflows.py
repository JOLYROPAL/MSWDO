from core.workflows.base import WorkflowStrategy


class DefaultWorkflow(WorkflowStrategy):
    def allowed_transitions(self) -> dict[str, list[str]]:
        return {
            "Submitted": ["Verified"],
            "Verified": ["Evaluated"],
            "Evaluated": ["Approved", "Referred"],
            "Approved": ["Released"],
            "Released": ["Closed"],
            "Referred": ["Closed"],
        }


class AICSWorkflow(DefaultWorkflow):
    def allowed_transitions(self) -> dict[str, list[str]]:
        transitions = super().allowed_transitions()
        transitions["Evaluated"].append("For Case Conference")
        transitions["For Case Conference"] = ["Approved", "Referred"]
        return transitions
