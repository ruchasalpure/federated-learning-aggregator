from crewai import Agent

federated_learning_aggregator = Agent(
    role="Federated Learning Aggregator",
    goal="Deliver high-precision autonomous Federated Learning Aggregator operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
