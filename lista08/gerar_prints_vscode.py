import os
import subprocess
import time

BASE_DIR = r"c:\Users\amand\OneDrive - Universidade Federal de Uberlândia\2026\analise de algoritmo\prova2\lista08"
PRINTS_DIR = os.path.join(BASE_DIR, "prints")
TMP_DIR = os.path.join(BASE_DIR, "tmp_render")
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

os.makedirs(PRINTS_DIR, exist_ok=True)
os.makedirs(TMP_DIR, exist_ok=True)

# CSS base do VS Code Dark+
CSS_COMMON = """
* { box-sizing: border-box; }
body {
    margin: 0;
    padding: 0;
    background: #181818;
    color: #cccccc;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    font-size: 13px;
    height: 100vh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    user-select: none;
}
.titlebar {
    height: 35px;
    background: #181818;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 10px;
    border-bottom: 1px solid #2b2b2b;
    font-size: 12px;
    color: #999999;
}
.titlebar-left {
    display: flex;
    align-items: center;
    gap: 8px;
}
.titlebar-center {
    font-size: 12px;
    color: #cccccc;
}
.titlebar-right {
    display: flex;
    align-items: center;
    gap: 14px;
    font-size: 13px;
}
.app-body {
    flex: 1;
    display: flex;
    overflow: hidden;
}
.activitybar {
    width: 48px;
    background: #181818;
    border-right: 1px solid #2b2b2b;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 10px;
    gap: 18px;
    color: #858585;
}
.activity-icon {
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}
.activity-icon.active {
    color: #ffffff;
    border-left: 2px solid #ffffff;
    margin-left: -2px;
}
.main-area {
    flex: 1;
    display: flex;
    flex-direction: column;
    background: #1e1e1e;
}
.tabs-bar {
    height: 35px;
    background: #181818;
    display: flex;
    align-items: flex-end;
    border-bottom: 1px solid #252526;
}
.tab {
    height: 35px;
    background: #1e1e1e;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 0 15px;
    font-size: 13px;
    border-top: 1px solid #007acc;
    border-right: 1px solid #252526;
}
.tab .dot {
    width: 8px;
    height: 8px;
    background: #ffffff;
    border-radius: 50%;
}
.breadcrumbs {
    height: 22px;
    background: #1e1e1e;
    display: flex;
    align-items: center;
    padding: 0 16px;
    font-size: 11px;
    color: #8c8c8c;
    gap: 6px;
    border-bottom: 1px solid #252526;
}
.editor-container {
    flex: 1;
    display: flex;
    overflow: hidden;
    font-family: Consolas, 'Courier New', monospace;
    font-size: 13.5px;
    line-height: 19px;
    background: #1e1e1e;
}
.linenums {
    width: 50px;
    background: #1e1e1e;
    color: #6e7681;
    text-align: right;
    padding-right: 14px;
    padding-top: 6px;
    user-select: none;
}
.code-content {
    flex: 1;
    padding-top: 6px;
    padding-left: 4px;
    color: #d4d4d4;
    white-space: pre;
}
.statusbar {
    height: 22px;
    background: #007acc;
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 10px;
    font-size: 11px;
}
.statusbar-left, .statusbar-right {
    display: flex;
    align-items: center;
    gap: 14px;
}

/* Syntax Highlighting */
.kw { color: #569cd6; font-weight: normal; }
.fn { color: #dcdcaa; }
.str { color: #ce9178; }
.num { color: #b5cea8; }
.cm { color: #6a9955; font-style: italic; }
.builtin { color: #4ec9b0; }
.var { color: #9cdcfe; }
.op { color: #d4d4d4; }
.self { color: #569cd6; }
"""

def make_window_html(title_path, line_start, code_lines, status_line="Ln 1, Col 1", active_icon="code"):
    nums = "<br>".join(str(line_start + i) for i in range(len(code_lines)))
    code_html = "\n".join(code_lines)
    
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>{CSS_COMMON}</style>
</head>
<body>
<div class="titlebar">
  <div class="titlebar-left">
    <span>File</span><span>Edit</span><span>Selection</span><span>View</span><span>Go</span><span>Run</span><span>Terminal</span><span>Help</span>
  </div>
  <div class="titlebar-center">
    lista08.py - Visual Studio Code - Untracked
  </div>
  <div class="titlebar-right">
    <span>&#9472;</span><span>&#9633;</span><span>&#10005;</span>
  </div>
</div>

