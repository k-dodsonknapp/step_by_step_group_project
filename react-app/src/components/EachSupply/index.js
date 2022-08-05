import { useEffect, useState } from "react"

function EachSupply({ supply, index, projectSupplies, setProjectSupplies }) {
    // console.log(supply)
    // console.log(index)
    // console.log(setSupplies)
    const [editedSupply, setEditedSupply] = useState(supply.supply)
    // console.log()
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