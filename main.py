print("=========================================")
print("   GOOGLE IT APPRENTICESHIP DIAGNOSTICS   ")
print("=========================================")
print("1. Network & Connectivity Issues")
print("2. Operating System / Software Errors")
print("3. Hardware & Power Diagnostic Failures")
print("\n")

choice = input("Select an IT ticket category to diagnose (1-3): ")

if choice == "1":
    print("\n[Diagnosing Network Connectivity...]")
    ping_status = input("Is the router ping status successful? (yes/no): ").lower()
    if ping_status == "no":
        print("--> Recommendation: Flush the local DNS cache, reset IP configurations, or check physical ethernet connections.")
    else:
        print("--> Recommendation: Check proxy settings and local firewall rules blocking ports 80 or 443.")

elif choice == "2":
    print("\n[Diagnosing Operating System Error...]")
    boot_issue = input("Does the system fail to boot into the desktop environment? (yes/no): ").lower()
    if boot_issue == "yes":
        print("--> Recommendation: Boot the device into Safe Mode, run a system file check (SFC), and verify OS image integrity.")
    else:
        print("--> Recommendation: Clear local application caches and check for pending Google system patches.")

elif choice == "3":
    print("\n[Diagnosing Hardware Failures...]")
    power_light = input("Is the system receiving power (Are the indicator lights on)? (yes/no): ").lower()
    if power_light == "no":
        print("--> Recommendation: Inspect the Power Supply Unit (PSU) voltage switches and verify connection to a functional outlet.")
    else:
        print("--> Recommendation: Disconnect peripheral hardware components and run an internal RAM diagnostic check.")

else:
    print("\n--> Invalid selection. Escalating this ticket to Tier-2 Corporate Support engineers.")
