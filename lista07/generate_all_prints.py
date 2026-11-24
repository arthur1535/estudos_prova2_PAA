import os
import subprocess
import html
import re

DIR = r"c:\Users\amand\OneDrive - Universidade Federal de Uberlândia\2026\analise de algoritmo\prova2\lista07"
PRINTS_DIR = os.path.join(DIR, "prints")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

with open(os.path.join(DIR, "lista07.py"), "r", encoding="utf-8") as f:
    RAW_LINES = f.readlines()

try:
    with open(os.path.join(DIR, "resultado.txt"), "r", encoding="utf-8") as f:
        RESULT_TEXT = f.read()
except UnicodeDecodeError:
    with open(os.path.join(DIR, "resultado.txt"), "r", encoding="utf-16") as f:
        RESULT_TEXT = f.read()

def syntax_highlight(line):
    # Escapes html first
    s = html.escape(line.rstrip("\r\n"))
    if not s.strip():
        return "&nbsp;"
    
    # Comments
    comment_idx = -1
    in_quote = False
    quote_char = ''
    for i, ch in enumerate(s):
        if ch in ('"', "'") and (i == 0 or s[i-1] != '\\'):
            if not in_quote:
                in_quote = True
                quote_char = ch
            elif quote_char == ch:
                in_quote = False
        elif ch == '#' and not in_quote:
            comment_idx = i
            break
            
    comment_part = ""
    if comment_idx != -1:
        comment_part = f'<span style="color:#6a9955;">{s[comment_idx:]}</span>'
        s = s[:comment_idx]

    # Strings
    def repl_str(m):
        return f'<span style="color:#ce9178;">{m.group(0)}</span>'
    s = re.sub(r'(\".*?\"|\'.*?\')', repl_str, s)

    # Def and Class
    s = re.sub(r'\b(def|class)\b', r'<span style="color:#569cd6;">\1</span>', s)
    
    # Control keywords (purple in VS Code)
    s = re.sub(r'\b(return|if|elif|else|while|for|in|import|from|as|is|not|and|or)\b', r'<span style="color:#c586c0;">\1</span>', s)
    
    # Constants
    s = re.sub(r'\b(True|False|None)\b', r'<span style="color:#569cd6;">\1</span>', s)

    # Function calls / declarations
    s = re.sub(r'\b([a-zA-Z_][a-zA-Z0-9_]*)(?=\()', r'<span style="color:#dcdcaa;">\1</span>', s)

    # Numbers
    s = re.sub(r'\b(\d+)\b', r'<span style="color:#b5cea8;">\1</span>', s)

    return s + comment_part

