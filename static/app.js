const branchCode = new URLSearchParams(window.location.search).get('branch') || '';

document.getElementById('branch').textContent = branchCode
  ? `Branch view: ${branchCode}`
  : 'Province-wide view';

async function loadServices() {
  const res = await fetch(`/api/v1/services?branch_code=${branchCode}`);
  const data = await res.json();
  const tbody = document.getElementById('services');
  tbody.innerHTML = data.map(s => `<tr><td>${s.name}</td><td>${s.description}</td></tr>`).join('');
}

async function loadAnnouncements() {
  const res = await fetch(`/api/v1/announcements?branch_code=${branchCode}`);
  const data = await res.json();
  const tbody = document.getElementById('announcements');
  tbody.innerHTML = data.map(a => `<tr><td>${a.title}</td><td>${a.body}</td></tr>`).join('');
}

loadServices();
loadAnnouncements();
