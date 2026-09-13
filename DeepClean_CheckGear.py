import streamlit as st

def repair_station():
    st.subheader("Repair Station")
    gear = st.session_state.gear

    for item in gear.gear_inventory():
        status = gear.gear_status[item]
        color = "red" if status == "Broken" else "green"

        col1, col2 = st.columns([3, 1])
        col1.write(f"{item}: :{color}[{status}]")

        if status == "Broken":
            if col2.button("Repair", key=f"repair_{item}"):
                msg = gear.repair_gear(item)
                st.success(msg)
                st.rerun()
        else:
            col2.write("✅")


def gear_shop():
    st.subheader("Gear Shop")
    gear = st.session_state.gear

    available_to_buy = ["Extra Oxygen Tank", "Spare Flippers", "Backup Mask"]

    for item_name in available_to_buy:
        already_owned = item_name in gear.gear_inventory()

        col1, col2 = st.columns([3, 1])
        col1.write(item_name)

        if already_owned:
            col2.write("Owned")
        else:
            if col2.button("Buy", key=f"buy_{item_name}"):
                msg = gear.buy_gear(item_name)
                st.success(msg)
                st.rerun()