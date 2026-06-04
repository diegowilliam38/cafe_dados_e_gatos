/* ============================================================
   Achadinhos da Shopee — Carregamento via JSON
   - Lê data/achadinhos.json
   - Renderiza pílulas de categoria e cards por seção
   - Não exibe metadados técnicos, score, ranking, etc.
   ============================================================ */

const DATA_URL = "data/achadinhos.json";

// Subtítulos delicados por categoria (linguagem editorial)
const SUBTITULOS = {
  "moda": "Toques de estilo para todos os momentos",
  "beleza": "Pequenos gestos que cuidam de você",
  "acessórios para celular": "Detalhes que protegem com charme",
  "casa": "Conforto e beleza para o seu lar",
  "cozinha": "Aconchego em cada receita",
  "organização": "Harmonia para o seu dia a dia",
  "pets": "Carinho para quem te ama de verdade",
  "papelaria": "Inspiração em cada anotação",
  "infantil": "Delícias para os pequenos",
  "fitness": "Bem-estar com leveza",
};

// Ordem de exibição das categorias
const ORDEM_CATEGORIAS = [
  "moda", "beleza", "acessórios para celular", "casa", "cozinha",
  "organização", "pets", "papelaria", "infantil", "fitness",
];

// Formatação monetária
const fmtBRL = (v) => {
  const n = Number(v);
  if (!isFinite(n) || n <= 0) return null;
  return n.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
};

function categoriaTitulo(cat) {
  const map = {
    "moda": "Moda",
    "beleza": "Beleza",
    "acessórios para celular": "Acessórios para Celular",
    "casa": "Casa",
    "cozinha": "Cozinha",
    "organização": "Organização",
    "pets": "Pets",
    "papelaria": "Papelaria",
    "infantil": "Infantil",
    "fitness": "Fitness",
  };
  return map[cat] || cat.charAt(0).toUpperCase() + cat.slice(1);
}

function renderPill(cat) {
  return `<button class="category-pill" data-cat="${cat}">${categoriaTitulo(cat)}</button>`;
}

function renderPills(categorias) {
  const nav = document.getElementById("category-nav");
  nav.innerHTML = `<button class="category-pill active" data-cat="all">Tudo</button>` +
    categorias.map(renderPill).join("");
}

function renderCard(p) {
  const sale = fmtBRL(p.sale_price);
  const price = fmtBRL(p.price);
  const showOriginal = price && sale && Number(p.price) > Number(p.sale_price);
  const discount = (p.discount_percentage !== null && p.discount_percentage !== undefined && p.discount_percentage !== "")
    ? Number(p.discount_percentage) : null;
  const rating = (p.item_rating !== null && p.item_rating !== undefined && p.item_rating !== "")
    ? Number(p.item_rating) : null;
  const img = p.image_link || "assets/placeholder.svg";
  // Prioridade: link_gerado_shopee (afiliada) > product_link (original)
  const afiliado = (p.link_gerado_shopee || "").toString().trim();
  const link = (afiliado && afiliado !== "") ? afiliado : (p.product_link || "#");
  const porte = p.porte_estimado && p.porte_estimado !== "indefinido" ? p.porte_estimado : null;

  return `
    <article class="product-card">
      <div class="product-image-wrap">
        <img class="product-image" src="${img}" alt="${(p.title_clean || '').replace(/"/g, '&quot;')}" loading="lazy" onerror="this.src='assets/placeholder.svg'" />
        <span class="product-badge">${categoriaTitulo(p.categoria_final)}</span>
        ${discount && discount > 0 ? `<span class="product-discount">-${Math.round(discount)}%</span>` : ""}
      </div>
      <div class="product-body">
        <h3 class="product-title">${p.title_clean || "Achadinho"}</h3>
        <div class="product-meta">
          ${rating ? `<span class="product-rating" title="Avaliação"><span class="product-rating-star">★</span> ${rating.toFixed(1)}</span>` : ""}
          ${porte ? `<span class="product-porte">${porte}</span>` : ""}
        </div>
        <div class="product-price">
          ${sale ? `<span class="price-current">${sale}</span>` : ""}
          ${showOriginal ? `<span class="price-original">${price}</span>` : ""}
        </div>
        <a class="product-button" href="${link}" target="_blank" rel="noopener noreferrer">Ver achadinho ✿</a>
      </div>
    </article>
  `;
}

function renderSection(cat, items) {
  return `
    <section class="category-section" id="cat-${cat}">
      <div class="category-header">
        <h2 class="category-title">${categoriaTitulo(cat)}</h2>
        <p class="category-subtitle">${SUBTITULOS[cat] || ""}</p>
      </div>
      <div class="products-grid">
        ${items.map(renderCard).join("")}
      </div>
    </section>
  `;
}

function renderTudo(produtos) {
  const main = document.getElementById("catalogo");
  const grupos = {};
  for (const p of produtos) {
    if (!grupos[p.categoria_final]) grupos[p.categoria_final] = [];
    grupos[p.categoria_final].push(p);
  }
  const ordem = ORDEM_CATEGORIAS.filter(c => grupos[c]);
  main.innerHTML = ordem.map(cat => renderSection(cat, grupos[cat])).join("");
}

function ativarPill(cat) {
  document.querySelectorAll(".category-pill").forEach(b => {
    b.classList.toggle("active", b.dataset.cat === cat);
  });
  if (cat === "all") {
    document.querySelectorAll(".category-section").forEach(s => s.style.display = "");
    window.scrollTo({ top: 0, behavior: "smooth" });
  } else {
    document.querySelectorAll(".category-section").forEach(s => {
      s.style.display = (s.id === `cat-${cat}`) ? "" : "none";
    });
    const target = document.getElementById(`cat-${cat}`);
    if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
  }
}

async function init() {
  const main = document.getElementById("catalogo");
  main.innerHTML = `<p class="loading">Carregando achadinhos…</p>`;
  try {
    const resp = await fetch(DATA_URL, { cache: "no-store" });
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const produtos = await resp.json();
    if (!Array.isArray(produtos) || produtos.length === 0) {
      main.innerHTML = `<p class="empty">Em breve novos achadinhos.</p>`;
      return;
    }
    const categorias = [...new Set(produtos.map(p => p.categoria_final))];
    renderPills(categorias);
    renderTudo(produtos);
    document.getElementById("category-nav").addEventListener("click", (ev) => {
      const btn = ev.target.closest(".category-pill");
      if (!btn) return;
      ativarPill(btn.dataset.cat);
    });
  } catch (e) {
    console.error(e);
    main.innerHTML = `<p class="empty">Não foi possível carregar os achadinhos agora. Tente novamente mais tarde.</p>`;
  }
}

document.addEventListener("DOMContentLoaded", init);
