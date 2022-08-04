import React, { useEffect, useState } from 'react'
import EachSupply from '../EachSupply'

function Supplies({ setProjectSupplies, project, projectSupplies }) {


    // console.log(projectSupplies)
    const [supply, setSupply] = useState("");
    const [projectId, setProjectId] = useState(projectSupplies[0].projectId)
    const [oldProjectSupplies, setOldProjectSupplies] = useState(projectSupplies)
    const [supplyErrors, setSupplyErrors] = useState([]);
    const [showSupplyErrors, setShowSupplyErrors] = useState(false);
    console.log(oldProjectSupplies)
    const [amount, setAmount] = useState(null);

    useEffect(() => {
        const inFuncErrors = []
        if (supply.length < 3) {
            inFuncErrors.push('Please provide a supply name')
        }
        setSupplyErrors(inFuncErrors)
    }, [supply, showSupplyErrors])

    const addSupply = (e) => {
        e.preventDefault();

        if (supplyErrors.length === 0) {

            const newwSupply = {
                supply,
                amount,
                projectId
            };
            setProjectSupplies([...projectSupplies, newwSupply])
            console.log(projectSupplies)
            setSupply("");
            setShowSupplyErrors(false)
        } else {
            setShowSupplyErrors(true)
        }

    }

    return (
        <>
            {projectSupplies?.map((supply, i) => (
                <EachSupply
                    setProjectSupplies={setProjectSupplies}
                    supply={supply}
                    index={i}
                    projectSupplies={projectSupplies}
                />
            ))}
            <div className="supply-input">
                <label>Supply</label>
                <input
                    placeholder="Add supplies needed for this project"
                    type='text'
                    name='supply'
                    value={supply}
                    // required
                    onChange={(e) => setSupply(e.target.value)}
                ></input>
                {showSupplyErrors &&
                    <>
                        <ul>
                            {supplyErrors.map(error => (
                                <li>{error}</li>
                            ))}
                        </ul>
                    </>
                }
            </div>
            <div className='add-supply-btn-div'>
                <button className="add-supply" onClick={addSupply}>Add Supply</button>
            </div>
        </>
    )
}

export default Supplies