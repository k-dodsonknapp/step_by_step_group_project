const EDIT_INSTRUCTIONS = "/instructions/:projectId/update";

const updateInstructions = (instructions) => ({
    type: EDIT_INSTRUCTIONS,
    instructions
});

export const editInstructions = (projectId) => async (dispatch) => {
    const res = await fetch(`${process.env.REACT_APP_API_URL}/api/instructions/${projectId}/update`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
    });

    if (res.ok) {
        const instruction = await res.json();
        dispatch(updateInstructions(projectId))
    };
};