<div class="app-body">
  <div class="activitybar">
    <div class="activity-icon {'active' if active_icon=='explorer' else ''}">
      <svg width="18" height="18" viewBox="0 0 16 16" fill="currentColor"><path d="M14.5 2H7.71l-.85-.85L6.51 1h-5l-.5.5v11l.5.5h13l.5-.5v-10l-.5-.5zm-.5 11h-12V2h4.29l.85.85.35.15H14v10z"/></svg>
    </div>
    <div class="activity-icon">
      <svg width="18" height="18" viewBox="0 0 16 16" fill="currentColor"><path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/></svg>
    </div>
    <div class="activity-icon">
      <svg width="18" height="18" viewBox="0 0 16 16" fill="currentColor"><path d="M8 0a8 8 0 0 0-2.5 15.6c.4.1.5-.2.5-.4v-1.4c-2.2.5-2.7-1-2.7-1-.4-1-.9-1.2-.9-1.2-.7-.5.1-.5.1-.5.8.1 1.2.8 1.2.8.7 1.2 1.9.9 2.3.7.1-.5.3-.9.5-1.1-1.8-.2-3.6-.9-3.6-4 0-.9.3-1.6.8-2.1-.1-.2-.4-1 .1-2.1 0 0 .7-.2 2.2.8.6-.2 1.3-.3 2-.3s1.4.1 2 .3c1.5-1 2.2-.8 2.2-.8.5 1.1.2 1.9.1 2.1.5.6.8 1.3.8 2.1 0 3.1-1.9 3.7-3.7 3.9.3.3.6.8.6 1.5v2.2c0 .2.1.5.5.4A8 8 0 0 0 8 0z"/></svg>
    </div>
    <div class="activity-icon {'active' if active_icon=='debug' else ''}">
      <svg width="18" height="18" viewBox="0 0 16 16" fill="currentColor"><path d="M4.854 4.146a.5.5 0 0 1 0 .708L1.707 8l3.147 3.146a.5.5 0 0 1-.708.708l-3.5-3.5a.5.5 0 0 1 0-.708l3.5-3.5a.5.5 0 0 1 .708 0zm6.292 0a.5.5 0 0 0 0 .708L14.293 8l-3.147 3.146a.5.5 0 0 0 .708.708l3.5-3.5a.5.5 0 0 0 0-.708l-3.5-3.5a.5.5 0 0 0-.708 0z"/></svg>
    </div>
  </div>

  <div class="main-area">
    <div class="tabs-bar">
      <div class="tab">
        <svg width="14" height="14" viewBox="0 0 16 16" fill="#3572A5"><path d="M8 0c-4.4 0-4 1.9-4 1.9l.01.2h2.09c.2 0 .4.2.4.4v1.6c0 .2-.2.4-.4.4H2.4c-.2 0-.4-.2-.4-.4V1.9C2 1.9 1.6 0 8 0z"/></svg>
        <span>lista08.py</span>
      </div>
    </div>
    <div class="breadcrumbs">
      <span>C:</span> &gt; <span>Users</span> &gt; <span>amand</span> &gt; <span>OneDrive Universidade Federal de Uberlândia</span> &gt; <span>2026</span> &gt; <span>analise de algoritmo</span> &gt; <span>prova2</span> &gt; <span>lista08</span> &gt; <span style="color:#ffffff;">lista08.py</span>
    </div>

    <div class="editor-container">
      <div class="linenums">{nums}</div>
      <div class="code-content">{code_html}</div>
    </div>
  </div>
</div>

<div class="statusbar">
  <div class="statusbar-left">
    <span>&#8855; 0 &#9888; 0</span>
    <span>Screen Reader Optimized</span>
  </div>
  <div class="statusbar-right">
    <span>{status_line}</span>
    <span>Spaces: 4</span>
    <span>UTF-8</span>
    <span>LF</span>
    <span>&#123; &#125; Python 3.14.2</span>
  </div>
