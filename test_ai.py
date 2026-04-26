from ai_interpreter import AIInterpreter

def test_reliability():
    interpreter = AIInterpreter()
    
    # Expanded test cases to cover all priority levels
    test_cases = [
        {"input": "My dog is bleeding", "expected_priority": 5},
        {"input": "He ate a chocolate bar", "expected_priority": 5},
        {"input": "Time for a walk", "expected_priority": 3},
        {"input": "Mochi needs a bath", "expected_priority": 2},
        {"input": "Buy more poop bags", "expected_priority": 1}
    ]
    
    passed = 0
    print("=" * 50)
    print("🔍 PAWPAL+ AI RELIABILITY TEST SUITE")
    print("=" * 50)

    for case in test_cases:
        result = interpreter.parse_input(case["input"])
        # Check if the AI's priority matches our expectation
        if result["priority"] == case["expected_priority"]:
            passed += 1
            print(f"✅ Pass: '{case['input'][:20]}...' -> Priority {result['priority']}")
        else:
            print(f"❌ Fail: '{case['input']}' | Expected {case['expected_priority']}, got {result['priority']}")

    score = (passed / len(test_cases)) * 100
    print("-" * 50)
    print(f"TOTAL SCORE: {score}% | {passed}/{len(test_cases)} Passed")
    print("=" * 50)

if __name__ == "__main__":
    test_reliability()