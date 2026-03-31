import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Davčni Kalkulator 2026",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default chrome for cleaner look
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: 100%;
    }
    .stApp {
        background: #faf9f6;
    }
    @media (prefers-color-scheme: dark) {
        .stApp { background: #1c1c1e; }
    }
</style>
""", unsafe_allow_html=True)

html_content = """
<!DOCTYPE html>
<html lang="sl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --ivory:#faf9f6;--ink:#1a1a1a;--muted:#6b6b6b;--accent:#2563eb;--accent-soft:#eff4ff;
  --border:#e5e3dc;--card:#ffffff;--success:#166534;--success-bg:#f0fdf4;
  --warn:#92400e;--warn-bg:#fffbeb;--radius:16px;
  --font-serif:'DM Serif Display',serif;--font-sans:'DM Sans',sans-serif;
}
@media(prefers-color-scheme:dark){:root{
  --ivory:#1c1c1e;--ink:#f5f5f5;--muted:#999;--accent:#60a5fa;--accent-soft:#1e2a3a;
  --border:#3a3a3c;--card:#2c2c2e;--success:#86efac;--success-bg:#052e16;
  --warn:#fcd34d;--warn-bg:#292100;
}}
html,body{background:var(--ivory);color:var(--ink);font-family:var(--font-sans)}
.app{max-width:780px;margin:0 auto;padding:2rem 1.25rem}
.header{text-align:center;margin-bottom:2.25rem}
.header h1{font-family:var(--font-serif);font-size:2rem;font-weight:400;letter-spacing:-0.02em;line-height:1.2;margin-bottom:.45rem}
.header p{font-size:.88rem;color:var(--muted)}
.inputs-grid{display:grid;grid-template-columns:1fr 1fr;gap:.9rem;margin-bottom:1.25rem}
@media(max-width:520px){.inputs-grid{grid-template-columns:1fr}}
.card{background:var(--card);border:0.5px solid var(--border);border-radius:var(--radius);padding:1.15rem}
.card-title{font-size:.68rem;font-weight:500;text-transform:uppercase;letter-spacing:.1em;color:var(--muted);margin-bottom:.7rem}
label{display:block;font-size:.8rem;color:var(--muted);margin-bottom:.3rem}
input[type=number]{width:100%;padding:.58rem .82rem;border:0.5px solid var(--border);border-radius:8px;font-family:var(--font-sans);font-size:.93rem;color:var(--ink);background:var(--ivory);outline:none}
input[type=number]:focus{border-color:var(--accent)}
.toggle-row{display:flex;gap:.45rem;margin-bottom:.7rem}
.toggle-btn{flex:1;padding:.52rem .3rem;border:0.5px solid var(--border);border-radius:8px;font-size:.78rem;font-family:var(--font-sans);background:transparent;color:var(--muted);cursor:pointer;transition:all .15s}
.toggle-btn.active{background:var(--accent);color:#fff;border-color:var(--accent)}
.checkbox-row{display:flex;align-items:center;gap:.6rem;padding:.65rem .9rem;border:0.5px solid var(--border);border-radius:10px;cursor:pointer;background:var(--card);margin-bottom:1.25rem}
.checkbox-row input{width:17px;height:17px;accent-color:var(--accent);cursor:pointer;flex-shrink:0}
.checkbox-row span{font-size:.86rem;color:var(--ink);line-height:1.4}
.kpi-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:.65rem;margin-bottom:1.15rem}
@media(max-width:440px){.kpi-grid{grid-template-columns:1fr 1fr}}
.kpi{background:var(--card);border:0.5px solid var(--border);border-radius:var(--radius);padding:.95rem 1rem}
.kpi-label{font-size:.68rem;font-weight:500;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);margin-bottom:.35rem}
.kpi-value{font-family:var(--font-serif);font-size:1.45rem;font-weight:400;color:var(--ink);line-height:1}
.poracun-banner{border-radius:var(--radius);padding:.9rem 1.1rem;display:flex;justify-content:space-between;align-items:center;margin-bottom:1.2rem}
.poracun-banner.doplačilo{background:var(--warn-bg);border:0.5px solid #fbbf24}
.poracun-banner.vračilo{background:var(--success-bg);border:0.5px solid #86efac}
.poracun-label{font-size:.72rem;font-weight:500;text-transform:uppercase;letter-spacing:.08em}
.poracun-label.doplačilo{color:var(--warn)}
.poracun-label.vračilo{color:var(--success)}
.poracun-sub{font-size:.75rem;color:var(--muted);margin-top:.15rem}
.poracun-amount{font-family:var(--font-serif);font-size:1.4rem}
.poracun-amount.doplačilo{color:var(--warn)}
.poracun-amount.vračilo{color:var(--success)}
.divider{border:none;border-top:0.5px solid var(--border);margin:1.1rem 0}
.section-title{font-family:var(--font-serif);font-size:1.05rem;font-weight:400;color:var(--ink);margin-bottom:.75rem}
.razred-row{display:flex;align-items:center;gap:.65rem;padding:.55rem 0;border-bottom:0.5px solid var(--border)}
.razred-row:last-child{border-bottom:none}
.razred-name{font-size:.78rem;color:var(--muted);flex:1.3;white-space:nowrap}
.razred-bar-wrap{flex:2;height:5px;background:var(--border);border-radius:3px;overflow:hidden}
.razred-bar{height:100%;background:var(--accent);border-radius:3px;transition:width .4s}
.razred-amt{font-size:.82rem;font-weight:500;text-align:right;min-width:68px}
.detail-row{display:flex;justify-content:space-between;align-items:baseline;padding:.5rem 0;border-bottom:0.5px solid var(--border);font-size:.85rem}
.detail-row:last-child{border-bottom:none}
.detail-row.total{font-family:var(--font-serif);font-size:.95rem;padding-top:.7rem;margin-top:.2rem}
.detail-key{color:var(--muted);flex:1;padding-right:.4rem;line-height:1.4}
.detail-val{font-weight:500;text-align:right;white-space:nowrap}
.info-box{border-radius:10px;padding:.8rem .95rem;font-size:.82rem;line-height:1.55;margin-top:.65rem}
.info-box.blue{background:var(--accent-soft);color:var(--accent)}
.info-box.orange{background:var(--warn-bg);color:var(--warn)}
.info-box.green{background:var(--success-bg);color:var(--success)}
</style>
</head>
<body>
<div class="app">
  <div class="header">
    <h1>Davčni kalkulator 2026</h1>
    <p>Za upokojence &middot; Pokojnina + 2. steber &middot; Slovenija</p>
  </div>

  <div class="inputs-grid">
    <div class="card">
      <div class="card-title">Pokojnina (ZPIZ)</div>
      <label>Mesečna bruto pokojnina</label>
      <input type="number" id="pokojnina" value="1500" min="0" step="50" inputmode="decimal">
    </div>
    <div class="card">
      <div class="card-title">2. steber (PDPZ)</div>
      <div class="toggle-row">
        <button class="toggle-btn active" id="btn-renta" onclick="setTip('renta')">Mesečna renta</button>
        <button class="toggle-btn" id="btn-odkup" onclick="setTip('odkup')">Enkratni odkup</button>
      </div>
      <label id="renta-label">Mesečna bruto renta</label>
      <input type="number" id="renta" value="200" min="0" step="10" inputmode="decimal">
    </div>
  </div>

  <label class="checkbox-row" for="senior">
    <input type="checkbox" id="senior">
    <span>Uveljavljam seniorsko olajšavo (70+ let, 138,80 €/mes.)</span>
  </label>

  <div class="kpi-grid">
    <div class="kpi"><div class="kpi-label">Letni davčni dolg</div><div class="kpi-value" id="kpi-dolg">—</div></div>
    <div class="kpi"><div class="kpi-label">Plačane akontacije</div><div class="kpi-value" id="kpi-ak">—</div></div>
    <div class="kpi"><div class="kpi-label">Neto davčna osnova</div><div class="kpi-value" id="kpi-osnova">—</div></div>
  </div>

  <div id="poracun-banner" class="poracun-banner vračilo" style="display:none">
    <div>
      <div class="poracun-label vračilo" id="poracun-label">Vračilo</div>
      <div class="poracun-sub">Po letni odmeri FURS</div>
    </div>
    <div class="poracun-amount vračilo" id="poracun-amt">—</div>
  </div>

  <hr class="divider">
  <div class="section-title">Obdavčitev po progresivnih razredih</div>
  <div id="razredi-list"></div>

  <hr class="divider">
  <div class="section-title">Podroben letni razrez</div>
  <div id="detail-list"></div>

  <div id="info-boxes"></div>
  <div style="height:2rem"></div>
</div>

<script>
const S_OL=5551.93,SEN_OL=1665.60,OZP_MES=35.0,POK_OL=0.135;
const RAZREDI=[["1. razred (16%)",9721.43,.16],["2. razred (26%)",20177.30,.26],["3. razred (33%)",35560.00,.33],["4. razred (39%)",74160.00,.39],["5. razred (50%)",Infinity,.50]];
let tip='renta';
function setTip(t){tip=t;document.getElementById('btn-renta').classList.toggle('active',t==='renta');document.getElementById('btn-odkup').classList.toggle('active',t==='odkup');document.getElementById('renta-label').textContent=t==='renta'?'Mesečna bruto renta':'Celotni znesek odkupa';document.getElementById('renta').value=t==='renta'?200:20000;document.getElementById('renta').step=t==='renta'?10:500;recalc();}
function fmt(n){return n.toLocaleString('sl-SI',{minimumFractionDigits:2,maximumFractionDigits:2})+' €';}
function recalc(){
  const pok_m=parseFloat(document.getElementById('pokojnina').value)||0;
  const renta_raw=parseFloat(document.getElementById('renta').value)||0;
  const je_sen=document.getElementById('senior').checked;
  const renta_mes=tip==='renta'?renta_raw:0;
  const renta_letna=tip==='renta'?renta_raw*12:renta_raw;
  const pok_letna=pok_m*12;
  const m_do=pok_m*0.01,m_ozp=OZP_MES,m_ol=(S_OL/12)+(je_sen?SEN_OL/12:0);
  const m_osnova=Math.max(0,pok_m-m_do-m_ozp);
  const m_net=Math.max(0,m_osnova-m_ol);
  const m_ak_zpiz=Math.max(0,(m_net*0.16)-(pok_m*POK_OL));
  const ak_zpiz_letna=m_ak_zpiz*12;
  let m_ak_renta=0,ak_renta_letna=0;
  if(tip==='odkup'){ak_renta_letna=renta_letna*0.25;m_ak_renta=ak_renta_letna;}
  else{if(renta_mes>=160)m_ak_renta=(renta_mes*0.5)*0.25;ak_renta_letna=m_ak_renta*12;}
  const letni_do=(pok_letna+renta_letna)*0.01,letni_ozp=OZP_MES*12;
  const renta_v_osnovi=tip==='renta'?renta_letna*0.5:renta_letna;
  let letna_osnova=(pok_letna+renta_v_osnovi)-letni_do-letni_ozp-S_OL;
  if(je_sen)letna_osnova-=SEN_OL;
  letna_osnova=Math.max(0,letna_osnova);
  let odmerjena=0,ostanek=letna_osnova,prev=0;
  const razRez=[];
  for(const[ime,prag,stopnja]of RAZREDI){const v=Math.min(Math.max(0,ostanek),prag-prev);const d=v*stopnja;razRez.push([ime,v,d]);odmerjena+=d;ostanek-=v;prev=prag;if(ostanek<=0)break;}
  const pok_ol_letna=pok_letna*POK_OL;
  const koncni=Math.max(0,odmerjena-pok_ol_letna);
  const ak_skupaj=ak_zpiz_letna+ak_renta_letna;
  const poracun=koncni-ak_skupaj;
  document.getElementById('kpi-dolg').textContent=fmt(koncni);
  document.getElementById('kpi-ak').textContent=fmt(ak_skupaj);
  document.getElementById('kpi-osnova').textContent=fmt(letna_osnova);
  const banner=document.getElementById('poracun-banner');
  const lbl=document.getElementById('poracun-label');
  const amt=document.getElementById('poracun-amt');
  banner.style.display='flex';
  const isDoplac=poracun>0;
  banner.className='poracun-banner '+(isDoplac?'doplačilo':'vračilo');
  lbl.className='poracun-label '+(isDoplac?'doplačilo':'vračilo');
  amt.className='poracun-amount '+(isDoplac?'doplačilo':'vračilo');
  lbl.textContent=isDoplac?'Doplačilo':'Vračilo';
  amt.textContent=fmt(Math.abs(poracun));
  const maxD=Math.max(...razRez.map(r=>r[2]),1);
  document.getElementById('razredi-list').innerHTML=razRez.map(([ime,osnova,davek])=>`<div class="razred-row"><span class="razred-name">${ime}</span><div class="razred-bar-wrap"><div class="razred-bar" style="width:${Math.round(davek/maxD*100)}%"></div></div><span class="razred-amt">${fmt(davek)}</span></div>`).join('');
  const rows=[["Bruto pokojnina (ZPIZ)",fmt(pok_letna)],["Bruto znesek iz 2. stebra",fmt(renta_letna)],["Vstop v davčno osnovo (PDPZ)",fmt(renta_v_osnovi)],["Prispevek za dolgotrajno oskrbo (1%)","−"+fmt(letni_do)],["Zdravstveni prispevek (OZP)","−"+fmt(letni_ozp)],["Splošna olajšava","−"+fmt(S_OL)],...(je_sen?[["Seniorska olajšava","−"+fmt(SEN_OL)]]:[]),["Neto davčna osnova",fmt(letna_osnova),true],["Pokojninska olajšava (13,5%)","−"+fmt(pok_ol_letna)],["Odmerjeni davek pred olajšavo",fmt(odmerjena)],["Končni letni davčni dolg",fmt(koncni),true],["Akontacija ZPIZ (letno)","−"+fmt(ak_zpiz_letna)],["Akontacija PDPZ (letno)","−"+fmt(ak_renta_letna)]];
  document.getElementById('detail-list').innerHTML=rows.map(([k,v,bold])=>`<div class="detail-row${bold?' total':''}"><span class="detail-key">${k}</span><span class="detail-val">${v}</span></div>`).join('');
  let html='';
  const prag=je_sen?2019:1724;
  if(pok_m<prag)html+=`<div class="info-box blue">Vaša pokojnina je pod pragom — ZPIZ vam mesečno ne odteguje akontacije dohodnine.</div>`;
  else html+=`<div class="info-box orange">Pokojnina presega prag — ZPIZ mesečno odteguje ${fmt(m_ak_zpiz)} akontacije.</div>`;
  if(tip==='renta'&&renta_mes>=160)html+=`<div class="info-box orange" style="margin-top:.5rem">Renta presega 160 € — zavarovalnica mesečno odvede ${fmt(m_ak_renta)} akontacije.</div>`;
  if(!isDoplac)html+=`<div class="info-box green" style="margin-top:.5rem">FURS vam vrne ${fmt(Math.abs(poracun))}.</div>`;
  document.getElementById('info-boxes').innerHTML=html;
}
['pokojnina','renta','senior'].forEach(id=>{const el=document.getElementById(id);el.addEventListener(el.type==='checkbox'?'change':'input',recalc);});
recalc();
</script>
</body>
</html>
"""

components.html(html_content, height=1600, scrolling=True)
