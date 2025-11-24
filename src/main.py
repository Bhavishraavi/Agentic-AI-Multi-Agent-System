from graph import build_graph
from memory import update_history
from src.ui.app import main

if __name__ == "__main__":
    main()
    
def run():
    graph = build_graph()
    history = []

    print("🚀 Agentic AI Started (CLI Mode)")
    print("Type 'exit' to quit.\n")

    while True:
        user = input("You: ")

        if user.lower() in ["exit", "quit"]:
            break

        # prepare state
        state = {
            "input": user,
            "plan": "",
            "research": "",
            "tool_result": "",
            "rag_context": "",
            "final_answer": "",
            "history": history,
        }

        # run graph
        result = graph.invoke(state)
        answer = result["final_answer"]

        print("\nAssistant:", answer, "\n")

        # update memory
        history = update_history(history, user, answer)

if __name__ == "__main__":
    run()
