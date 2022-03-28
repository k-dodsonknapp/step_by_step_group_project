import { useState } from "react"

function EachSupply({ supply, index, supplies, setSupplies }) {
    const [editedSupply, setEditedSupply] = useState(supplies[index].supply)
    // console.log("BBBBBBBBBBBBB" , editedSupply)

    supplies[index].supply = editedSupply
    setSupplies(editedSupply)
    // console.log("CCCCCCCCCCCCC" , supply)
    // console.log("JJJJJJJJJ" ,supplies)
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