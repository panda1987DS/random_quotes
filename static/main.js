function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const csrftoken = getCookie('csrftoken');

document.querySelectorAll('button.like').forEach(button => {
  button.addEventListener('click', function() {
    const id = this.dataset.id;
    fetch(`/like/${id}/`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrftoken,
        'Content-Type': 'application/json',
      },
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById(`likes-count-${id}`).textContent = data.likes;
    })
    .catch(err => console.error(err));
  });
});

document.querySelectorAll('button.dislike').forEach(button => {
  button.addEventListener('click', function() {
    const id = this.dataset.id;
    fetch(`/dislike/${id}/`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrftoken,
        'Content-Type': 'application/json',
      },
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById(`dislikes-count-${id}`).textContent = data.dislikes;
    })
    .catch(err => console.error(err));
  });
});
document.getElementById('refresh-btn').addEventListener('click', () => {
    location.reload();
  });