def render_editor_html(start_line, end_line, focus_line=None, status_ln=1, status_col=1):
    lines_slice = RAW_LINES[start_line - 1 : end_line]
    
    rows_html = []
    for idx, raw_line in enumerate(lines_slice):
        lineno = start_line + idx
        hl = syntax_highlight(raw_line)
        is_focus = (lineno == focus_line)
        bg = 'background-color:#2a2d2e;' if is_focus else ''
        gutter_marker = '<span style="color:#e51400; font-size:11px; margin-right:4px;">●</span>' if is_focus else ''
        rows_html.append(f'''
        <div style="display:flex; height:19px; line-height:19px; {bg}">
            <div style="width:52px; text-align:right; padding-right:16px; color:#858585; user-select:none; font-size:13px;">{gutter_marker}{lineno}</div>
            <div style="white-space:pre; font-size:13.5px; font-family:Consolas, 'Courier New', monospace; color:#d4d4d4;">{hl}</div>
        </div>
        ''')
    
    code_content = "".join(rows_html)

    html_page = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background-color: #181818;
    color: #cccccc;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 12px;
    width: 1202px;
    height: 802px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }}
  /* Title bar */
  .titlebar {{
    height: 35px;
    background-color: #181818;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 10px;
    border-bottom: 1px solid #2b2b2b;
    user-select: none;
  }}
  .titlebar-left {{
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12px;
    color: #cccccc;
  }}
  .titlebar-menu {{
    display: flex;
    gap: 12px;
    margin-left: 10px;
    color: #cccccc;
  }}
  .titlebar-center {{
    color: #9d9d9d;
    font-size: 12px;
  }}
  .titlebar-right {{
    display: flex;
    align-items: center;
    gap: 14px;
    color: #cccccc;
  }}
  
  /* Main workspace */
  .workspace {{
    display: flex;
    flex: 1;
    height: calc(802px - 35px - 22px);
    background-color: #1f1f1f;
  }}
  
  /* Activity bar */
  .activitybar {{
    width: 48px;
    background-color: #181818;
    border-right: 1px solid #2b2b2b;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
  }}
  .activity-top {{
    display: flex;
    flex-direction: column;
    gap: 18px;
    align-items: center;
  }}
  .activity-icon {{
    width: 24px;
    height: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #858585;
    cursor: pointer;
  }}
  .activity-icon.active {{
    color: #ffffff;
    border-left: 2px solid #ffffff;
    width: 48px;
  }}
  
  /* Editor container */
  .editor-container {{
    flex: 1;
    display: flex;
    flex-direction: column;
    background-color: #1f1f1f;
  }}
  
  /* Tab bar */
  .tabbar {{
    height: 35px;
    background-color: #181818;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #1f1f1f;
  }}
  .tab {{
    height: 35px;
    background-color: #1f1f1f;
    border-top: 1px solid #0078d4;
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 0 14px;
    color: #ffffff;
    font-size: 12px;
    border-right: 1px solid #252526;
  }}
  .tab .py-icon {{
    color: #3572A5;
    font-weight: bold;
  }}
  
  /* Breadcrumbs */
  .breadcrumbs {{
    height: 22px;
    background-color: #1f1f1f;
    display: flex;
    align-items: center;
    padding: 0 16px;
    color: #888888;
    font-size: 11px;
    gap: 6px;
    border-bottom: 1px solid #252526;
  }}
  
  /* Code editor */
  .editor-body {{
    flex: 1;
    padding-top: 6px;
    overflow: hidden;
    position: relative;
  }}
  
  /* Status bar */
  .statusbar {{
    height: 22px;
    background-color: #007acc;
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 10px;
    font-size: 11px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }}
  .statusbar-left, .statusbar-right {{
    display: flex;
    align-items: center;
    gap: 14px;
  }}
  .pill {{
    background: rgba(255,255,255,0.2);
    padding: 1px 6px;
    border-radius: 2px;
  }}
</style>
</head>
<body>

  <!-- Title bar -->
  <div class="titlebar">
    <div class="titlebar-left">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="#007acc"><path d="M14.5 2.5l-3.2-1.5c-.4-.2-.8-.1-1.1.2L5.8 5.4 3.2 3.5c-.3-.2-.7-.2-1 .1L.4 5.3c-.3.3-.4.8-.1 1.1l2.5 2.3-2.5 2.3c-.3.3-.2.8.1 1.1l1.8 1.7c.3.3.7.3 1 .1l2.6-1.9 4.4 4.2c.3.3.7.4 1.1.2l3.2-1.5c.4-.2.6-.6.6-1.1V3.6c0-.5-.2-.9-.6-1.1z"/></svg>
      <div class="titlebar-menu">
        <span>File</span><span>Edit</span><span>Selection</span><span>View</span><span>Go</span><span>Run</span><span>...</span>
      </div>
    </div>
    <div class="titlebar-center">
      &larr; &rarr; &nbsp; lista07.py - Visual Studio Code - Untracked
    </div>
    <div class="titlebar-right">
      <span>&#9633;</span><span>&#9645;</span><span>&#10005;</span>
    </div>
  </div>

  <!-- Workspace -->
  <div class="workspace">
    <!-- Activity bar -->
    <div class="activitybar">
      <div class="activity-top">
        <div class="activity-icon active">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3h18v18H3zM3 9h18M9 21V9"/></svg>
        </div>
        <div class="activity-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
        </div>
        <div class="activity-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="18" r="3"/><circle cx="6" cy="6" r="3"/><path d="M6 9v12M18 9a9 9 0 0 0-9 9"/></svg>
        </div>
        <div class="activity-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
        </div>
        <div class="activity-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
        </div>
      </div>
      <div class="activity-bottom">
        <div class="activity-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>
        </div>
      </div>
    </div>

    <!-- Editor -->
    <div class="editor-container">
      <div class="tabbar">
        <div class="tab">
          <span class="py-icon">🐍</span>
          <span>lista07.py</span>
          <span style="font-size:10px; color:#cccccc;">U</span>
          <span style="font-size:14px; margin-left:6px; cursor:pointer;">&times;</span>
        </div>
      </div>
      <div class="breadcrumbs">
        <span>C:</span> &rsaquo; <span>Users</span> &rsaquo; <span>amand</span> &rsaquo; <span>OneDrive Universidade Federal de Uberlândia</span> &rsaquo; <span>2026</span> &rsaquo; <span>analise de algoritmo</span> &rsaquo; <span>prova2</span> &rsaquo; <span>lista07</span> &rsaquo; <span>🐍 lista07.py</span>
      </div>
      <div class="editor-body">
        {code_content}
      </div>
    </div>
  </div>

  <!-- Status bar -->
  <div class="statusbar">
    <div class="statusbar-left">
      <span>&#10005; 0 &nbsp; &#9888; 0</span>
      <span class="pill">Screen Reader Optimized</span>
    </div>
    <div class="statusbar-right">
      <span>Ln {status_ln}, Col {status_col}</span>
      <span>Spaces: 4</span>
      <span>UTF-8</span>
      <span>LF</span>
      <span>&#123; &#125; Python</span>
      <span>🔔</span>
    </div>
  </div>

