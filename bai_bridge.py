# bai_bridge.py

from bai_manager import search_nodes, get_full_chain
import time

def activate_bai():
    print("Activating Bai System...")
    # Simulate a startup "play, pretend" mode
    print("Bai status: dormant")
    time.sleep(1)
    print("Bai status: awakening...")
    time.sleep(1)
    print("Bai status: active and ready.\n")

def demo_search_and_display(keyword):
    print(f"Searching for keyword: '{keyword}'\n")
    results = search_nodes(keyword)
    if not results:
        print("No matching nodes found.")
        return
    for r in results:
        print(f"Node {r['index']} - {r['key']} ({r['category']})")
        for c in r['chain']:
            print(f"  > {c}")
        print()

if __name__ == "__main__":
    activate_bai()
    demo_search_and_display("folklore")
    demo_search_and_display("stan")
