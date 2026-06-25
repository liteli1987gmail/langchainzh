
const input = document.getElementById('search');
const results = document.getElementById('results');
let index = [];
fetch('/search-index.json').then((response) => response.json()).then((data) => {
  index = data;
});
input?.addEventListener('input', () => {
  const query = input.value.trim().toLowerCase();
  if (!query) {
    results.hidden = true;
    results.innerHTML = '';
    return;
  }
  const hits = index.filter((item) =>
    item.title.toLowerCase().includes(query) ||
    item.text.toLowerCase().includes(query)
  ).slice(0, 12);
  results.hidden = false;
  results.innerHTML = '<h2>搜索结果</h2>' + hits.map((item) => `
    <a class="result" href="${item.url}">
      <strong>${item.title}</strong><br>
      <small>${item.url}</small>
    </a>
  `).join('');
});