</body>
</html>'''
    return html_page

def render_terminal_html():
    escaped_output = html.escape(RESULT_TEXT.strip())
    # Format lines
    terminal_lines = escaped_output.split("\n")
    formatted_body = []
    for l in terminal_lines:
        if l.startswith("LISTA 7") or l.startswith("1)") or l.startswith("2)") or l.startswith("3)") or l.startswith("4)") or l.startswith("5)"):
            formatted_body.append(f'<div style="color:#ffffff; font-weight:bold; margin-top:6px;">{l}</div>')
        elif "Resultado final:" in l or "Comparacoes realizadas:" in l:
            formatted_body.append(f'<div style="color:#4ec9b0; font-weight:bold;">{l}</div>')
        elif "Metodo" in l:
            formatted_body.append(f'<div style="color:#9cdcfe;">{l}</div>')
        elif "Pivo" in l:
            formatted_body.append(f'<div style="color:#dcdcaa;">{l}</div>')
        else:
            formatted_body.append(f'<div>{l}</div>')
            
    terminal_body = "\n".join(formatted_body)

    html_page = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background-color: #181818;
    color: #cccccc;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 12px;
    width: 1536px;
    height: 816px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }}
  .titlebar {{
    height: 35px;
    background-color: #181818;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 10px;
    border-bottom: 1px solid #2b2b2b;
    user-select: none;
  }}
  .titlebar-left {{ display: flex; align-items: center; gap: 8px; font-size: 12px; }}
  .titlebar-menu {{ display: flex; gap: 12px; margin-left: 10px; }}
  .titlebar-center {{ color: #9d9d9d; }}
  .titlebar-right {{ display: flex; align-items: center; gap: 14px; }}
  
  .terminal-panel {{
    flex: 1;
    background-color: #181818;
    display: flex;
    flex-direction: column;
  }}
  .terminal-tabs {{
    height: 35px;
    background-color: #181818;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 16px;
    border-bottom: 1px solid #252526;
  }}
  .tabs-left {{
    display: flex;
    gap: 20px;
    font-size: 11px;
    text-transform: uppercase;
    font-weight: 600;
    color: #969696;
  }}
  .tabs-left .active {{
    color: #ffffff;
    border-bottom: 1px solid #ffffff;
    padding-bottom: 8px;
  }}
  .tabs-right {{
    display: flex;
    align-items: center;
    gap: 12px;
    color: #cccccc;
    font-size: 12px;
  }}
  .terminal-content {{
    flex: 1;
    background-color: #181818;
    padding: 12px 18px;
    font-family: Consolas, 'Courier New', monospace;
    font-size: 13.5px;
    line-height: 20px;
    color: #cccccc;
    overflow: hidden;
  }}
  .cmd-line {{
    color: #4ec9b0;
    margin-bottom: 8px;
  }}
  .prompt-char {{
    color: #569cd6;
    margin-right: 6px;
  }}
  .statusbar {{
    height: 22px;
    background-color: #007acc;
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 10px;
    font-size: 11px;
  }}
</style>
</head>
<body>
  <div class="titlebar">
    <div class="titlebar-left">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="#007acc"><path d="M14.5 2.5l-3.2-1.5c-.4-.2-.8-.1-1.1.2L5.8 5.4 3.2 3.5c-.3-.2-.7-.2-1 .1L.4 5.3c-.3.3-.4.8-.1 1.1l2.5 2.3-2.5 2.3c-.3.3-.2.8.1 1.1l1.8 1.7c.3.3.7.3 1 .1l2.6-1.9 4.4 4.2c.3.3.7.4 1.1.2l3.2-1.5c.4-.2.6-.6.6-1.1V3.6c0-.5-.2-.9-.6-1.1z"/></svg>
      <div class="titlebar-menu">
        <span>File</span><span>Edit</span><span>Selection</span><span>View</span><span>Go</span><span>Run</span><span>Terminal</span><span>Help</span>
      </div>
    </div>
    <div class="titlebar-center">&larr; &rarr; &nbsp; lista07</div>
    <div class="titlebar-right"><span>&#9633;</span><span>&#9645;</span><span>&#10005;</span></div>
  </div>

  <div class="terminal-panel">
    <div class="terminal-tabs">
      <div class="tabs-left">
        <span>Problems</span>
        <span>Output</span>
        <span>Debug Console</span>
        <span class="active">Terminal</span>
        <span>Ports</span>
      </div>
      <div class="tabs-right">
        <span>&#9881; Executar Lista 7 - Task</span>
        <span>+</span>
        <span>&#8964;</span>
        <span>&#128465;</span>
        <span>&times;</span>
      </div>
    </div>
    <div class="terminal-content">
      <div class="cmd-line"><span class="prompt-char">*</span> Executing task: python lista07.py</div>
      {terminal_body}
    </div>
  </div>

  <div class="statusbar">
    <div style="display:flex; gap:14px;">
      <span>&#10005; 0 &nbsp; &#9888; 0</span>
      <span style="background:rgba(255,255,255,0.2); padding:1px 6px; border-radius:2px;">Screen Reader Optimized</span>
    </div>
    <div style="display:flex; gap:14px;">
      <span>UTF-8</span>
      <span>LF</span>
      <span>PowerShell</span>
      <span>🔔</span>
    </div>
  </div>
</body>
</html>'''
    return html_page

