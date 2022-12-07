import { useEffect, useState } from "react"

function EachSupply({ supply, index, projectSupplies, setProjectSupplies }) {

    const [editedSupply, setEditedSupply] = useState(supply.supply)
    projectSupplies[index].supply = editedSupply
    setProjectSupplies(projectSupplies)
    // supplies[index].supply = editedSupply
    // setSupplies(supply.supply = editedSupply)

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