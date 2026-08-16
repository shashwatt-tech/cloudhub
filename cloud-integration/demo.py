from appetize_client import AppetizeClient
import time


def main():
    """Demo script to test all Appetize functionality"""
    
    print("\n" + "="*60)
    print("🚀 CloudHub - Appetize Integration Demo")
    print("="*60 + "\n")
    
    # Initialize client
    client = AppetizeClient()
    
    # Step 1: Test connection
    print("\n📡 STEP 1: Testing Connection")
    print("-" * 40)
    if not client.test_connection():
        print("❌ Cannot proceed without connection")
        return
    
    # Step 2: List apps
    print("\n📋 STEP 2: Listing Apps")
    print("-" * 40)
    apps = client.list_apps()
    
    if not apps:
        print("\n⚠️  No apps found. Please upload an APK first.")
        print("   You can upload via Appetize.io dashboard")
        return
    
    # Step 3: Create session with first app
    print("\n🎮 STEP 3: Creating Session")
    print("-" * 40)
    public_key = apps[0]['publicKey']
    session = client.create_session(public_key)
    session_id = session['sessionId']
    
    # Step 4: Get session info
    print("\nℹ️  STEP 4: Getting Session Info")
    print("-" * 40)
    info = client.get_session_info(session_id)
    print(f"Status: {info.get('status', 'active')}")
    
    # Step 5: Wait
    print("\n⏳ STEP 5: Session Running")
    print("-" * 40)
    print("Waiting 15 seconds... (session is active)")
    time.sleep(15)
    
    # Step 6: Stop session
    print("\n🛑 STEP 6: Stopping Session")
    print("-" * 40)
    client.stop_session(session_id)
    
    # Done
    print("\n" + "="*60)
    print("✅ Demo Completed Successfully!")
    print("="*60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Demo interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Demo failed: {e}")