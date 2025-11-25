from service.db import menu_col, guests_col, convos_col
from service.llm_adapter import get_llm
from datetime import datetime

llm = get_llm()

async def process_message(guest_id: str, text: str):
    text_lower = text.lower()

    guest = await guests_col.find_one({"guest_id": guest_id})
    if not guest:
        guest = {"guest_id": guest_id, "preferences": []}
        await guests_col.insert_one(guest)

    convo = await convos_col.find_one({"guest_id": guest_id})
    if not convo:
        convo = {"guest_id": guest_id, "messages": []}
        await convos_col.insert_one(convo)

    convo["messages"].append({
        "role": "user",
        "content": text,
        "timestamp": datetime.utcnow().isoformat()
    })
    await convos_col.update_one(
        {"guest_id": guest_id},
        {"$set": {"messages": convo["messages"]}}
    )

    matches = []
    async for item in menu_col.find({}):
        if item["name"].split()[0].lower() in text_lower:
            matches.append(item)

    if not matches or "or" in text_lower:
        response = await llm.ask([{"role": "user", "content": text}])

        convo["messages"].append({
            "role": "assistant",
            "content": response
        })
        await convos_col.update_one(
            {"guest_id": guest_id},
            {"$set": {"messages": convo["messages"]}}
        )

        return {"assistant": response}

    selected_item = matches[0]
    confirmation = f"Order confirmed: {selected_item['name']}. ETA {selected_item.get('prep_time', 20)} minutes."

    convo["messages"].append({
        "role": "assistant",
        "content": confirmation
    })
    await convos_col.update_one(
        {"guest_id": guest_id},
        {"$set": {"messages": convo["messages"]}}
    )

    return {"assistant": confirmation}