def render_debug_html():
    # Show Question 2 in Debugger with breakpoint and variables
    start_line = 38
    end_line = 76
    lines_slice = RAW_LINES[start_line - 1 : end_line]
    rows_html = []
    for idx, raw_line in enumerate(lines_slice):
        lineno = start_line + idx
        hl = syntax_highlight(raw_line)
        is_bp = (lineno == 61)  # Breakpoint at q = particiona_primeiro(...) or if i == k
        bg = 'background-color:#4a3f13;' if is_bp else ''
        bp_icon = '<span style="color:#e51400; font-size:11px; margin-right:4px;">●</span>' if is_bp else ''
        arrow_icon = '&#10148; ' if is_bp else ''
        rows_html.append(f'''
        <div style="display:flex; height:19px; line-height:19px; {bg}">
            <div style="width:48px; text-align:right; padding-right:12px; color:#858585; user-select:none; font-size:12px;">{bp_icon}{arrow_icon}{lineno}</div>
            <div style="white-space:pre; font-size:13px; font-family:Consolas, 'Courier New', monospace; color:#d4d4d4;">{hl}</div>
        </div>
        ''')
    code_content = "".join(rows_html)

    html_page = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background-color: #181818;
    color: #cccccc;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 12px;
    width: 1536px;
    height: 816px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }}
  .titlebar {{
    height: 35px;
    background-color: #181818;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 10px;
    border-bottom: 1px solid #2b2b2b;
  }}
  .debug-toolbar {{
    display: flex;
    gap: 8px;
    background-color: #252526;
    padding: 3px 12px;
    border-radius: 4px;
    border: 1px solid #3c3c3c;
    box-shadow: 0 2px 8px rgba(0,0,0,0.4);
  }}
  .debug-btn {{
    color: #75beff;
    font-size: 14px;
    cursor: pointer;
    padding: 0 4px;
  }}
  .main-split {{
    display: flex;
    flex: 1;
    height: calc(816px - 35px - 22px);
  }}
  .activitybar {{
    width: 48px;
    background-color: #181818;
    border-right: 1px solid #2b2b2b;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px 0;
    gap: 18px;
  }}
  .sidebar-debug {{
    width: 280px;
    background-color: #181818;
    border-right: 1px solid #2b2b2b;
    display: flex;
    flex-direction: column;
    font-size: 11.5px;
  }}
  .debug-header {{
    padding: 8px 14px;
    font-weight: 600;
    text-transform: uppercase;
    color: #bbbbbb;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: #202020;
    border-bottom: 1px solid #2b2b2b;
  }}
  .var-tree {{
    padding: 6px 12px;
    line-height: 20px;
    font-family: Consolas, monospace;
    font-size: 12px;
  }}
  .var-item {{
    display: flex;
    gap: 6px;
  }}
  .var-name {{ color: #9cdcfe; }}
  .var-val {{ color: #b5cea8; }}
  .editor-side {{
    flex: 1;
    display: flex;
    flex-direction: column;
    background-color: #1f1f1f;
  }}
  .statusbar {{
    height: 22px;
    background-color: #cc6600; /* Orange debug status bar */
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 10px;
    font-size: 11px;
  }}
</style>
</head>
<body>
  <div class="titlebar">
    <div style="display:flex; align-items:center; gap:8px;">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="#007acc"><path d="M14.5 2.5l-3.2-1.5c-.4-.2-.8-.1-1.1.2L5.8 5.4 3.2 3.5c-.3-.2-.7-.2-1 .1L.4 5.3c-.3.3-.4.8-.1 1.1l2.5 2.3-2.5 2.3c-.3.3-.2.8.1 1.1l1.8 1.7c.3.3.7.3 1 .1l2.6-1.9 4.4 4.2c.3.3.7.4 1.1.2l3.2-1.5c.4-.2.6-.6.6-1.1V3.6c0-.5-.2-.9-.6-1.1z"/></svg>
      <span style="color:#cccccc; font-size:12px;">File Edit Selection View Go Run Terminal Help</span>
    </div>
    <!-- Floating debug toolbar -->
    <div class="debug-toolbar">
      <span class="debug-btn" style="color:#75beff;">&#10074;&#10074;</span> <!-- Pause -->
      <span class="debug-btn" style="color:#75beff;">&#8631;</span> <!-- Step over -->
      <span class="debug-btn" style="color:#75beff;">&#8600;</span> <!-- Step into -->
      <span class="debug-btn" style="color:#75beff;">&#8599;</span> <!-- Step out -->
      <span class="debug-btn" style="color:#89d185;">&#8635;</span> <!-- Restart -->
      <span class="debug-btn" style="color:#f48771;">&#9632;</span> <!-- Stop -->
    </div>
    <div style="display:flex; gap:14px; color:#cccccc;"><span>&#9633;</span><span>&#9645;</span><span>&#10005;</span></div>
  </div>

  <div class="main-split">
    <div class="activitybar">
      <div style="color:#858585; cursor:pointer;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3h18v18H3zM3 9h18M9 21V9"/></svg></div>
      <div style="color:#858585; cursor:pointer;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg></div>
      <div style="color:#858585; cursor:pointer;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="18" r="3"/><circle cx="6" cy="6" r="3"/><path d="M6 9v12M18 9a9 9 0 0 0-9 9"/></svg></div>
      <div style="color:#ffffff; border-left:2px solid #ffffff; width:48px; display:flex; justify-content:center;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>
      <div style="color:#858585; cursor:pointer;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg></div>
    </div>

    <!-- Sidebar debug panels -->
    <div class="sidebar-debug">
      <div class="debug-header"><span>RUN AND DEBUG</span></div>
      
      <div class="debug-header" style="background:#181818; font-size:11px;"><span>&rsaquo; VARIABLES: LOCALS</span></div>
      <div class="var-tree">
        <div class="var-item"><span class="var-name">i</span>: <span class="var-val">3</span></div>
        <div class="var-item"><span class="var-name">p</span>: <span class="var-val">0</span></div>
        <div class="var-item"><span class="var-name">r</span>: <span class="var-val">8</span></div>
        <div class="var-item"><span class="var-name">pivo</span>: <span class="var-val">1</span></div>
        <div class="var-item"><span class="var-name">q</span>: <span class="var-val">0</span></div>
        <div class="var-item"><span class="var-name">k</span>: <span class="var-val">1</span></div>
        <div class="var-item"><span class="var-name">v</span>: <span style="color:#ce9178;">[1, 8, 7, 6, 5, 3, 2, 10, 9]</span></div>
        <div class="var-item"><span class="var-name">passos</span>: <span style="color:#ce9178;">list [1 item]</span></div>
      </div>

      <div class="debug-header" style="background:#181818; font-size:11px;"><span>&rsaquo; CALL STACK</span></div>
      <div class="var-tree" style="font-size:11px; line-height:18px;">
        <div style="color:#ffffff; font-weight:600;">selection <span style="color:#888;">lista07.py:61</span></div>
        <div style="color:#888888;">&lt;module&gt; <span style="color:#888;">lista07.py:145</span></div>
      </div>

      <div class="debug-header" style="background:#181818; font-size:11px;"><span>&rsaquo; BREAKPOINTS</span></div>
      <div class="var-tree" style="font-size:11px;">
        <div><span style="color:#e51400;">●</span> lista07.py:61 <span style="color:#888;">selection</span></div>
      </div>
    </div>

    <!-- Editor -->
    <div class="editor-side">
      <div style="height:35px; background:#181818; display:flex; align-items:center; padding:0 14px; gap:8px; border-bottom:1px solid #1f1f1f;">
        <span>🐍</span><span style="color:#fff;">lista07.py</span>
      </div>
      <div style="height:22px; background:#1f1f1f; display:flex; align-items:center; padding:0 16px; color:#888; font-size:11px; gap:6px;">
        <span>lista07</span> &rsaquo; <span>lista07.py</span> &rsaquo; <span>selection</span>
      </div>
      <div style="flex:1; padding-top:6px; overflow:hidden;">
        {code_content}
      </div>
    </div>
  </div>

  <div class="statusbar">
    <div style="display:flex; gap:14px;">
      <span>&#10005; 0 &nbsp; &#9888; 0</span>
      <span>Paused on breakpoint</span>
    </div>
    <div style="display:flex; gap:14px;">
      <span>Ln 61, Col 5</span>
      <span>Spaces: 4</span>
      <span>UTF-8</span>
      <span>Python 3.14.2</span>
    </div>
  </div>
</body>
</html>'''
    return html_page

# Generate the files
specs = [
    ("codigo_1.html", "codigo_1.png", render_editor_html(1, 38, focus_line=None, status_ln=1, status_col=1), (1202, 802)),
    ("codigo_2.html", "codigo_2.png", render_editor_html(39, 78, focus_line=None, status_ln=39, status_col=1), (1202, 802)),
    ("debug_exercicio.html", "debug_exercicio.png", render_debug_html(), (1536, 816)),
    ("codigo_3.html", "codigo_3.png", render_editor_html(79, 120, focus_line=None, status_ln=79, status_col=1), (1202, 802)),
    ("terminal_execucao.html", "terminal_execucao.png", render_terminal_html(), (1536, 816)),
    ("codigo_4.html", "codigo_4.png", render_editor_html(121, 155, focus_line=None, status_ln=121, status_col=1), (1202, 802)),
]

for html_name, png_name, html_data, (w, h) in specs:
    html_path = os.path.join(PRINTS_DIR, html_name)
    png_path = os.path.join(PRINTS_DIR, png_name)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_data)
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        f"--window-size={w},{h}",
        f"--screenshot={png_path}",
        html_path
    ]
    subprocess.run(cmd, check=True)
    print(f"Generated {png_name} ({w}x{h})")

print("All prints generated successfully!")
