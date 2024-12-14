// constants
const SET_USER = 'session/SET_USER';
const REMOVE_USER = 'session/REMOVE_USER';

const setUser = (user) => ({
  type: SET_USER,
  payload: user
});

const removeUser = () => ({
  type: REMOVE_USER,
})

const initialState = { user: null };

export const authenticate = () => async (dispatch) => {
  const response = await fetch(`${process.env.REACT_APP_API_URL}/api/auth/`, {
    headers: {
      'Content-Type': 'application/json'
    }
  });
  console.log(response)
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    };
    dispatch(setUser(data));
  };
};

// function getCSRFToken() {
//   const name = 'csrf_token=';
//   const decodedCookie = decodeURIComponent(document.cookie);
//   const ca = decodedCookie.split(';');
//   for (let i = 0; i < ca.length; i++) {
//       let c = ca[i];
//       while (c.charAt(0) === ' ') c = c.substring(1);
//       if (c.indexOf(name) === 0) return c.substring(name.length, c.length);
//   }
//   return "";
// }

export const login = (email, password) => async (dispatch) => {
  const response = await fetch(`${process.env.REACT_APP_API_URL}/api/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password }),
    credentials: 'include',
  });
  
  
  if (response.ok) {
    const data = await response.json();
    dispatch(setUser(data));
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    };
  } else {
    return ['An error occurred. Please try again.'];
  };
};

export const logout = () => async (dispatch) => {
  const response = await fetch('/api/auth/logout', {
    headers: {
      'Content-Type': 'application/json',
    }
  });

  if (response.ok) {
    dispatch(removeUser());
  };
};


export const signUp = (username, email, password, userPhoto) => async (dispatch) => {
  console.warn(username, email, password, userPhoto, "LLLLLLLLLL")
  const response = await fetch('/api/auth/signup', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username,
      email,
      password,
      userPhoto,
    }),
  });
  
  if (response.ok) {
    const data = await response.json();
    dispatch(setUser(data));
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    };
  } else {
    return ['An error occurred. Please try again.'];
  };
};

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case SET_USER:
      return { user: action.payload }
    case REMOVE_USER:
      return { user: null }
    default:
      return state;
  }
}
