import { useState } from "react"

function EachSupply({ supply, index, supplies, setSupplies }) {
    const [editedSupply, setEditedSupply] = useState(supplies[index].supply)

    supplies[index].supply = editedSupply
    setSupplies(editedSupply)

    return (
        <div>
            <input
                key={supply.id}
                type="text"
                name="supply"
                value={editedSupply}
                onChange={e => setEditedSupply(e.target.value)}
            />
        </div>
    )
}

export default EachSupply;