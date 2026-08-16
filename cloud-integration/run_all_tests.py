import subprocess


def run_command(cmd, description):
    print("\n" + "=" * 70)
    print(f"🧪 {description}")
    print("=" * 70)

    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True
        )

        print(result.stdout)

        if result.returncode == 0:
            print(f"✅ {description} - PASSED")
            return True
        else:
            print(f"❌ {description} - FAILED")
            print(result.stderr)
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    print("\n" + "=" * 70)
    print("🚀 CLOUDHUB - COMPLETE TEST SUITE")
    print("=" * 70)

    results = []

    results.append(
        run_command(
            "python appetize_client.py",
            "Basic Client Test"
        )
    )

    results.append(
        run_command(
            "python demo.py",
            "Full Demo Test"
        )
    )

    results.append(
        run_command(
            "python -m pytest tests/ -v",
            "Unit Tests"
        )
    )

    results.append(
        run_command(
            "python manual_test.py",
            "Manual Integration Test"
        )
    )

    print("\n" + "=" * 70)
    print("📊 TEST SUMMARY")
    print("=" * 70)

    passed = sum(results)
    total = len(results)

    print(f"\n✅ Passed: {passed}/{total}")
    print(f"❌ Failed: {total - passed}/{total}")

    if passed == total:
        print("\n🎉 ALL TESTS PASSED! 🎉")
    else:
        print("\n⚠️ Some tests failed. Please review above.")

    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()