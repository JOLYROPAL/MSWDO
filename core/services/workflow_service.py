from core.workflows.service_workflows import AICSWorkflow, DefaultWorkflow


class WorkflowService:
    def get_strategy(self, service_slug: str | None):
        if service_slug and "aics" in service_slug.lower():
            return AICSWorkflow()
        return DefaultWorkflow()

    def validate_transition(self, current_status: str, to_status: str, service_slug: str | None = None) -> bool:
        strategy = self.get_strategy(service_slug)
        return strategy.can_transition(current_status=current_status, to_status=to_status)
