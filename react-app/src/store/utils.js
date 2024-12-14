export async function fetchWithCsrf(url, options = {}) {
  const csrfToken = getCsrfToken();

  const headers = {
    "Content-Type": "application/json",
    "X-CSRFToken": csrfToken, // Include the CSRF token
    ...options.headers, // Merge with existing headers if any
  };

  const updatedOptions = {
    ...options,
    headers,
  };

  return fetch(url, updatedOptions);
}

export default {
  fetchWithCsrf,
};
