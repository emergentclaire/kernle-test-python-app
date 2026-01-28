#!/usr/bin/env python3
"""Test application using Kernle as a library."""
from kernle import Kernle

def main():
    agent_id = "python-app-test"
    k = Kernle(agent_id)
    
    print("=== Kernle Python App Test ===\n")
    
    # 1. Load memory
    print("1. Loading memory...")
    memory = k.load()
    print(f"   Loaded: {len(memory.get('values', []))} values, "
          f"{len(memory.get('beliefs', []))} beliefs")
    
    # 2. Check for checkpoint
    checkpoint = memory.get('checkpoint')
    if checkpoint:
        print(f"   Last checkpoint: {checkpoint.get('current_task', 'unknown')}")
    else:
        print("   No previous checkpoint")
    
    # 3. Record an episode
    print("\n2. Recording episode...")
    ep_id = k.episode(
        "Testing Kernle Python integration",
        "Success - library works as expected",
        lessons=["Kernle library API is clean", "Memory loads quickly"]
    )
    print(f"   Episode saved: {ep_id[:8]}...")
    
    # 4. Add a note
    print("\n3. Adding note...")
    note_id = k.note("Python integration test completed successfully")
    print(f"   Note saved: {note_id[:8]}...")
    
    # 5. Search
    print("\n4. Searching...")
    results = k.search("integration")
    print(f"   Found {len(results)} results")
    
    # 6. Save checkpoint
    print("\n5. Saving checkpoint...")
    k.checkpoint("Python app test complete")
    print("   Checkpoint saved")
    
    # 7. Check anxiety (using new simpler API)
    print("\n6. Checking anxiety...")
    anxiety = k.anxiety()  # Now works! (alias for get_anxiety_report)
    print(f"   Overall: {anxiety['overall_level']} ({anxiety['overall_score']}/100)")
    
    print("\n=== Test Complete ===")

if __name__ == "__main__":
    main()
