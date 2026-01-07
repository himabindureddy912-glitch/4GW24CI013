import tkinter as tk
from tkinter import messagebox, scrolledtext
from collections import deque, Counter
import webbrowser
import os
from datetime import datetime

class BrowserSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("DSA Lab: Browser History - REPORT FIXED")
        self.root.geometry("1600x850")
        self.root.configure(bg='lightblue')
        
        # Data structures
        self.current_url = "https://google.com"
        self.back_stack = deque()
        self.forward_stack = deque()
        self.stats = {"visits": 1, "back": 0, "forward": 0}
        self.visit_counts = Counter({"https://google.com": 1})
        
        self.setup_ui()
        self.update_display()
    
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="DSA Lab: Browser History - BACK & FORWARD STACKS", 
                        font=('Arial', 18, 'bold'), bg='navy', fg='white')
        title.pack(pady=10, fill='x')
        
        # Stats
        stats_frame = tk.Frame(self.root, bg='lightgray', height=40)
        stats_frame.pack(fill='x', pady=5)
        stats_frame.pack_propagate(False)
        
        self.visit_label = tk.Label(stats_frame, text="Total Visits: 1", font=('Arial', 14, 'bold'), bg='lightgray')
        self.visit_label.pack(side=tk.LEFT, padx=20)
        self.back_label = tk.Label(stats_frame, text="Back: 0", font=('Arial', 14, 'bold'), bg='lightgray')
        self.back_label.pack(side=tk.LEFT, padx=20)
        self.forward_label = tk.Label(stats_frame, text="Forward: 0", font=('Arial', 14, 'bold'), bg='lightgray')
        self.forward_label.pack(side=tk.LEFT, padx=20)
        
        # Controls
        control_frame = tk.LabelFrame(self.root, text="Controls", font=('Arial', 12, 'bold'))
        control_frame.pack(pady=10, padx=20, fill='x')
        
        # URL input
        url_frame = tk.Frame(control_frame)
        url_frame.pack(pady=10)
        tk.Label(url_frame, text="URL:", font=('Arial', 12)).pack(side=tk.LEFT)
        self.url_entry = tk.Entry(url_frame, font=('Arial', 12), width=40)
        self.url_entry.pack(side=tk.LEFT, padx=10)
        self.url_entry.insert(0, "youtube.com")
        
        tk.Button(url_frame, text="Visit", command=self.visit_url, bg='green', fg='white', 
                 font=('Arial', 11, 'bold'), width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(url_frame, text="Open", command=self.open_browser, bg='orange', fg='white', 
                 font=('Arial', 11, 'bold'), width=10).pack(side=tk.LEFT, padx=5)
        
        # Navigation buttons
        nav_frame = tk.Frame(control_frame)
        nav_frame.pack(pady=10)
        
        self.back_btn = tk.Button(nav_frame, text="⬅️ Back", command=self.go_back, bg='red', fg='white', 
                                 font=('Arial', 11, 'bold'), width=10)
        self.back_btn.pack(side=tk.LEFT, padx=5)
        
        tk.Button(nav_frame, text="🔗 Current", command=self.open_current_browser, bg='blue', fg='white', 
                 font=('Arial', 11, 'bold'), width=12).pack(side=tk.LEFT, padx=5)
        
        self.forward_btn = tk.Button(nav_frame, text="➡️ Forward", command=self.go_forward, bg='orange', fg='white', 
                                    font=('Arial', 11, 'bold'), width=12)
        self.forward_btn.pack(side=tk.LEFT, padx=5)
        
        tk.Button(nav_frame, text="🏠 Home", command=self.go_home, bg='green', fg='white', 
                 font=('Arial', 11, 'bold'), width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(nav_frame, text="📊 Report", command=self.save_report, bg='purple', fg='white', 
                 font=('Arial', 11, 'bold'), width=10).pack(side=tk.LEFT, padx=5)
        
        # 2x2 PERFECT SQUARES
        main_frame = tk.Frame(self.root, bg='lightblue')
        main_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Row 1
        row1 = tk.Frame(main_frame, bg='lightblue')
        row1.pack(fill='both', expand=True, pady=(0,10))
        
        # Current - BIG BLUE BOX
        self.current_frame = tk.LabelFrame(row1, text="📱 CURRENT PAGE", font=('Arial', 14, 'bold'), 
                                          bg='lightcyan', fg='darkblue')
        self.current_frame.pack(side=tk.LEFT, fill='both', expand=True, padx=(0,10))
        self.current_label = tk.Label(self.current_frame, font=('Arial', 16, 'bold'), 
                                     bg='white', fg='darkblue', relief='solid', padx=20, pady=30)
        self.current_label.pack(fill='both', expand=True)
        
        # Counts - GREEN BOX
        self.count_frame = tk.LabelFrame(row1, text="🔢 VISIT COUNTS", font=('Arial', 14, 'bold'), 
                                        bg='lightgreen', fg='darkgreen')
        self.count_frame.pack(side=tk.RIGHT, fill='both', expand=True)
        self.count_text = scrolledtext.ScrolledText(self.count_frame, height=15, font=('Courier', 11), bg='white')
        self.count_text.pack(fill='both', expand=True, padx=15, pady=15)
        
        # Row 2
        row2 = tk.Frame(main_frame, bg='lightblue')
        row2.pack(fill='both', expand=True)
        
        # Back - YELLOW BOX
        self.back_frame = tk.LabelFrame(row2, text="⬅️ BACK STACK", font=('Arial', 14, 'bold'), 
                                       bg='lightyellow', fg='darkred')
        self.back_frame.pack(side=tk.LEFT, fill='both', expand=True, padx=(0,10))
        self.back_text = scrolledtext.ScrolledText(self.back_frame, height=15, font=('Courier', 11), bg='white')
        self.back_text.pack(fill='both', expand=True, padx=15, pady=15)
        
        # Forward - RED BOX
        self.fwd_frame = tk.LabelFrame(row2, text="➡️ FORWARD STACK ✅", font=('Arial', 14, 'bold'), 
                                      bg='lightcoral', fg='darkred')
        self.fwd_frame.pack(side=tk.RIGHT, fill='both', expand=True)
        self.fwd_text = scrolledtext.ScrolledText(self.fwd_frame, height=15, font=('Courier', 12, 'bold'), bg='white')
        self.fwd_text.pack(fill='both', expand=True, padx=15, pady=15)
    
    def open_current_browser(self):
        webbrowser.open(self.current_url)
        messagebox.showinfo("🌐", f"Opened: {self.current_url}")
    
    def visit_url(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("⚠️", "Enter URL!")
            return
        
        if not url.startswith(('http://', 'https://')):
            url = "https://" + url
        
        self.back_stack.append(self.current_url)
        self.current_url = url
        self.visit_counts[url] += 1
        self.stats["visits"] += 1
        
        self.visit_label.config(text=f"Total Visits: {self.stats['visits']}")
        self.url_entry.delete(0, tk.END)
        self.update_display()
    
    def open_browser(self):
        url = self.url_entry.get().strip()
        if not url: return
        if not url.startswith(('http://', 'https://')):
            url = "https://" + url
        webbrowser.open(url)
        self.visit_url()
    
    def go_back(self):
        if self.back_stack:
            self.forward_stack.appendleft(self.current_url)
            self.current_url = self.back_stack.pop()
            self.stats["back"] += 1
            self.back_label.config(text=f"Back: {self.stats['back']}")
            self.forward_label.config(text=f"Forward: {len(self.forward_stack)}")
        else:
            messagebox.showinfo("ℹ️", "No previous pages!")
        self.update_display()
    
    def go_forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current_url)
            self.current_url = self.forward_stack.popleft()
            self.stats["forward"] += 1
            self.back_label.config(text=f"Back: {len(self.back_stack)}")
            self.forward_label.config(text=f"Forward: {self.stats['forward']}")
        else:
            messagebox.showinfo("ℹ️", "No forward pages!")
        self.update_display()
    
    def go_home(self):
        self.back_stack.clear()
        self.forward_stack.clear()
        self.current_url = "https://google.com"
        self.visit_counts = Counter({"https://google.com": 1})
        self.stats = {"visits": 1, "back": 0, "forward": 0}
        self.visit_label.config(text="Total Visits: 1")
        self.back_label.config(text="Back: 0")
        self.forward_label.config(text="Forward: 0")
        self.url_entry.delete(0, tk.END)
        self.update_display()
    
    def save_report(self):
        """✅ PERFECT REPORT - NO ERRORS!"""
        try:
            sorted_counts = self.visit_counts.most_common()
            
            html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>DSA Lab Report - Browser History</title>
    <style>
        body { font-family: Arial, sans-serif; background: linear-gradient(to bottom, lightblue, white); margin: 0; padding: 30px; }
        .header { background: linear-gradient(45deg, navy, darkblue); color: white; padding: 30px; border-radius: 15px; text-align: center; margin-bottom: 30px; box-shadow: 0 8px 20px rgba(0,0,0,0.3); }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
        th, td { border: 2px solid #4682b4; padding: 15px; text-align: left; }
        th { background: linear-gradient(45deg, #4682b4, #1e3a8a); color: white; font-weight: bold; font-size: 16px; }
        .current { background: #add8e6 !important; font-weight: bold; font-size: 18px; }
        .back-stack { background: #ffffe0 !important; }
        .forward-stack { background: #ffcccc !important; }
        h2 { color: navy; margin-top: 30px; }
        h3 { color: #1e3a8a; border-bottom: 3px solid #4682b4; padding-bottom: 10px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🎓 DSA Lab: Browser History Analysis Report</h1>
        <p>Generated: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S IST') + """</p>
    </div>
"""
            
            html_content += f"""
    <h2>📱 Current Page</h2>
    <table>
        <tr><th>Current URL</th><td class="current">{self.current_url}</td></tr>
    </table>
    
    <h3>🔢 Visit Counts (Top 15)</h3>
    <table>
        <tr><th>Rank</th><th>URL</th><th>Visit Count</th></tr>
"""
            
            for i, (url, count) in enumerate(sorted_counts[:15], 1):
                html_content += f"        <tr><td>{i}</td><td>{url}</td><td><strong>{count}</strong></td></tr>\n"
            
            html_content += f"""
    </table>
    
    <h3>⬅️ Back Stack (Previous Pages)</h3>
    <table class="back-stack">
        <tr><th>Back Stack Contents</th><td>""" + str(list(self.back_stack)) + """</td></tr>
    </table>
    
    <h3>➡️ Forward Stack (Next Pages)</h3>
    <table class="forward-stack">
        <tr><th>Forward Stack Contents</th><td>""" + str(list(self.forward_stack)) + """</td></tr>
    </table>
    
    <h3>📊 Operation Statistics</h3>
    <table>
        <tr><th>Total Visits</th><td><strong>{self.stats['visits']}</strong></td></tr>
        <tr><th>Back Operations</th><td><strong>{self.stats['back']}</strong></td></tr>
        <tr><th>Forward Operations</th><td><strong>{self.stats['forward']}</strong></td></tr>
    </table>
    
    <div style="background: #e8f4f8; padding: 20px; border-radius: 10px; margin-top: 30px; border-left: 5px solid #4682b4;">
        <h3>✅ Data Structure Analysis</h3>
        <p><strong>Stack Implementation:</strong> LIFO (Last In First Out)</p>
        <p><strong>Time Complexity:</strong> O(1) for push/pop operations</p>
        <p><strong>Space Complexity:</strong> O(n) where n = number of pages</p>
    </div>
</body>
</html>"""
            
            filename = "DSA_Report.html"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            # ✅ SAFE BROWSER OPEN
            full_path = os.path.abspath(filename).replace('\\', '/')
            webbrowser.open(f'file:///{full_path}')
            
            messagebox.showinfo("✅ SUCCESS", f"✨ Report created!\n📁 DSA_Report.html\n\nBeautiful HTML opened in browser!")
            
        except Exception as e:
            messagebox.showerror("❌ Error", f"Report failed!\nError: {str(e)}")
    
    def update_display(self):
        count = self.visit_counts[self.current_url]
        self.current_label.config(text=f"📱 {self.current_url}\n({count} visits)")
        
        # Counts
        self.count_text.delete(1.0, tk.END)
        for i, (url, cnt) in enumerate(self.visit_counts.most_common(12), 1):
            self.count_text.insert(tk.END, f"{i}. {url}\n   → {cnt} visits\n")
        
        # Back stack
        self.back_text.delete(1.0, tk.END)
        if self.back_stack:
            self.back_text.insert(tk.END, f"📋 {len(self.back_stack)} pages:\n\n")
            for i, url in enumerate(reversed(self.back_stack), 1):
                self.back_text.insert(tk.END, f"{i}. {url}\n")
        else:
            self.back_text.insert(tk.END, "🚫 EMPTY")
        
        # Forward stack
        self.fwd_text.delete(1.0, tk.END)
        if self.forward_stack:
            self.fwd_text.insert(tk.END, f"✅ {len(self.forward_stack)} PAGES READY:\n\n")
            for i, url in enumerate(self.forward_stack, 1):
                self.fwd_text.insert(tk.END, f"🎯 {i}. {url}\n")
        else:
            self.fwd_text.insert(tk.END, "🚫 NO FORWARD PAGES\nClick BACK first!")
        
        # Button states
        self.back_btn.config(state='normal' if self.back_stack else 'disabled')
        self.forward_btn.config(state='normal' if self.forward_stack else 'disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = BrowserSimulator(root)
    root.mainloop()