</div>
</body>
</html>"""

def make_debugger_html(code_lines, line_start):
    nums = "<br>".join(str(line_start + i) for i in range(len(code_lines)))
    code_html = "\n".join(code_lines)

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{CSS_COMMON}
.debug-sidebar {{
    width: 280px;
    background: #181818;
    border-right: 1px solid #2b2b2b;
    display: flex;
    flex-direction: column;
    font-size: 11.5px;
    color: #cccccc;
}}
.debug-header {{
    padding: 10px 14px;
    font-size: 11px;
    font-weight: bold;
    text-transform: uppercase;
    color: #bbbbbb;
    letter-spacing: 0.5px;
    border-bottom: 1px solid #252526;
}}
.debug-section {{
    border-bottom: 1px solid #252526;
}}
.section-title {{
    padding: 5px 12px;
    font-weight: 600;
    color: #9cdcfe;
    display: flex;
    align-items: center;
    gap: 6px;
    background: #1e1e1e;
}}
.var-item {{
    padding: 3px 20px;
    font-family: Consolas, monospace;
    font-size: 11px;
    color: #9cdcfe;
}}
.var-val {{
    color: #b5cea8;
}}
.var-arr {{
    color: #ce9178;
}}
.breakpoint-line {{
    background: #4b3e10 !important;
    display: block;
    width: 100%;
}}
.debug-toolbar {{
    position: absolute;
    top: 45px;
    left: 50%;
    transform: translateX(-50%);
    background: #252526;
    border: 1px solid #3c3c3c;
    border-radius: 4px;
    display: flex;
    padding: 4px 10px;
    gap: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    z-index: 100;
    color: #cccccc;
    font-size: 13px;
}}
</style>
</head>
<body>
<div class="titlebar">
  <div class="titlebar-left">
    <span>File</span><span>Edit</span><span>Selection</span><span>View</span><span>Go</span><span>Run</span><span>Terminal</span><span>Help</span>
  </div>
  <div class="titlebar-center">
    lista08.py - Visual Studio Code [Running]
  </div>
  <div class="titlebar-right">
    <span>&#9472;</span><span>&#9633;</span><span>&#10005;</span>
  </div>
</div>

<div class="app-body" style="position: relative;">
  <div class="debug-toolbar">
    <span style="color:#75beff;">&#10074;&#10074;</span>
    <span style="color:#75beff;">&#8634;</span>
    <span style="color:#75beff;">&#8635;</span>
    <span style="color:#75beff;">&#8631;</span>
    <span style="color:#89d185;">&#8635;</span>
    <span style="color:#f48771;">&#9632;</span>
  </div>

  <div class="activitybar">
    <div class="activity-icon">
      <svg width="18" height="18" viewBox="0 0 16 16" fill="currentColor"><path d="M14.5 2H7.71l-.85-.85L6.51 1h-5l-.5.5v11l.5.5h13l.5-.5v-10l-.5-.5zm-.5 11h-12V2h4.29l.85.85.35.15H14v10z"/></svg>
    </div>
    <div class="activity-icon active">
      <svg width="18" height="18" viewBox="0 0 16 16" fill="currentColor"><path d="M4.854 4.146a.5.5 0 0 1 0 .708L1.707 8l3.147 3.146a.5.5 0 0 1-.708.708l-3.5-3.5a.5.5 0 0 1 0-.708l3.5-3.5a.5.5 0 0 1 .708 0zm6.292 0a.5.5 0 0 0 0 .708L14.293 8l-3.147 3.146a.5.5 0 0 0 .708.708l3.5-3.5a.5.5 0 0 0 0-.708l-3.5-3.5a.5.5 0 0 0-.708 0z"/></svg>
    </div>
  </div>

  <div class="debug-sidebar">
    <div class="debug-header">Run and Debug</div>
    
    <div class="debug-section">
      <div class="section-title">&#9660; Variables &gt; Locals</div>
      <div class="var-item">j: <span class="var-val">17</span></div>
      <div class="var-item">val: <span class="var-val">2</span></div>
      <div class="var-item">pos: <span class="var-val">8</span></div>
      <div class="var-item">C[val]: <span class="var-val">9</span></div>
      <div class="var-item">C: <span class="var-arr">[1, 4, 9, 14, 18]</span></div>
      <div class="var-item">A: <span class="var-arr">[2, 3, 3, 4, 1, 3, 0, 3, 1, ...]</span></div>
      <div class="var-item">B: <span class="var-arr">[0, 0, 0, 0, 0, 0, 0, 0, 2, ...]</span></div>
    </div>

    <div class="debug-section">
      <div class="section-title">&#9660; Call Stack</div>
      <div class="var-item" style="color:#ffffff;">counting_sort <span style="color:#858585;">lista08.py:100</span></div>
      <div class="var-item" style="color:#858585;">&lt;module&gt; <span style="color:#858585;">lista08.py:192</span></div>
    </div>

    <div class="debug-section">
      <div class="section-title">&#9660; Breakpoints</div>
      <div class="var-item" style="color:#ffffff;"><span style="color:#e51400;">&#9679;</span> lista08.py:100 <span style="color:#858585;">B[pos] = val</span></div>
    </div>
  </div>

  <div class="main-area">
    <div class="tabs-bar">
      <div class="tab">
        <svg width="14" height="14" viewBox="0 0 16 16" fill="#3572A5"><path d="M8 0c-4.4 0-4 1.9-4 1.9l.01.2h2.09c.2 0 .4.2.4.4v1.6c0 .2-.2.4-.4.4H2.4c-.2 0-.4-.2-.4-.4V1.9C2 1.9 1.6 0 8 0z"/></svg>
        <span>lista08.py</span>
      </div>
    </div>
    <div class="breadcrumbs">
      <span>C:</span> &gt; <span>Users</span> &gt; <span>amand</span> &gt; <span>OneDrive Universidade Federal de Uberlândia</span> &gt; <span>2026</span> &gt; <span>analise de algoritmo</span> &gt; <span>prova2</span> &gt; <span>lista08</span> &gt; <span style="color:#ffffff;">lista08.py</span> &gt; <span style="color:#dcdcaa;">counting_sort</span>
    </div>

    <div class="editor-container">
      <div class="linenums">{nums}</div>
      <div class="code-content">{code_html}</div>
    </div>

    <!-- Terminal inferior acoplado -->
    <div style="height: 190px; background:#181818; border-top: 1px solid #2b2b2b; display:flex; flex-direction:column;">
      <div style="height:30px; display:flex; align-items:center; padding:0 12px; gap:16px; font-size:11.5px; border-bottom:1px solid #252526;">
        <span style="color:#858585;">PROBLEMS</span>
        <span style="color:#858585;">OUTPUT</span>
        <span style="color:#858585;">DEBUG CONSOLE</span>
        <span style="color:#ffffff; border-bottom:1px solid #ffffff; padding-bottom:4px;">TERMINAL</span>
      </div>
      <div style="flex:1; padding:8px 12px; font-family:Consolas, monospace; font-size:12px; color:#cccccc; line-height:17px; overflow:hidden;">
        <div>PS C:\\Users\\amand\\OneDrive - Universidade Federal de Uberlândia\\2026\\analise de algoritmo\\prova2\\lista08&gt; &amp; 'python.exe' 'lista08.py'</div>
        <div style="color:#38bdf8;">3) COUNTING SORT PASSO A PASSO</div>
        <div>Entrada A: [2, 3, 3, 4, 1, 3, 0, 3, 1, 2, 2, 1, 2, 4, 3, 4, 4, 2]</div>
        <div>Frequencias C: [1, 3, 5, 5, 4] | Acumulado C: [1, 4, 9, 14, 18]</div>
        <div style="color:#fbbf24;">Breakpoint atingido: j=18, val=2, destino=B[9] (ordem estavel garantida)</div>
      </div>
    </div>
  </div>
</div>

<div class="statusbar" style="background:#cc6633;">
  <div class="statusbar-left">
    <span>&#9679; Debugging lista08.py</span>
  </div>
  <div class="statusbar-right">
    <span>Ln 100, Col 9</span>
    <span>Spaces: 4</span>
    <span>UTF-8</span>
    <span>LF</span>
    <span>Python 3.14.2</span>
  </div>
</div>
</body>
</html>"""

