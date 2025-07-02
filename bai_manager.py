# bai_manager.py

import datetime
from who_is_b import nodes

# Add metadata and create complex chains

for key, val in nodes.items():
    # Category based on index
    if val["index"] <= 22:
        category = "Taylor Swift"
    else:
        category = "Eminem"
    
    val["metadata"] = {
        "category": category,
        "created": datetime.datetime.now().isoformat(),
        "related": [val["tier1"].split("::")[0].strip()]  # top-level category as related
    }
    
    val["chain"] = [val["tier1"], val["tier2"], val["tier3"]]

def search_nodes(keyword):
    """Search nodes by keyword in any tier or key."""
    keyword = keyword.lower()
    results = []
    for key, val in nodes.items():
        if (
            keyword in key.lower() or
            any(keyword in tier.lower() for tier in val["chain"])
        ):
            results.append({
                "key": key,
                "index": val["index"],
                "category": val["metadata"]["category"],
                "chain": val["chain"],
                "metadata": val["metadata"],
            })
    return results

def get_full_chain(key):
    """Return the full tier chain and metadata for a given node key."""
    node = nodes.get(key)
    if node:
        return {
            "key": key,
            "index": node["index"],
            "category": node["metadata"]["category"],
            "chain": node["chain"],
            "metadata": node["metadata"],
        }
    else:
        return None

if __name__ == "__main__":
    # Example search test
    results = search_nodes("folklore")
    print(f"Found {len(results)} nodes matching 'folklore':\n")
    for r in results:
        print(f"Index {r['index']} - Key: {r['key']}")
        for c in r['chain']:
            print(f"  > {c}")
        print(f"  Category: {r['category']}")
        print(f"  Metadata created at: {r['metadata']['created']}\n")

    # Example full chain fetch
    stan_chain = get_full_chain("stan")
    print("Full chain for 'stan':")
    print(stan_chain)
