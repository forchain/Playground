const REPOSITORY = "https://github.com/forchain/Playground/blob/main/";
const state = { questions: [], query: "", domain: "all", difficulty: "all", topic: "all", selectedId: "" };
const elements = {
  search: document.querySelector("#search"), difficulty: document.querySelector("#difficulty"), topic: document.querySelector("#topic"),
  list: document.querySelector("#question-list"), reader: document.querySelector("#reader"), visible: document.querySelector("#visible-count"),
  total: document.querySelector("#total-count"), context: document.querySelector("#active-context"), nav: document.querySelector("#library-nav"),
  menu: document.querySelector("#menu-button"), scrim: document.querySelector("#nav-scrim"),
};

const escapeHtml = (value) => value.replace(/[&<>"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[char]));
const inline = (text) => escapeHtml(text).replace(/`([^`]+)`/g, "<code>$1</code>").replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>").replace(/\*([^*]+)\*/g, "<em>$1</em>");

function markdown(markdownText) {
  const lines = markdownText.trim().split("\n"); let html = "", inCode = false, code = [], inList = false, listTag = "";
  const closeList = () => { if (inList) { html += `</${listTag}>`; inList = false; } };
  const closeCode = () => { if (inCode) { html += `<pre><code>${escapeHtml(code.join("\n"))}</code></pre>`; inCode = false; code = []; } };
  for (let index = 0; index < lines.length; index += 1) {
    const line = lines[index];
    if (line.startsWith("```")) { if (inCode) closeCode(); else { closeList(); inCode = true; } continue; }
    if (inCode) { code.push(line); continue; }
    if (/^\|.*\|$/.test(line) && /^\|?\s*:?-+/.test(lines[index + 1] || "")) {
      closeList(); const headers = line.split("|").slice(1, -1); const rows = []; index += 2;
      while (index < lines.length && /^\|.*\|$/.test(lines[index])) { rows.push(lines[index].split("|").slice(1, -1)); index += 1; } index -= 1;
      html += `<table><thead><tr>${headers.map((cell) => `<th>${inline(cell.trim())}</th>`).join("")}</tr></thead><tbody>${rows.map((row) => `<tr>${row.map((cell) => `<td>${inline(cell.trim())}</td>`).join("")}</tr>`).join("")}</tbody></table>`; continue;
    }
    const heading = line.match(/^(#{1,4})\s+(.+)$/); if (heading) { closeList(); const level = Math.min(heading[1].length + 1, 4); html += `<h${level}>${inline(heading[2])}</h${level}>`; continue; }
    const bullet = line.match(/^[-*]\s+(.+)$/); const ordered = line.match(/^\d+\.\s+(.+)$/);
    if (bullet || ordered) { const tag = ordered ? "ol" : "ul"; if (!inList || listTag !== tag) { closeList(); html += `<${tag}>`; inList = true; listTag = tag; } html += `<li>${inline((bullet || ordered)[1])}</li>`; continue; }
    closeList(); if (!line.trim()) continue; if (/^---+$/.test(line.trim())) { html += "<hr>"; continue; }
    if (line.startsWith("> ")) { html += `<blockquote>${inline(line.slice(2))}</blockquote>`; continue; }
    html += `<p>${inline(line)}</p>`;
  }
  closeList(); closeCode(); return html;
}

function visibleQuestions() {
  const query = state.query.trim().toLowerCase();
  return state.questions.filter((question) => {
    const matchesQuery = !query || [question.title, question.domain, ...question.topics, question.promptMarkdown].join(" ").toLowerCase().includes(query);
    return matchesQuery && (state.domain === "all" || question.domain === state.domain) && (state.difficulty === "all" || question.difficulty === state.difficulty) && (state.topic === "all" || question.topics.includes(state.topic));
  });
}

function populateFilters() {
  const values = (selector, items) => { selector.insertAdjacentHTML("beforeend", items.map((item) => `<option value="${escapeHtml(item)}">${escapeHtml(item)}</option>`).join("")); };
  values(elements.difficulty, [...new Set(state.questions.map((question) => question.difficulty))].filter((item) => item !== "未标注"));
  values(elements.topic, [...new Set(state.questions.flatMap((question) => question.topics))].sort((a, b) => a.localeCompare(b, "zh-CN")));
}

function updateLocation() { history.replaceState(null, "", `${location.pathname}${location.search}#${state.selectedId}`); }
function selectQuestion(id, shouldFocus = false) { state.selectedId = id; updateLocation(); render(); if (shouldFocus) elements.reader.focus(); }

function renderList(questions) {
  elements.visible.textContent = `${questions.length} 道题`;
  elements.context.textContent = state.domain === "all" ? "全部题目" : state.domain === "sql" ? "SQL" : "编程";
  elements.list.innerHTML = questions.map((question) => `<button class="question-item ${question.id === state.selectedId ? "is-active" : ""}" type="button" data-id="${question.id}"><span class="question-number">${String(question.number).padStart(2, "0")}</span><span><span class="question-title">${escapeHtml(question.title)}</span><span class="question-detail"><span>${question.domain === "sql" ? "SQL" : "编程"}</span><span>${escapeHtml(question.topics[0])}</span></span></span></button>`).join("");
  elements.list.querySelectorAll("[data-id]").forEach((button) => button.addEventListener("click", () => { closeNavigation(); selectQuestion(button.dataset.id, true); }));
}

function renderReader(question) {
  if (!question) { elements.reader.innerHTML = document.querySelector("#empty-template").innerHTML; elements.reader.querySelector("[data-reset]").addEventListener("click", reset); return; }
  const labels = [question.domain === "sql" ? "SQL" : "编程", question.difficulty, question.duration, ...question.topics].filter(Boolean);
  const links = Object.entries(question.paths).filter(([, path]) => path).map(([key, path]) => `<a href="${REPOSITORY}${path}" target="_blank" rel="noreferrer">${key === "readme" ? "查看原题" : key === "solution" ? "查看源答案" : "查看测试"}</a>`).join("");
  elements.reader.innerHTML = `<header class="reader-header"><p class="eyebrow">${question.domain === "sql" ? "SQL 笔试题" : "编程笔试题"} · ${String(question.number).padStart(2, "0")}</p><h1>${escapeHtml(question.title)}</h1><div class="metadata">${labels.map((label, index) => `<span class="badge ${index === 1 ? "difficulty" : ""}">${escapeHtml(label)}</span>`).join("")}</div></header><section class="reader-section"><h2>题目</h2>${markdown(question.promptMarkdown)}</section><section class="reader-section"><h2>解析</h2>${markdown(question.explanationMarkdown || "本题暂无独立解析，请结合参考答案与测试用例理解。")}</section><section class="reader-section"><div class="answer-heading"><h2>参考答案</h2><button class="copy-button" type="button" data-copy>复制代码</button></div><pre><code>${escapeHtml(question.answer)}</code></pre></section>${question.notesMarkdown ? `<section class="reader-section"><h2>补充说明</h2>${markdown(question.notesMarkdown)}</section>` : ""}<footer class="source-links">${links}</footer>`;
  elements.reader.querySelector("[data-copy]").addEventListener("click", async (event) => { await navigator.clipboard.writeText(question.answer); event.currentTarget.textContent = "已复制"; setTimeout(() => { event.currentTarget.textContent = "复制代码"; }, 1600); });
}

function render() { const questions = visibleQuestions(); if (!questions.some((question) => question.id === state.selectedId)) state.selectedId = questions[0]?.id || ""; renderList(questions); renderReader(questions.find((question) => question.id === state.selectedId)); }
function reset() { state.query = ""; state.domain = "all"; state.difficulty = "all"; state.topic = "all"; elements.search.value = ""; elements.difficulty.value = "all"; elements.topic.value = "all"; document.querySelectorAll(".segment").forEach((button) => button.classList.toggle("is-active", button.dataset.domain === "all")); render(); }
function closeNavigation() { elements.nav.classList.remove("is-open"); elements.scrim.classList.remove("is-open"); elements.menu.setAttribute("aria-expanded", "false"); }

document.querySelectorAll(".segment").forEach((button) => button.addEventListener("click", () => { state.domain = button.dataset.domain; document.querySelectorAll(".segment").forEach((item) => item.classList.toggle("is-active", item === button)); render(); }));
elements.search.addEventListener("input", () => { state.query = elements.search.value; render(); });
elements.difficulty.addEventListener("change", () => { state.difficulty = elements.difficulty.value; render(); });
elements.topic.addEventListener("change", () => { state.topic = elements.topic.value; render(); });
document.querySelector("#reset-button").addEventListener("click", reset);
elements.menu.addEventListener("click", () => { const open = elements.nav.classList.toggle("is-open"); elements.scrim.classList.toggle("is-open", open); elements.menu.setAttribute("aria-expanded", String(open)); });
elements.scrim.addEventListener("click", closeNavigation);
window.addEventListener("hashchange", () => { const id = location.hash.slice(1); if (state.questions.some((question) => question.id === id)) { state.selectedId = id; render(); } });

fetch("data/questions.json").then((response) => { if (!response.ok) throw new Error("题库数据无法加载"); return response.json(); }).then((payload) => { state.questions = payload.questions; state.selectedId = location.hash.slice(1); elements.total.textContent = `${state.questions.length} 道题`; populateFilters(); render(); }).catch((error) => { elements.reader.innerHTML = `<section class="empty-state"><p class="eyebrow">加载失败</p><h1>${escapeHtml(error.message)}</h1><p>请先运行题库数据生成命令后再启动静态服务器。</p></section>`; });