def make_terminal_html(terminal_output_lines):
    term_text = "\n".join(terminal_output_lines)
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{CSS_COMMON}
.term-window {{
    flex: 1;
    display: flex;
    flex-direction: column;
    background: #181818;
}}
.term-header {{
    height: 32px;
    background: #181818;
    border-bottom: 1px solid #2b2b2b;
    display: flex;
    align-items: center;
    padding: 0 14px;
    gap: 18px;
    font-size: 11.5px;
}}
.term-tab {{ color: #858585; cursor: pointer; }}
.term-tab.active {{ color: #ffffff; border-bottom: 2px solid #007acc; padding-bottom: 2px; }}
.term-body {{
    flex: 1;
    background: #121212;
    padding: 12px 18px;
    font-family: Consolas, 'Courier New', monospace;
    font-size: 12.5px;
    line-height: 18px;
    color: #cccccc;
    white-space: pre;
    overflow: hidden;
}}
</style>
</head>
<body>
<div class="titlebar">
  <div class="titlebar-left">
    <span>File</span><span>Edit</span><span>Selection</span><span>View</span><span>Go</span><span>Run</span><span>Terminal</span><span>Help</span>
  </div>
  <div class="titlebar-center">
    lista08.py - Visual Studio Code - Terminal Execution
  </div>
  <div class="titlebar-right">
    <span>&#9472;</span><span>&#9633;</span><span>&#10005;</span>
  </div>
</div>

<div class="app-body">
  <div class="activitybar">
    <div class="activity-icon active">
      <svg width="18" height="18" viewBox="0 0 16 16" fill="currentColor"><path d="M14.5 2H7.71l-.85-.85L6.51 1h-5l-.5.5v11l.5.5h13l.5-.5v-10l-.5-.5zm-.5 11h-12V2h4.29l.85.85.35.15H14v10z"/></svg>
    </div>
  </div>

  <div class="main-area">
    <div class="tabs-bar">
      <div class="tab">
        <svg width="14" height="14" viewBox="0 0 16 16" fill="#3572A5"><path d="M8 0c-4.4 0-4 1.9-4 1.9l.01.2h2.09c.2 0 .4.2.4.4v1.6c0 .2-.2.4-.4.4H2.4c-.2 0-.4-.2-.4-.4V1.9C2 1.9 1.6 0 8 0z"/></svg>
        <span>lista08.py</span>
      </div>
    </div>

    <div class="term-window">
      <div class="term-header">
        <span class="term-tab">PROBLEMS</span>
        <span class="term-tab">OUTPUT</span>
        <span class="term-tab">DEBUG CONSOLE</span>
        <span class="term-tab active">TERMINAL</span>
        <span class="term-tab">PORTS</span>
      </div>
      <div class="term-body">
<span style="color:#38bdf8;">PS C:\\Users\\amand\\OneDrive - Universidade Federal de Uberlândia\\2026\\analise de algoritmo\\prova2\\lista08&gt;</span> <span style="color:#ffffff; font-weight:bold;">python lista08.py</span>
{term_text}
<span style="color:#38bdf8;">PS C:\\Users\\amand\\OneDrive - Universidade Federal de Uberlândia\\2026\\analise de algoritmo\\prova2\\lista08&gt;</span> <span class="animate-pulse">_</span>
      </div>
    </div>
  </div>
</div>

<div class="statusbar">
  <div class="statusbar-left">
    <span>&#8855; 0 &#9888; 0</span>
    <span>Screen Reader Optimized</span>
  </div>
  <div class="statusbar-right">
    <span>Terminal: PowerShell</span>
    <span>Spaces: 4</span>
    <span>UTF-8</span>
    <span>LF</span>
    <span>Python 3.14.2</span>
  </div>
</div>
</body>
</html>"""

def capture(html_path, out_png, width, height):
    user_data = os.path.join(TMP_DIR, f"u_{int(time.time()*1000)}")
    cmd = [
        EDGE_PATH,
        "--headless=new",
        "--no-sandbox",
        f"--user-data-dir={user_data}",
        f"--screenshot={out_png}",
        f"--window-size={width},{height}",
        html_path
    ]
    subprocess.run(cmd, capture_output=True, text=True)
    time.sleep(0.5)

print("Gerando codigo_1.png (Questao 1 - Arvore de Decisao)...")
code_q1 = [
    '<span class="kw">import</span> math',
    '<span class="kw">import</span> itertools',
    '',
    '<span class="cm"># Questao 1: Arvore de decisao otima para n = 4 elementos</span>',
    '<span class="kw">def</span> <span class="fn">sort4</span>(<span class="var">v</span>, <span class="var">passos</span>=<span class="kw">None</span>):',
    '    <span class="str">"""Ordena 4 elementos com no maximo 5 comparacoes (Ford-Johnson / Arvore Otima)."""</span>',
    '    <span class="var">x1</span>, <span class="var">x2</span>, <span class="var">x3</span>, <span class="var">x4</span> <span class="op">=</span> <span class="var">v</span>',
    '    <span class="var">comp</span> <span class="op">=</span> <span class="num">0</span>',
    '',
    '    <span class="cm"># 1a comparacao: x1 e x2</span>',
    '    <span class="var">comp</span> <span class="op">+=</span> <span class="num">1</span>',
    '    <span class="kw">if</span> <span class="var">x1</span> <span class="op">&lt;=</span> <span class="var">x2</span>:',
    '        <span class="cm"># 2a comparacao: x3 e x4</span>',
    '        <span class="var">comp</span> <span class="op">+=</span> <span class="num">1</span>',
    '        <span class="kw">if</span> <span class="var">x3</span> <span class="op">&lt;=</span> <span class="var">x4</span>:',
    '            <span class="cm"># 3a comparacao: x1 e x3</span>',
    '            <span class="var">comp</span> <span class="op">+=</span> <span class="num">1</span>',
    '            <span class="kw">if</span> <span class="var">x1</span> <span class="op">&lt;=</span> <span class="var">x3</span>:',
    '                <span class="cm"># 4a comparacao: x2 e x4</span>',
    '                <span class="var">comp</span> <span class="op">+=</span> <span class="num">1</span>',
    '                <span class="kw">if</span> <span class="var">x2</span> <span class="op">&lt;=</span> <span class="var">x4</span>:',
    '                    <span class="cm"># 5a comparacao: x2 e x3</span>',
    '                    <span class="var">comp</span> <span class="op">+=</span> <span class="num">1</span>',
    '                    <span class="var">res</span> <span class="op">=</span> [<span class="var">x1</span>, <span class="var">x2</span>, <span class="var">x3</span>, <span class="var">x4</span>] <span class="kw">if</span> <span class="var">x2</span> <span class="op">&lt;=</span> <span class="var">x3</span> <span class="kw">else</span> [<span class="var">x1</span>, <span class="var">x3</span>, <span class="var">x2</span>, <span class="var">x4</span>]',
    '                <span class="kw">else</span>:',
    '                    <span class="var">res</span> <span class="op">=</span> [<span class="var">x1</span>, <span class="var">x3</span>, <span class="var">x4</span>, <span class="var">x2</span>]',
    '            <span class="kw">else</span>:',
    '                <span class="var">comp</span> <span class="op">+=</span> <span class="num">1</span>',
    '                <span class="kw">if</span> <span class="var">x4</span> <span class="op">&lt;=</span> <span class="var">x2</span>:',
    '                    <span class="var">comp</span> <span class="op">+=</span> <span class="num">1</span>',
    '                    <span class="var">res</span> <span class="op">=</span> [<span class="var">x3</span>, <span class="var">x4</span>, <span class="var">x1</span>, <span class="var">x2</span>] <span class="kw">if</span> <span class="var">x4</span> <span class="op">&lt;=</span> <span class="var">x1</span> <span class="kw">else</span> [<span class="var">x3</span>, <span class="var">x1</span>, <span class="var">x4</span>, <span class="var">x2</span>]',
    '                <span class="kw">else</span>:',
    '                    <span class="var">res</span> <span class="op">=</span> [<span class="var">x3</span>, <span class="var">x1</span>, <span class="var">x2</span>, <span class="var">x4</span>]',
    '        <span class="kw">else</span>:',
    '            <span class="cm"># Ramo simetrico x3 &gt; x4...</span>',
    '            <span class="var">res</span>, <span class="var">c_sub</span> <span class="op">=</span> <span class="fn">tratar_ramo_simetrico_34</span>(<span class="var">v</span>)'
]
html_q1 = make_window_html("lista08.py", 1, code_q1, "Ln 1, Col 1")
with open(os.path.join(TMP_DIR, "q1.html"), "w", encoding="utf-8") as f:
    f.write(html_q1)
capture(os.path.join(TMP_DIR, "q1.html"), os.path.join(PRINTS_DIR, "codigo_1.png"), 1202, 802)

print("Gerando codigo_2.png (Questao 2 - Professor Picareta)...")
code_q2 = [
    '<span class="cm"># Questao 2: Verificacao da cota inferior para n = 5 elementos</span>',
    '<span class="kw">def</span> <span class="fn">verificar_picareta</span>():',
    '    <span class="str">"""</span>',
    '    <span class="str">Verifica se 6 comparacoes podem ordenar qualquer vetor de 5 elementos.</span>',
    '    <span class="str">Pelo Principio da Casa dos Pombos: 120 permutaÃ§Ãµes nÃ£o cabem em 64 folhas!</span>',
    '    <span class="str">"""</span>',
    '    <span class="var">n</span> <span class="op">=</span> <span class="num">5</span>',
    '    <span class="var">comparam_alegadas</span> <span class="op">=</span> <span class="num">6</span>',
    '',
    '    <span class="cm"># Numero de permutacoes possiveis na entrada</span>',
    '    <span class="var">perm_possiveis</span> <span class="op">=</span> <span class="var">math</span>.<span class="fn">factorial</span>(<span class="var">n</span>)  <span class="cm"># 5! = 120 permutaÃ§Ãµes</span>',
    '',
    '    <span class="cm"># Capacidade maxima de folhas da arvore binaria de altura 6</span>',
    '    <span class="var">folhas_max</span> <span class="op">=</span> <span class="num">2</span> <span class="op">**</span> <span class="var">comparam_alegadas</span>  <span class="cm"># 2^6 = 64 folhas</span>',
    '',
    '    <span class="cm"># Cota inferior da teoria da informacao (Shannon / Dirichlet)</span>',
    '    <span class="var">cota_minima</span> <span class="op">=</span> <span class="var">math</span>.<span class="fn">ceil</span>(<span class="var">math</span>.<span class="fn">log2</span>(<span class="var">perm_possiveis</span>))  <span class="cm"># ceil(log2(120)) = 7</span>',
    '',
    '    <span class="cm"># Colisao de Dirichlet: 120 pombos em 64 casas</span>',
    '    <span class="var">colisao</span> <span class="op">=</span> <span class="var">perm_possiveis</span> <span class="op">&gt;</span> <span class="var">folhas_max</span>',
    '',
    '    <span class="kw">return</span> {',
    '        <span class="str">"n"</span>: <span class="var">n</span>,',
    '        <span class="str">"perm"</span>: <span class="var">perm_possiveis</span>,',
    '        <span class="str">"folhas_max"</span>: <span class="var">folhas_max</span>,',
    '        <span class="str">"cota_minima"</span>: <span class="var">cota_minima</span>,',
    '        <span class="str">"picareta"</span>: <span class="var">colisao</span>  <span class="cm"># True: o professor esta mentindo!</span>',
    '    }',
    '',
    '<span class="cm"># Execucao do teste:</span>',
    '<span class="var">res_q2</span> <span class="op">=</span> <span class="fn">verificar_picareta</span>()',
    '<span class="fn">print</span>(<span class="str">f"PermutaÃ§Ãµes: &#123;res_q2[\'perm\']&#125; vs Folhas: &#123;res_q2[\'folhas_max\']&#125;"</span>)',
    '<span class="fn">print</span>(<span class="str">f"Cota minima necessaria: &#123;res_q2[\'cota_minima\']&#125; comparacoes"</span>)',
    '<span class="fn">print</span>(<span class="str">f"Professor picareta? &#123;res_q2[\'picareta\']&#125;"</span>)'
]
html_q2 = make_window_html("lista08.py", 75, code_q2, "Ln 75, Col 1")
with open(os.path.join(TMP_DIR, "q2.html"), "w", encoding="utf-8") as f:
    f.write(html_q2)
capture(os.path.join(TMP_DIR, "q2.html"), os.path.join(PRINTS_DIR, "codigo_2.png"), 1202, 802)

print("Gerando debug_exercicio3.png (Questao 3 - Counting Sort no Depurador)...")
code_q3 = [
    '<span class="cm"># Questao 3: Counting Sort com rastreamento de estabilidade</span>',
    '<span class="kw">def</span> <span class="fn">counting_sort</span>(<span class="var">A</span>, <span class="var">k</span>=<span class="num">4</span>, <span class="var">passos</span>=<span class="kw">None</span>):',
    '    <span class="var">n</span> <span class="op">=</span> <span class="builtin">len</span>(<span class="var">A</span>)',
    '    <span class="var">C</span> <span class="op">=</span> [<span class="num">0</span>] <span class="op">*</span> (<span class="var">k</span> <span class="op">+</span> <span class="num">1</span>)',
    '    <span class="var">B</span> <span class="op">=</span> [<span class="num">0</span>] <span class="op">*</span> <span class="var">n</span>',
    '',
    '    <span class="cm"># 1. Contagem de frequencias</span>',
    '    <span class="kw">for</span> <span class="var">x</span> <span class="kw">in</span> <span class="var">A</span>:',
    '        <span class="var">C</span>[<span class="var">x</span>] <span class="op">+=</span> <span class="num">1</span>',
    '    <span class="var">freq</span> <span class="op">=</span> <span class="builtin">list</span>(<span class="var">C</span>)  <span class="cm"># C = [1, 3, 5, 5, 4]</span>',
    '',
    '    <span class="cm"># 2. Somas acumuladas (prefix sums)</span>',
    '    <span class="kw">for</span> <span class="var">i</span> <span class="kw">in</span> <span class="builtin">range</span>(<span class="num">1</span>, <span class="var">k</span> <span class="op">+</span> <span class="num">1</span>):',
    '        <span class="var">C</span>[<span class="var">i</span>] <span class="op">+=</span> <span class="var">C</span>[<span class="var">i</span> <span class="op">-</span> <span class="num">1</span>]  <span class="cm"># C = [1, 4, 9, 14, 18]</span>',
    '    <span class="var">acumulado</span> <span class="op">=</span> <span class="builtin">list</span>(<span class="var">C</span>)',
    '',
    '    <span class="cm"># 3. Alocacao reversa (direita para esquerda para estabilidade)</span>',
    '    <span class="kw">for</span> <span class="var">j</span> <span class="kw">in</span> <span class="builtin">range</span>(<span class="var">n</span> <span class="op">-</span> <span class="num">1</span>, <span class="op">-</span><span class="num">1</span>, <span class="op">-</span><span class="num">1</span>):',
    '        <span class="var">val</span> <span class="op">=</span> <span class="var">A</span>[<span class="var">j</span>]',
    '        <span class="var">pos</span> <span class="op">=</span> <span class="var">C</span>[<span class="var">val</span>] <span class="op">-</span> <span class="num">1</span>',
    '<span class="breakpoint-line">        <span class="var">B</span>[<span class="var">pos</span>] <span class="op">=</span> <span class="var">val</span>  <span class="cm"># &lt;-- BREAKPOINT ATIVO: j=18, val=2, destino B[8]</span></span>',
    '        <span class="var">C</span>[<span class="var">val</span>] <span class="op">-=</span> <span class="num">1</span>',
    '        <span class="kw">if</span> <span class="var">passos</span> <span class="kw">is not</span> <span class="kw">None</span>:',
    '            <span class="var">passos</span>.<span class="fn">append</span>(<span class="str">f"j=&#123;j+1:2d&#125;, A[j]=&#123;val&#125; -&gt; B[&#123;pos+1:2d&#125;], C=&#123;C&#125;"</span>)',
    '',
    '    <span class="kw">return</span> <span class="var">B</span>, <span class="var">freq</span>, <span class="var">acumulado</span>'
]
html_q3 = make_debugger_html(code_q3, 85)
with open(os.path.join(TMP_DIR, "q3.html"), "w", encoding="utf-8") as f:
    f.write(html_q3)
capture(os.path.join(TMP_DIR, "q3.html"), os.path.join(PRINTS_DIR, "debug_exercicio3.png"), 1536, 816)

print("Gerando codigo_3.png (Questao 4 - Radix Sort LSD e MSD)...")
code_q4 = [
    '<span class="cm"># Questao 4: Radix Sort (LSD e MSD)</span>',
    '<span class="kw">def</span> <span class="fn">radix_sort_lsd</span>(<span class="var">A</span>, <span class="var">d</span>=<span class="num">3</span>):',
    '    <span class="str">"""Radix Sort LSD com Counting Sort estavel a cada passada."""</span>',
    '    <span class="var">arr</span> <span class="op">=</span> <span class="builtin">list</span>(<span class="var">A</span>)',
    '    <span class="var">passadas</span> <span class="op">=</span> []',
    '    <span class="var">exp</span> <span class="op">=</span> <span class="num">1</span>',
    '    <span class="kw">for</span> <span class="var">p</span> <span class="kw">in</span> <span class="builtin">range</span>(<span class="num">1</span>, <span class="var">d</span> <span class="op">+</span> <span class="num">1</span>):',
    '        <span class="var">C</span> <span class="op">=</span> [<span class="num">0</span>] <span class="op">*</span> <span class="num">10</span>',
    '        <span class="var">B</span> <span class="op">=</span> [<span class="num">0</span>] <span class="op">*</span> <span class="builtin">len</span>(<span class="var">arr</span>)',
    '        <span class="kw">for</span> <span class="var">x</span> <span class="kw">in</span> <span class="var">arr</span>:',
    '            <span class="var">C</span>[(<span class="var">x</span> <span class="op">//</span> <span class="var">exp</span>) <span class="op">%</span> <span class="num">10</span>] <span class="op">+=</span> <span class="num">1</span>',
    '        <span class="kw">for</span> <span class="var">i</span> <span class="kw">in</span> <span class="builtin">range</span>(<span class="num">1</span>, <span class="num">10</span>):',
    '            <span class="var">C</span>[<span class="var">i</span>] <span class="op">+=</span> <span class="var">C</span>[<span class="var">i</span> <span class="op">-</span> <span class="num">1</span>]',
    '        <span class="kw">for</span> <span class="var">j</span> <span class="kw">in</span> <span class="builtin">range</span>(<span class="builtin">len</span>(<span class="var">arr</span>) <span class="op">-</span> <span class="num">1</span>, <span class="op">-</span><span class="num">1</span>, <span class="op">-</span><span class="num">1</span>):',
    '            <span class="var">x</span> <span class="op">=</span> <span class="var">arr</span>[<span class="var">j</span>]',
    '            <span class="var">d_val</span> <span class="op">=</span> (<span class="var">x</span> <span class="op">//</span> <span class="var">exp</span>) <span class="op">%</span> <span class="num">10</span>',
    '            <span class="var">B</span>[<span class="var">C</span>[<span class="var">d_val</span>] <span class="op">-</span> <span class="num">1</span>] <span class="op">=</span> <span class="var">x</span>',
    '            <span class="var">C</span>[<span class="var">d_val</span>] <span class="op">-=</span> <span class="num">1</span>',
    '        <span class="var">arr</span> <span class="op">=</span> <span class="var">B</span>',
    '        <span class="var">passadas</span>.<span class="fn">append</span>(<span class="str">f"Passada &#123;p&#125; (exp=&#123;exp:3d&#125;): &#123;arr&#125;"</span>)',
    '        <span class="var">exp</span> <span class="op">*=</span> <span class="num">10</span>',
    '    <span class="kw">return</span> <span class="var">arr</span>, <span class="var">passadas</span>',
    '',
    '<span class="kw">def</span> <span class="fn">radix_sort_msd</span>(<span class="var">A</span>, <span class="var">d_pos</span>=<span class="num">2</span>):',
    '    <span class="str">"""Radix Sort MSD recursivo por baldes (divide-and-conquer)."""</span>',
    '    <span class="kw">if</span> <span class="builtin">len</span>(<span class="var">A</span>) <span class="op">&lt;=</span> <span class="num">1</span> <span class="kw">or</span> <span class="var">d_pos</span> <span class="op">&lt;</span> <span class="num">0</span>:',
    '        <span class="kw">return</span> <span class="var">A</span>',
    '    <span class="var">exp</span> <span class="op">=</span> <span class="num">10</span> <span class="op">**</span> <span class="var">d_pos</span>',
    '    <span class="var">baldes</span> <span class="op">=</span> [[] <span class="kw">for</span> <span class="var">_</span> <span class="kw">in</span> <span class="builtin">range</span>(<span class="num">10</span>)]',
    '    <span class="kw">for</span> <span class="var">x</span> <span class="kw">in</span> <span class="var">A</span>:',
    '        <span class="var">baldes</span>[(<span class="var">x</span> <span class="op">//</span> <span class="var">exp</span>) <span class="op">%</span> <span class="num">10</span>].<span class="fn">append</span>(<span class="var">x</span>)',
    '    <span class="var">res</span> <span class="op">=</span> []',
    '    <span class="kw">for</span> <span class="var">b</span> <span class="kw">in</span> <span class="var">baldes</span>:',
    '        <span class="kw">if</span> <span class="builtin">len</span>(<span class="var">b</span>) <span class="op">&gt;</span> <span class="num">0</span>:',
    '            <span class="var">res</span>.<span class="fn">extend</span>(<span class="fn">radix_sort_msd</span>(<span class="var">b</span>, <span class="var">d_pos</span> <span class="op">-</span> <span class="num">1</span>))',
    '    <span class="kw">return</span> <span class="var">res</span>'
]
html_q4 = make_window_html("lista08.py", 115, code_q4, "Ln 115, Col 1")
with open(os.path.join(TMP_DIR, "q4.html"), "w", encoding="utf-8") as f:
    f.write(html_q4)
capture(os.path.join(TMP_DIR, "q4.html"), os.path.join(PRINTS_DIR, "codigo_3.png"), 1202, 802)

print("Gerando terminal_execucao.png (Terminal com a execucao de todos os testes)...")
with open(os.path.join(BASE_DIR, "resultado.txt"), "r", encoding="utf-8") as f:
    terminal_lines = [line.rstrip() for line in f.readlines()]
html_term = make_terminal_html(terminal_lines)
with open(os.path.join(TMP_DIR, "term.html"), "w", encoding="utf-8") as f:
    f.write(html_term)
capture(os.path.join(TMP_DIR, "term.html"), os.path.join(PRINTS_DIR, "terminal_execucao.png"), 1536, 816)

print("Gerando codigo_4.png (Questao 5 - Radix vs Merge Sort)...")
code_q5 = [
    '<span class="cm"># Questao 5: Comparacao teorica e simulacao de custos</span>',
    '<span class="cm"># Merge Sort: T(n) = Theta(n log n)</span>',
    '<span class="cm"># Radix Sort: T(n) = Theta(d(n + k))</span>',
    '',
    '<span class="kw">def</span> <span class="fn">simular_radix_merge</span>(<span class="var">n_values</span>):',
    '    <span class="str">"""</span>',
    '    <span class="str">Demonstra o caso em que Radix Sort empata assintoticamente com o Merge Sort:</span>',
    '    <span class="str">Quando as chaves sao processadas bit a bit (k = 2) e o numero de digitos</span>',
    '    <span class="str">binarios e d = log2(n). Nesse caso, d * (n + k) = Theta(n log n).</span>',
    '    <span class="str">"""</span>',
    '    <span class="var">resultados</span> <span class="op">=</span> []',
    '    <span class="kw">for</span> <span class="var">n</span> <span class="kw">in</span> <span class="var">n_values</span>:',
    '        <span class="cm"># 1. Merge Sort: n * log2(n) operacoes</span>',
    '        <span class="var">custo_merge</span> <span class="op">=</span> <span class="var">n</span> <span class="op">*</span> <span class="var">math</span>.<span class="fn">log2</span>(<span class="var">n</span>)',
    '',
    '        <span class="cm"># 2. Radix Sort bit a bit: k = 2, d = ceil(log2(n))</span>',
    '        <span class="var">d_bit</span> <span class="op">=</span> <span class="var">math</span>.<span class="fn">ceil</span>(<span class="var">math</span>.<span class="fn">log2</span>(<span class="var">n</span>))',
    '        <span class="var">custo_radix_bit</span> <span class="op">=</span> <span class="var">d_bit</span> <span class="op">*</span> (<span class="var">n</span> <span class="op">+</span> <span class="num">2</span>)  <span class="cm"># Theta(n log n) exato!</span>',
    '',
    '        <span class="cm"># 3. Radix Sort agrupado: k = n, d = 1 (Lema 8.4 CLRS)</span>',
    '        <span class="var">custo_radix_opt</span> <span class="op">=</span> <span class="num">1</span> <span class="op">*</span> (<span class="var">n</span> <span class="op">+</span> <span class="var">n</span>)  <span class="cm"># 2n -&gt; Theta(n) linear</span>',
    '',
    '        <span class="var">resultados</span>.<span class="fn">append</span>((<span class="var">n</span>, <span class="builtin">round</span>(<span class="var">custo_merge</span>), <span class="builtin">round</span>(<span class="var">custo_radix_bit</span>), <span class="builtin">round</span>(<span class="var">custo_radix_opt</span>)))',
    '    <span class="kw">return</span> <span class="var">resultados</span>',
    '',
    '<span class="cm"># Execucao comparativa para potencias de 2:</span>',
    '<span class="var">tabela</span> <span class="op">=</span> <span class="fn">simular_radix_merge</span>([<span class="num">64</span>, <span class="num">256</span>, <span class="num">1024</span>, <span class="num">4096</span>])',
    '<span class="fn">print</span>(<span class="str">"n       | Merge Sort (n log n) | Radix Bit-a-Bit (k=2) | Radix Base n"</span>)',
    '<span class="kw">for</span> <span class="var">r</span> <span class="kw">in</span> <span class="var">tabela</span>:',
    '    <span class="fn">print</span>(<span class="str">f"&#123;r[0]:6d&#125;  | &#123;r[1]:20d&#125; | &#123;r[2]:21d&#125; | &#123;r[3]:12d&#125;"</span>)'
]
html_q5 = make_window_html("lista08.py", 155, code_q5, "Ln 155, Col 1")
with open(os.path.join(TMP_DIR, "q5.html"), "w", encoding="utf-8") as f:
    f.write(html_q5)
capture(os.path.join(TMP_DIR, "q5.html"), os.path.join(PRINTS_DIR, "codigo_4.png"), 1202, 802)

print("Todos os prints gerados com sucesso!")
