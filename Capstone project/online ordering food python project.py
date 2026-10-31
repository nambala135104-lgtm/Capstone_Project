import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
import random

APP_TITLE = "FoodFlow — Smart Food Marketplace"
DB_NAME = "foodflow.db"

# ----------------------------- THEME -----------------------------
BG = "#F5F8F7"
WHITE = "#FFFFFF"
TEXT = "#173F3B"
MUTED = "#71827E"
TEAL = "#0F766E"
DARK = "#115E59"
LIGHT = "#DFF7F3"
GREEN = "#16A34A"
RED = "#DC2626"
ORANGE = "#D97706"
BORDER = "#D9E7E4"

FONT = "Segoe UI"
EMOJI_FONT = "Segoe UI Emoji"

# ----------------------------- DATA -----------------------------
RESTAURANTS = [
    ("Spice Route", "Biryani, North Indian", 4.7, 28, "🍛", "₹₹"),
    ("Pizza Planet", "Pizza, Italian", 4.5, 30, "🍕", "₹₹"),
    ("Burger Barn", "Burgers, Fast Food", 4.4, 24, "🍔", "₹"),
    ("Wok Street", "Chinese, Asian", 4.6, 27, "🍜", "₹₹"),
    ("South Bowl", "South Indian, Breakfast", 4.8, 22, "🥞", "₹"),
    ("Sweet Cloud", "Desserts, Shakes", 4.6, 20, "🍰", "₹"),
]

FOODS = [
    # restaurant, category, subcategory, name, price, rating, time, emoji, bestseller
    ("Spice Route","Biryani","Veg","Veg Dum Biryani",219,4.6,30,"🍚",1),
    ("Spice Route","Biryani","Veg","Paneer Biryani",249,4.7,30,"🍚",1),
    ("Spice Route","Biryani","Veg","Mushroom Biryani",239,4.5,30,"🍄",0),
    ("Spice Route","Biryani","Veg","Veg Hyderabadi Biryani",229,4.6,32,"🍚",0),
    ("Spice Route","Biryani","Non-Veg","Chicken Dum Biryani",299,4.8,32,"🍗",1),
    ("Spice Route","Biryani","Non-Veg","Chicken Fry Piece Biryani",329,4.8,34,"🍗",1),
    ("Spice Route","Biryani","Non-Veg","Chicken 65 Biryani",319,4.7,34,"🍗",0),
    ("Spice Route","Biryani","Non-Veg","Mutton Biryani",399,4.9,38,"🍖",1),
    ("Spice Route","Biryani","Non-Veg","Prawns Biryani",429,4.7,40,"🍤",0),
    ("Pizza Planet","Pizza","Veg","Margherita Pizza",249,4.5,25,"🍕",1),
    ("Pizza Planet","Pizza","Veg","Farmhouse Pizza",349,4.7,30,"🍕",1),
    ("Pizza Planet","Pizza","Veg","Paneer Tikka Pizza",379,4.8,32,"🍕",1),
    ("Pizza Planet","Pizza","Veg","Corn & Cheese Pizza",299,4.4,28,"🌽",0),
    ("Pizza Planet","Pizza","Non-Veg","Chicken Pepperoni Pizza",449,4.8,32,"🍕",1),
    ("Pizza Planet","Pizza","Non-Veg","BBQ Chicken Pizza",429,4.7,32,"🍕",0),
    ("Pizza Planet","Pizza","Veg","Cheesy Garlic Pizza",279,4.5,27,"🍕",0),
    ("Pizza Planet","Pizza","Veg","Mexican Fiesta Pizza",369,4.7,31,"🍕",1),
    ("Pizza Planet","Pizza","Non-Veg","Tandoori Chicken Pizza",459,4.8,34,"🍕",1),
    ("Pizza Planet","Pizza","Non-Veg","Chicken Supreme Pizza",499,4.8,35,"🍕",1),
    ("Burger Barn","Burgers","Veg","Classic Veg Burger",149,4.4,20,"🍔",1),
    ("Burger Barn","Burgers","Veg","Aloo Tikki Burger",129,4.3,20,"🍔",0),
    ("Burger Barn","Burgers","Veg","Paneer Crunch Burger",189,4.7,22,"🍔",1),
    ("Burger Barn","Burgers","Veg","Mushroom Cheese Burger",199,4.5,23,"🍔",0),
    ("Burger Barn","Burgers","Non-Veg","Crispy Chicken Burger",219,4.7,24,"🍔",1),
    ("Burger Barn","Burgers","Non-Veg","Double Chicken Burger",279,4.8,26,"🍔",1),
    ("Burger Barn","Burgers","Non-Veg","Chicken Cheese Burger",249,4.6,24,"🍔",0),
    ("Burger Barn","Burgers","Veg","Spicy Paneer Burger",209,4.6,23,"🍔",1),
    ("Burger Barn","Burgers","Veg","Cheese Corn Burger",179,4.4,21,"🍔",0),
    ("Burger Barn","Burgers","Non-Veg","Peri Peri Chicken Burger",239,4.7,25,"🍔",1),
    ("Burger Barn","Burgers","Non-Veg","Smoky BBQ Chicken Burger",259,4.8,26,"🍔",1),
    ("Wok Street","Chinese","Veg","Veg Hakka Noodles",189,4.5,25,"🍜",1),
    ("Wok Street","Chinese","Veg","Schezwan Noodles",209,4.6,26,"🍜",1),
    ("Wok Street","Chinese","Veg","Veg Fried Rice",179,4.4,24,"🍚",0),
    ("Wok Street","Chinese","Veg","Gobi Manchurian",169,4.5,22,"🥦",1),
    ("Wok Street","Chinese","Veg","Paneer Chilli",229,4.7,25,"🥡",0),
    ("Wok Street","Chinese","Non-Veg","Chicken Noodles",239,4.7,27,"🍜",1),
    ("Wok Street","Chinese","Non-Veg","Chicken Fried Rice",249,4.6,27,"🍚",0),
    ("Wok Street","Chinese","Non-Veg","Chicken Manchurian",269,4.7,28,"🥡",1),
    ("South Bowl","South Indian","Veg","Masala Dosa",119,4.8,18,"🥞",1),
    ("South Bowl","South Indian","Veg","Paneer Dosa",169,4.6,20,"🥞",0),
    ("South Bowl","South Indian","Veg","Idli Sambar",89,4.7,15,"🍽️",1),
    ("South Bowl","South Indian","Veg","Vada Sambar",99,4.6,16,"🍽️",0),
    ("South Bowl","South Indian","Veg","Ghee Roast Dosa",149,4.8,20,"🥞",1),
    ("Sweet Cloud","Desserts","Veg","Chocolate Brownie",139,4.6,15,"🍫",1),
    ("Sweet Cloud","Desserts","Veg","Choco Lava Cake",159,4.8,18,"🍰",1),
    ("Sweet Cloud","Desserts","Veg","Oreo Shake",179,4.7,15,"🥤",1),
    ("Sweet Cloud","Desserts","Veg","Cold Coffee",129,4.5,12,"🥤",0),
    ("Sweet Cloud","Desserts","Veg","Mango Shake",149,4.5,12,"🥭",0),
]

CATEGORIES = ["All","Biryani","Pizza","Burgers","Chinese","South Indian","Desserts"]
COUPONS = {
    "WELCOME50": ("₹50 off above ₹399", 50, 399),
    "FOOD10": ("10% off above ₹499", 0.10, 499),
    "SMART100": ("₹100 off above ₹799", 100, 799),
}

# ----------------------------- DATABASE -----------------------------
class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.conn.row_factory = sqlite3.Row
        self.create()
        self.seed()

    def create(self):
        c = self.conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL,
            address TEXT DEFAULT '',
            created_at TEXT NOT NULL)""")
        c.execute("""CREATE TABLE IF NOT EXISTS favorites(
            user_id INTEGER,
            food_id INTEGER,
            UNIQUE(user_id, food_id))""")
        c.execute("""CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            order_code TEXT,
            restaurant TEXT,
            items TEXT,
            subtotal INTEGER,
            delivery INTEGER,
            discount INTEGER,
            total INTEGER,
            address TEXT,
            payment TEXT,
            status INTEGER,
            created_at TEXT)""")
        c.execute("""CREATE TABLE IF NOT EXISTS foods(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            restaurant TEXT, category TEXT, subcategory TEXT,
            name TEXT, price INTEGER, rating REAL, eta INTEGER,
            emoji TEXT, bestseller INTEGER)""")
        c.execute("""CREATE TABLE IF NOT EXISTS restaurants(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE, cuisines TEXT, rating REAL,
            eta INTEGER, emoji TEXT, price_range TEXT)""")
        self.conn.commit()

    def seed(self):
        c = self.conn.cursor()
        if c.execute("SELECT COUNT(*) FROM foods").fetchone()[0] == 0:
            c.executemany("""INSERT INTO foods
                (restaurant,category,subcategory,name,price,rating,eta,emoji,bestseller)
                VALUES (?,?,?,?,?,?,?,?,?)""", FOODS)
        if c.execute("SELECT COUNT(*) FROM restaurants").fetchone()[0] == 0:
            c.executemany("""INSERT INTO restaurants
                (name,cuisines,rating,eta,emoji,price_range)
                VALUES (?,?,?,?,?,?)""", RESTAURANTS)
        self.conn.commit()

    def user(self, name, phone, address=""):
        row = self.conn.execute("SELECT * FROM users WHERE phone=?", (phone,)).fetchone()
        if row:
            self.conn.execute("UPDATE users SET name=?, address=? WHERE phone=?",
                              (name, address, phone))
            self.conn.commit()
            return self.conn.execute("SELECT * FROM users WHERE phone=?", (phone,)).fetchone()
        self.conn.execute("INSERT INTO users(name,phone,address,created_at) VALUES(?,?,?,?)",
                          (name,phone,address,datetime.now().isoformat(timespec="seconds")))
        self.conn.commit()
        return self.conn.execute("SELECT * FROM users WHERE phone=?", (phone,)).fetchone()

    def favorites(self, uid):
        return {r["food_id"] for r in self.conn.execute(
            "SELECT food_id FROM favorites WHERE user_id=?", (uid,)).fetchall()}

    def toggle_favorite(self, uid, fid):
        exists = self.conn.execute(
            "SELECT 1 FROM favorites WHERE user_id=? AND food_id=?", (uid,fid)).fetchone()
        if exists:
            self.conn.execute("DELETE FROM favorites WHERE user_id=? AND food_id=?", (uid,fid))
        else:
            self.conn.execute("INSERT OR IGNORE INTO favorites(user_id,food_id) VALUES(?,?)",(uid,fid))
        self.conn.commit()

    def add_order(self, data):
        self.conn.execute("""INSERT INTO orders
            (user_id,order_code,restaurant,items,subtotal,delivery,discount,total,address,payment,status,created_at)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",
            (data["user_id"],data["code"],data["restaurant"],data["items"],data["subtotal"],
             data["delivery"],data["discount"],data["total"],data["address"],data["payment"],0,
             datetime.now().isoformat(timespec="seconds")))
        self.conn.commit()

    def orders(self, uid):
        return self.conn.execute(
            "SELECT * FROM orders WHERE user_id=? ORDER BY id DESC",(uid,)).fetchall()

    def close(self):
        self.conn.close()

# ----------------------------- APP -----------------------------
class FoodFlow:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("1280x820")
        self.root.minsize(1100,720)
        self.root.configure(bg=BG)
        self.db = Database()

        self.user = None
        self.cart = {}                 # food_id -> quantity
        self.favorites = set()
        self.restaurant_filter = None
        self.category_filter = "All"
        self.search = ""
        self.type_filter = "All"
        self.coupon = None
        self.order = None
        self.current_page = "login"
        self.service_windows = [
            ("Morning", "7:00 AM – 11:00 AM", "Fresh breakfast & early orders", "🌅"),
            ("Afternoon", "11:00 AM – 4:00 PM", "Lunch favourites & quick delivery", "☀️"),
            ("Evening", "4:00 PM – 9:00 PM", "Snacks, burgers & dinner", "🌇"),
            ("Late Night", "9:00 PM – 1:00 AM", "Late-night delivery • +₹40 service fee", "🌙"),
        ]
        self.banner_index = 0
        self.banners = [
            ("SMART MONDAY","Flat ₹100 OFF on orders above ₹799","SMART100"),
            ("WELCOME OFFER","₹50 OFF on your first smart order","WELCOME50"),
            ("FOOD FEST","10% OFF on big baskets above ₹499","FOOD10"),
            ("DINNER DEAL","Hot meals, smart prices & fast delivery","")
        ]
        self.statuses = [
            ("Order Placed","Restaurant received your order.","🧾"),
            ("Preparing","Chef is preparing your food.","👨‍🍳"),
            ("Packed","Your order is packed safely.","📦"),
            ("Rider Assigned","A delivery partner has picked it up.","🛵"),
            ("On the Way","Your food is travelling to you.","🚚"),
            ("Delivered","Enjoy your meal!","✓")
        ]

        self.build_header()
        self.show_login()
        self.animate_banner()

    # ----------------------------- COMMON -----------------------------
    def clear(self):
        for w in self.body.winfo_children():
            w.destroy()
        if hasattr(self,"body_canvas"):
            self.body_canvas.yview_moveto(0)

    def button(self,p,text,cmd,bg=TEAL,fg=WHITE,width=14):
        return tk.Button(p,text=text,command=cmd,bg=bg,fg=fg,
            activebackground=DARK,activeforeground=WHITE,relief="flat",bd=0,
            cursor="hand2",font=(FONT,10,"bold"),width=width,pady=8)

    def card(self,p):
        return tk.Frame(p,bg=WHITE,highlightbackground=BORDER,highlightthickness=1)

    def title(self,heading,sub=""):
        box=tk.Frame(self.body,bg=BG); box.pack(fill="x",padx=42,pady=(24,10))
        tk.Label(box,text=heading,bg=BG,fg=TEXT,font=(FONT,25,"bold")).pack(anchor="w")
        if sub: tk.Label(box,text=sub,bg=BG,fg=MUTED,font=(FONT,10)).pack(anchor="w",pady=(3,0))

    def money(self,n): return f"₹{int(round(n))}"

    def current_service_window(self):
        hour=datetime.now().hour
        if 7 <= hour < 11: return self.service_windows[0]
        if 11 <= hour < 16: return self.service_windows[1]
        if 16 <= hour < 21: return self.service_windows[2]
        if hour >= 21 or hour < 1: return self.service_windows[3]
        return ("Closed", "1:00 AM – 7:00 AM", "Ordering is available in demo mode; scheduled delivery starts at 7 AM", "🌙")

    def is_late_night(self):
        hour=datetime.now().hour
        return hour >= 21 or hour < 1

    def delivery_charges(self,subtotal):
        base=0 if subtotal>=499 else 35
        late=40 if self.is_late_night() else 0
        return base,late


    # ----------------------------- HEADER -----------------------------
    def build_header(self):
        self.header=tk.Frame(self.root,bg=WHITE,height=72,highlightbackground=BORDER,highlightthickness=1)
        self.header.pack(fill="x"); self.header.pack_propagate(False)
        logo=tk.Frame(self.header,bg=WHITE,cursor="hand2"); logo.pack(side="left",padx=28)
        logo.bind("<Button-1>",lambda e:self.show_home())
        tk.Label(logo,text="Food",bg=WHITE,fg=DARK,font=(FONT,21,"bold")).pack(side="left")
        tk.Label(logo,text="Flow",bg=WHITE,fg=TEAL,font=(FONT,21,"bold")).pack(side="left")
        tk.Label(logo,text="  •  SMART FOOD MARKETPLACE",bg=WHITE,fg=MUTED,
                 font=(FONT,8,"bold")).pack(side="left",padx=8)
        self.nav=tk.Frame(self.header,bg=WHITE); self.nav.pack(side="right",padx=18)
        self.refresh_nav()

        # Scrollable content area: every page can now scroll vertically.
        self.body_canvas=tk.Canvas(self.root,bg=BG,highlightthickness=0,bd=0)
        self.body_canvas.pack(fill="both",expand=True)
        self.body=tk.Frame(self.body_canvas,bg=BG)
        self.body_window=self.body_canvas.create_window((0,0),window=self.body,anchor="nw")
        self.body.bind("<Configure>",lambda e:self.body_canvas.configure(scrollregion=self.body_canvas.bbox("all")))
        self.body_canvas.bind("<Configure>",lambda e:self.body_canvas.itemconfigure(self.body_window,width=e.width))
        self.root.bind_all("<MouseWheel>",self._on_mousewheel)
        self.root.bind_all("<Button-4>",lambda e:self.body_canvas.yview_scroll(-3,"units"))
        self.root.bind_all("<Button-5>",lambda e:self.body_canvas.yview_scroll(3,"units"))

    def _on_mousewheel(self,event):
        if self.body_canvas.winfo_exists():
            self.body_canvas.yview_scroll(int(-1*(event.delta/120)),"units")

    def refresh_nav(self):
        for w in self.nav.winfo_children(): w.destroy()
        if not self.user: return
        for text,cmd in [
            ("Home",self.show_home),("Restaurants",self.show_restaurants),
            ("Menu",self.show_menu),("❤️ Favorites",self.show_favorites),
            ("🛒 Cart",self.show_cart),("Orders",self.show_orders)
        ]:
            tk.Button(self.nav,text=text,command=cmd,bg=WHITE,fg=TEXT,
                      activebackground=LIGHT,relief="flat",bd=0,cursor="hand2",
                      font=(FONT,9,"bold"),padx=9,pady=9).pack(side="left")
        tk.Button(self.nav,text=f"Hi, {self.user['name'].split()[0]}",
                  command=self.show_profile,bg=TEAL,fg=WHITE,relief="flat",bd=0,
                  cursor="hand2",font=(FONT,9,"bold"),padx=12,pady=8).pack(side="left",padx=(8,0))

    # ----------------------------- LOGIN -----------------------------
    def show_login(self):
        self.current_page = "login"
        self.clear()
        box=tk.Frame(self.body,bg=BG); box.pack(fill="both",expand=True,pady=40)
        panel=self.card(box); panel.pack(padx=20,pady=35,ipady=10)
        panel.config(width=500,height=535); panel.pack_propagate(False)
        tk.Label(panel,text="🍽️",bg=WHITE,font=(EMOJI_FONT,42)).pack(pady=(35,8))
        tk.Label(panel,text="Welcome to FoodFlow",bg=WHITE,fg=TEXT,font=(FONT,23,"bold")).pack()
        tk.Label(panel,text="A smarter marketplace for food, offers and delivery.",
                 bg=WHITE,fg=MUTED,font=(FONT,9)).pack(pady=(5,22))
        tk.Label(panel,text="Your Name",bg=WHITE,fg=MUTED,font=(FONT,9,"bold")).pack(anchor="w",padx=42)
        name=tk.Entry(panel,font=(FONT,11),relief="solid",bd=1); name.pack(fill="x",padx=42,ipady=8,pady=(4,12))
        tk.Label(panel,text="Mobile Number",bg=WHITE,fg=MUTED,font=(FONT,9,"bold")).pack(anchor="w",padx=42)
        phone=tk.Entry(panel,font=(FONT,11),relief="solid",bd=1); phone.pack(fill="x",padx=42,ipady=8,pady=(4,8))
        tk.Label(panel,text="📍 Delivery address is requested securely at checkout.",
                 bg=WHITE,fg=TEAL,font=(FONT,8,"bold")).pack(anchor="w",padx=42,pady=(2,18))
        def login():
            n=name.get().strip(); p="".join(x for x in phone.get() if x.isdigit())
            if not n or len(p)!=10:
                messagebox.showwarning("Check details","Enter your name and a valid 10-digit mobile number.")
                return
            # Login never pre-fills delivery address. Address belongs to the current checkout.
            # The mobile number identifies the existing account, but its saved address is not
            # loaded into checkout automatically.
            existing=self.db.conn.execute("SELECT * FROM users WHERE phone=?",(p,)).fetchone()
            if existing:
                self.user=existing
                if existing["name"] != n:
                    self.db.conn.execute("UPDATE users SET name=? WHERE phone=?",(n,p))
                    self.db.conn.commit()
                    self.user=self.db.conn.execute("SELECT * FROM users WHERE phone=?",(p,)).fetchone()
            else:
                self.user=self.db.user(n,p,"")
            self.favorites=self.db.favorites(self.user["id"])
            self.refresh_nav(); self.show_home()
        self.button(panel,"ENTER FOODFLOW  →",login,width=27).pack(pady=(0,5))
        tk.Label(panel,text="Demo project • Personal data is stored locally in SQLite",
                 bg=WHITE,fg=MUTED,font=(FONT,8)).pack(pady=15)

    # ----------------------------- HOME -----------------------------
    def show_home(self):
        if not self.user: return self.show_login()
        self.current_page = "home"
        self.clear()
        # banner
        self.banner=tk.Frame(self.body,bg=DARK,height=190); self.banner.pack(fill="x",padx=34,pady=(22,15)); self.banner.pack_propagate(False)
        self.render_banner()
        # search
        s=tk.Frame(self.body,bg=BG); s.pack(fill="x",padx=42)
        entrybox=tk.Frame(s,bg=WHITE,highlightbackground=BORDER,highlightthickness=1); entrybox.pack(fill="x")
        tk.Label(entrybox,text="🔎",bg=WHITE,font=(EMOJI_FONT,14)).pack(side="left",padx=12)
        e=tk.Entry(entrybox,bg=WHITE,fg=TEXT,relief="flat",bd=0,font=(FONT,11))
        e.insert(0,"Search biryani, pizza, burger, restaurant..."); e.config(fg=MUTED)
        e.pack(side="left",fill="x",expand=True,ipady=10)
        def focus(_):
            if e.get().startswith("Search biryani"):
                e.delete(0,"end"); e.config(fg=TEXT)
        e.bind("<FocusIn>",focus)
        e.bind("<Return>",lambda _:self.do_search(e.get()))
        self.button(entrybox,"Search",lambda:self.do_search(e.get()),width=10).pack(side="right",padx=5,pady=5)

        # quick categories
        tk.Label(self.body,text="What are you craving?",bg=BG,fg=TEXT,font=(FONT,18,"bold")).pack(anchor="w",padx=42,pady=(18,8))
        row=tk.Frame(self.body,bg=BG); row.pack(fill="x",padx=38)
        for c,icon in [("Biryani","🍚"),("Pizza","🍕"),("Burgers","🍔"),("Chinese","🍜"),("South Indian","🥞"),("Desserts","🍰")]:
            b=self.card(row); b.pack(side="left",fill="x",expand=True,padx=4)
            tk.Label(b,text=icon,bg=LIGHT,font=(EMOJI_FONT,25),width=3).pack(side="left",padx=8,pady=8)
            tk.Label(b,text=c,bg=WHITE,fg=TEXT,font=(FONT,9,"bold")).pack(side="left")
            for w in b.winfo_children(): w.bind("<Button-1>",lambda e,x=c:self.category_open(x))
            b.bind("<Button-1>",lambda e,x=c:self.category_open(x))

        # Delivery timings
        tk.Label(self.body,text="⏰ Delivery Hours & Smart Fees",bg=BG,fg=TEXT,font=(FONT,18,"bold")).pack(anchor="w",padx=42,pady=(20,8))
        timing_row=tk.Frame(self.body,bg=BG); timing_row.pack(fill="x",padx=38)
        current=self.current_service_window()[0]
        for title,window,desc,icon in self.service_windows:
            active=title==current
            b=self.card(timing_row); b.pack(side="left",fill="both",expand=True,padx=4)
            top=tk.Frame(b,bg=TEAL if active else LIGHT); top.pack(fill="x")
            tk.Label(top,text=icon,bg=top.cget("bg"),fg=WHITE if active else TEXT,font=(EMOJI_FONT,18)).pack(side="left",padx=8,pady=6)
            tk.Label(top,text=title + (" • NOW" if active else ""),bg=top.cget("bg"),fg=WHITE if active else TEXT,font=(FONT,9,"bold")).pack(side="left")
            tk.Label(b,text=window,bg=WHITE,fg=TEXT,font=(FONT,9,"bold")).pack(anchor="w",padx=10,pady=(8,2))
            tk.Label(b,text=desc,bg=WHITE,fg=MUTED,font=(FONT,8),wraplength=210,justify="left").pack(anchor="w",padx=10,pady=(0,9))

        tk.Label(self.body,text="🔥 Best Sellers",bg=BG,fg=TEXT,font=(FONT,18,"bold")).pack(anchor="w",padx=42,pady=(20,8))
        self.food_row(self.body,[r for r in self.db.conn.execute("SELECT * FROM foods WHERE bestseller=1 ORDER BY rating DESC LIMIT 5")])

    def render_banner(self):
        for w in self.banner.winfo_children(): w.destroy()
        title,desc,coupon=self.banners[self.banner_index]
        left=tk.Frame(self.banner,bg=DARK); left.pack(side="left",fill="both",expand=True,padx=32,pady=24)
        tk.Label(left,text=title,bg=DARK,fg="#B8FFF5",font=(FONT,10,"bold")).pack(anchor="w")
        tk.Label(left,text=desc,bg=DARK,fg=WHITE,font=(FONT,25,"bold")).pack(anchor="w",pady=5)
        if coupon: self.button(left,f"Use {coupon}",lambda c=coupon:self.apply_home_coupon(c),bg=WHITE,fg=DARK,width=15).pack(anchor="w",pady=8)
        tk.Label(self.banner,text="🍕  🍔\n🍚  🥤",bg=DARK,fg=WHITE,font=(EMOJI_FONT,36)).pack(side="right",padx=55)

    def animate_banner(self):
        if hasattr(self,"banner") and self.banner.winfo_exists():
            self.banner_index=(self.banner_index+1)%len(self.banners)
            self.render_banner()
        self.root.after(3500,self.animate_banner)

    def apply_home_coupon(self,c):
        self.coupon=c; self.show_cart()

    def do_search(self,q):
        q=q.strip()
        if q.startswith("Search biryani"): q=""
        self.search=q
        self.restaurant_filter=None
        self.category_filter="All"
        self.show_menu()

    def category_open(self,c):
        self.category_filter=c; self.restaurant_filter=None; self.search=""; self.show_menu()

    # ----------------------------- RESTAURANTS -----------------------------
    def show_restaurants(self):
        self.clear(); self.title("Discover Restaurants","Choose a restaurant to explore its complete menu.")
        top=tk.Frame(self.body,bg=BG); top.pack(fill="x",padx=42,pady=3)
        tk.Label(top,text="Popular near you",bg=BG,fg=MUTED,font=(FONT,10,"bold")).pack(side="left")
        grid=tk.Frame(self.body,bg=BG); grid.pack(fill="both",expand=True,padx=38,pady=8)
        for i,r in enumerate(self.db.conn.execute("SELECT * FROM restaurants ORDER BY rating DESC")):
            box=self.card(grid); box.grid(row=i//3,column=i%3,padx=7,pady=7,sticky="nsew")
            tk.Label(box,text=r["emoji"],bg=LIGHT,font=(EMOJI_FONT,35),width=4).pack(side="left",padx=12,pady=18)
            info=tk.Frame(box,bg=WHITE); info.pack(side="left",fill="both",expand=True,pady=15)
            tk.Label(info,text=r["name"],bg=WHITE,fg=TEXT,font=(FONT,13,"bold")).pack(anchor="w")
            tk.Label(info,text=r["cuisines"],bg=WHITE,fg=MUTED,font=(FONT,8)).pack(anchor="w",pady=3)
            tk.Label(info,text=f"⭐ {r['rating']}   •   {r['eta']} min   •   {r['price_range']}",
                     bg=WHITE,fg=DARK,font=(FONT,9,"bold")).pack(anchor="w")
            self.button(info,"View Menu →",lambda n=r["name"]:self.open_restaurant(n),width=13).pack(anchor="w",pady=8)
        for c in range(3): grid.grid_columnconfigure(c,weight=1)

    def open_restaurant(self,name):
        self.restaurant_filter=name; self.category_filter="All"; self.search=""; self.show_menu()

    # ----------------------------- MENU -----------------------------
    def show_menu(self):
        self.current_page = "menu"
        self.clear(); self.title("Explore Food","Filter by category, type, restaurant or search any dish.")
        bar=tk.Frame(self.body,bg=BG); bar.pack(fill="x",padx=40,pady=(0,8))
        se=tk.Entry(bar,font=(FONT,10),relief="solid",bd=1); se.insert(0,self.search)
        se.pack(side="left",fill="x",expand=True,ipady=8)
        self.button(bar,"Search",lambda:self.menu_search(se.get()),width=9).pack(side="left",padx=5)
        self.button(bar,"Clear",lambda:self.clear_filters(),bg="#E8F2F0",fg=DARK,width=8).pack(side="left")
        # filters
        filt=tk.Frame(self.body,bg=WHITE,highlightbackground=BORDER,highlightthickness=1); filt.pack(fill="x",padx=40,pady=4)
        tk.Label(filt,text="Categories:",bg=WHITE,fg=MUTED,font=(FONT,9,"bold")).pack(side="left",padx=12)
        for c in CATEGORIES:
            self.button(filt,c,lambda x=c:self.set_category(x),
                        bg=TEAL if c==self.category_filter else WHITE,
                        fg=WHITE if c==self.category_filter else TEXT,width=11).pack(side="left",padx=2,pady=5)
        tk.Label(filt,text="Type:",bg=WHITE,fg=MUTED,font=(FONT,9,"bold")).pack(side="left",padx=(16,4))
        for c in ["All","Veg","Non-Veg"]:
            self.button(filt,c,lambda x=c:self.set_type(x),bg=WHITE,fg=TEXT,width=9).pack(side="left",padx=2)
        self.render_menu()

    def menu_search(self,q):
        self.search=q.strip(); self.render_menu()

    def set_category(self,c): self.category_filter=c; self.render_menu()
    def set_type(self,c): self.type_filter=c; self.render_menu()
    def clear_filters(self):
        self.search=""; self.category_filter="All"; self.restaurant_filter=None; self.type_filter="All"; self.show_menu()

    def render_menu(self):
        for w in self.body.winfo_children()[3:]: w.destroy()
        self.type_filter=getattr(self,"type_filter","All")
        query=self.search.lower()
        sql="SELECT * FROM foods WHERE 1=1"; args=[]
        if self.category_filter!="All": sql+=" AND category=?"; args.append(self.category_filter)
        if self.restaurant_filter: sql+=" AND restaurant=?"; args.append(self.restaurant_filter)
        if self.type_filter!="All": sql+=" AND subcategory=?"; args.append(self.type_filter)
        if query:
            sql+=" AND (LOWER(name) LIKE ? OR LOWER(category) LIKE ? OR LOWER(restaurant) LIKE ?)"
            q=f"%{query}%"; args += [q,q,q]
        rows=self.db.conn.execute(sql+" ORDER BY bestseller DESC,rating DESC",args).fetchall()
        info=tk.Frame(self.body,bg=BG); info.pack(fill="x",padx=42,pady=(8,2))
        label=f"{len(rows)} dishes"
        if self.restaurant_filter: label+=f" • {self.restaurant_filter}"
        tk.Label(info,text=label,bg=BG,fg=MUTED,font=(FONT,9,"bold")).pack(side="left")
        tk.Label(info,text="Tap a dish to add it to cart",bg=BG,fg=TEAL,font=(FONT,9,"bold")).pack(side="right")
        self.food_grid=tk.Frame(self.body,bg=BG); self.food_grid.pack(fill="both",expand=True,padx=38,pady=4)
        for i,r in enumerate(rows):
            self.food_card(self.food_grid,r,i//4,i%4)
        for c in range(4): self.food_grid.grid_columnconfigure(c,weight=1)

    def food_card(self,parent,r,row,col):
        box=self.card(parent); box.grid(row=row,column=col,padx=6,pady=6,sticky="nsew")
        top=tk.Frame(box,bg=LIGHT,height=85); top.pack(fill="x"); top.pack_propagate(False)
        tk.Label(top,text=r["emoji"],bg=LIGHT,font=(EMOJI_FONT,36)).pack(side="left",padx=15)
        if r["bestseller"]: tk.Label(top,text="BEST",bg=ORANGE,fg=WHITE,font=(FONT,7,"bold")).pack(side="right",padx=8,pady=8)
        tk.Label(box,text=r["name"],bg=WHITE,fg=TEXT,font=(FONT,11,"bold"),wraplength=200,justify="left").pack(anchor="w",padx=13,pady=(10,2))
        tk.Label(box,text=f"{r['restaurant']}  •  {r['subcategory']}",bg=WHITE,fg=MUTED,font=(FONT,8)).pack(anchor="w",padx=13)
        tk.Label(box,text=f"⭐ {r['rating']}   •   {r['eta']} min",bg=WHITE,fg=DARK,font=(FONT,8,"bold")).pack(anchor="w",padx=13,pady=4)
        bottom=tk.Frame(box,bg=WHITE); bottom.pack(fill="x",padx=13,pady=(2,12))
        tk.Label(bottom,text=self.money(r["price"]),bg=WHITE,fg=TEXT,font=(FONT,12,"bold")).pack(side="left")
        fav="♥" if r["id"] in self.favorites else "♡"
        tk.Button(bottom,text=fav,command=lambda x=r:self.toggle_fav(x),bg=WHITE,fg=RED,relief="flat",bd=0,font=(FONT,16),cursor="hand2").pack(side="right")
        self.button(bottom,"ADD +",lambda x=r:self.add(x),width=8).pack(side="right",padx=5)

    def food_row(self,parent,rows):
        row=tk.Frame(parent,bg=BG); row.pack(fill="x",padx=38)
        for r in rows:
            self.food_card(row,r,0,len(row.winfo_children()))
        # prevent excessive width
        for c in range(len(rows)): row.grid_columnconfigure(c,weight=1)

    def add(self,r):
        self.cart[r["id"]]=self.cart.get(r["id"],0)+1
        self.show_menu()

    def toggle_fav(self,r):
        # Toggle only this dish for the logged-in customer.
        self.db.toggle_favorite(self.user["id"], r["id"])
        self.favorites = self.db.favorites(self.user["id"])

        # If the user is viewing Favorites, refresh that page immediately so the
        # removed dish disappears at once. Do not send the user to the full Menu.
        if getattr(self, "current_page", "") == "favorites":
            self.show_favorites()
        else:
            # On Menu, stay on Menu and update only the heart state.
            self.render_menu()

    # ----------------------------- FAVORITES -----------------------------
    def show_favorites(self):
        self.current_page = "favorites"
        self.clear(); self.title("Your Favorites","Your saved dishes are stored locally in SQLite.")
        rows=[]
        if self.favorites:
            ids=tuple(self.favorites)
            marks=",".join("?"*len(ids))
            rows=self.db.conn.execute(f"SELECT * FROM foods WHERE id IN ({marks})",ids).fetchall()
        if not rows:
            box=self.card(self.body); box.pack(fill="x",padx=90,pady=50,ipady=35)
            tk.Label(box,text="♡",bg=WHITE,fg=RED,font=(FONT,40)).pack()
            tk.Label(box,text="No favorites yet",bg=WHITE,fg=TEXT,font=(FONT,18,"bold")).pack()
            tk.Label(box,text="Tap the heart on any dish to save it here.",bg=WHITE,fg=MUTED,font=(FONT,9)).pack(pady=5)
            return
        grid=tk.Frame(self.body,bg=BG); grid.pack(fill="both",expand=True,padx=38)
        for i,r in enumerate(rows): self.food_card(grid,r,i//4,i%4)
        for c in range(4): grid.grid_columnconfigure(c,weight=1)

    # ----------------------------- CART -----------------------------
    def cart_data(self):
        items=[]
        for fid,qty in self.cart.items():
            r=self.db.conn.execute("SELECT * FROM foods WHERE id=?",(fid,)).fetchone()
            if r: items.append((r,qty))
        return items

    def show_cart(self):
        self.clear(); self.title("Smart Cart","Transparent delivery charges, late-night fees and coupons are shown before checkout.")
        items=self.cart_data()
        if not items:
            box=self.card(self.body); box.pack(fill="x",padx=80,pady=50,ipady=35)
            tk.Label(box,text="🛒",bg=WHITE,font=(EMOJI_FONT,42)).pack()
            tk.Label(box,text="Your cart is empty",bg=WHITE,fg=TEXT,font=(FONT,19,"bold")).pack(pady=5)
            self.button(box,"Explore Food",self.show_menu,width=18).pack(pady=12)
            return
        main=tk.Frame(self.body,bg=BG); main.pack(fill="both",expand=True,padx=42)
        left=self.card(main); left.pack(side="left",fill="both",expand=True,padx=(0,12))
        tk.Label(left,text="Your Items",bg=WHITE,fg=TEXT,font=(FONT,15,"bold")).pack(anchor="w",padx=20,pady=18)
        for r,q in items:
            row=tk.Frame(left,bg=WHITE,height=75); row.pack(fill="x",padx=15,pady=3); row.pack_propagate(False)
            tk.Label(row,text=r["emoji"],bg=LIGHT,font=(EMOJI_FONT,22),width=3).pack(side="left",padx=6,pady=7)
            inf=tk.Frame(row,bg=WHITE); inf.pack(side="left",fill="both",expand=True)
            tk.Label(inf,text=r["name"],bg=WHITE,fg=TEXT,font=(FONT,10,"bold")).pack(anchor="w",pady=(12,0))
            tk.Label(inf,text=f"{self.money(r['price'])} × {q}",bg=WHITE,fg=MUTED,font=(FONT,8)).pack(anchor="w")
            self.button(row,"+",lambda fid=r["id"]:self.change(fid,1),width=3).pack(side="right",padx=2)
            tk.Label(row,text=str(q),bg=WHITE,fg=TEXT,font=(FONT,10,"bold")).pack(side="right",padx=4)
            self.button(row,"−",lambda fid=r["id"]:self.change(fid,-1),bg="#E8F2F0",fg=DARK,width=3).pack(side="right")
            tk.Label(row,text=self.money(r["price"]*q),bg=WHITE,fg=TEXT,font=(FONT,10,"bold")).pack(side="right",padx=15)
        # Keep the bill card at its natural height so the checkout button is always visible.
        right=self.card(main); right.pack(side="right",anchor="n",padx=0); right.config(width=355); right.pack_propagate(True)
        tk.Label(right,text="Bill Summary",bg=WHITE,fg=TEXT,font=(FONT,15,"bold")).pack(anchor="w",padx=20,pady=18)
        sub=sum(r["price"]*q for r,q in items)
        delivery,late_fee=self.delivery_charges(sub)
        tk.Label(right,text=f"Food subtotal     {self.money(sub)}",bg=WHITE,fg=MUTED,font=(FONT,9)).pack(anchor="w",padx=20,pady=4)
        tk.Label(right,text=f"Delivery fee      {self.money(delivery)}",bg=WHITE,fg=MUTED,font=(FONT,9)).pack(anchor="w",padx=20,pady=4)
        if late_fee:
            tk.Label(right,text=f"Late-night fee    {self.money(late_fee)}",bg=WHITE,fg=ORANGE,font=(FONT,9,"bold")).pack(anchor="w",padx=20,pady=4)
        # ---------------- AVAILABLE OFFERS ----------------
        tk.Label(right,text="🎁 Available Offers",bg=WHITE,fg=TEXT,font=(FONT,10,"bold")).pack(anchor="w",padx=20,pady=(8,4))
        for code,(description,_,minimum) in COUPONS.items():
            offer=tk.Frame(right,bg=LIGHT,highlightbackground=BORDER,highlightthickness=1)
            offer.pack(fill="x",padx=20,pady=4)
            info=tk.Frame(offer,bg=LIGHT); info.pack(side="left",fill="x",expand=True,padx=8,pady=6)
            tk.Label(info,text=code,bg=LIGHT,fg=DARK,font=(FONT,8,"bold")).pack(anchor="w")
            tk.Label(info,text=description,bg=LIGHT,fg=MUTED,font=(FONT,7)).pack(anchor="w")
            if sub >= minimum:
                self.button(offer,"Apply",lambda c=code:self.apply_coupon(c),width=7).pack(side="right",padx=6,pady=6)
            else:
                tk.Label(offer,text=f"Min ₹{minimum}",bg=LIGHT,fg=MUTED,font=(FONT,7,"bold")).pack(side="right",padx=8)

        tk.Label(right,text="Or enter a coupon code",bg=WHITE,fg=MUTED,font=(FONT,8)).pack(anchor="w",padx=20,pady=(10,3))
        coupon_frame=tk.Frame(right,bg=WHITE); coupon_frame.pack(fill="x",padx=20,pady=(0,10))
        ce=tk.Entry(coupon_frame,font=(FONT,9),relief="solid",bd=1)
        if self.coupon:
            ce.insert(0,self.coupon)
        else:
            ce.insert(0,"Enter coupon code")
            ce.config(fg=MUTED)
            def clear_placeholder(event):
                if ce.get()=="Enter coupon code":
                    ce.delete(0,"end"); ce.config(fg=TEXT)
            ce.bind("<FocusIn>",clear_placeholder)
        ce.pack(side="left",fill="x",expand=True,ipady=6)
        self.button(coupon_frame,"Apply",lambda:self.apply_coupon(ce.get()),width=8).pack(side="left",padx=4)
        discount=self.discount(sub)
        if discount:
            tk.Label(right,text=f"Coupon discount  -{self.money(discount)}",bg=WHITE,fg=GREEN,font=(FONT,9,"bold")).pack(anchor="w",padx=20,pady=4)
        tk.Frame(right,bg=BORDER,height=1).pack(fill="x",padx=20,pady=10)
        total=max(0,sub+delivery+late_fee-discount)
        tk.Label(right,text=f"TOTAL              {self.money(total)}",bg=WHITE,fg=TEXT,font=(FONT,13,"bold")).pack(anchor="w",padx=20,pady=5)
        fee_text="🌙 Late-night service fee: ₹40 (9 PM–1 AM)" if late_fee else "🚚 Free delivery above ₹499"
        tk.Label(right,text=fee_text,bg=LIGHT,fg=DARK,font=(FONT,8,"bold"),pady=8).pack(fill="x",padx=20,pady=12)
        self.button(right,"Proceed to Checkout →",self.show_checkout,width=27).pack(pady=5)

    def change(self,fid,d):
        self.cart[fid]=self.cart.get(fid,0)+d
        if self.cart[fid]<=0: del self.cart[fid]
        self.show_cart()

    def discount(self,sub):
        if not self.coupon or self.coupon not in COUPONS: return 0
        _,val,minimum=COUPONS[self.coupon]
        if sub<minimum: return 0
        return sub*val if isinstance(val,float) else val

    def apply_coupon(self,c):
        c=c.strip().upper()
        if c=="ENTER COUPON CODE":
            messagebox.showwarning("Coupon","Please enter a coupon code or choose one from Available Offers.")
            return
        if c not in COUPONS:
            messagebox.showwarning("Coupon","Invalid coupon code. Choose one from Available Offers or check the code you entered.")
            return
        sub=sum(r["price"]*q for r,q in self.cart_data())
        if sub<COUPONS[c][2]:
            messagebox.showwarning("Coupon",f"This coupon needs a minimum order of ₹{COUPONS[c][2]}.")
            return
        self.coupon=c; self.show_cart()

    # ----------------------------- CHECKOUT -----------------------------
    def show_checkout(self):
        items=self.cart_data()
        if not items: return self.show_cart()
        self.clear(); self.title("Checkout","Confirm address and payment before placing the order.")
        sub=sum(r["price"]*q for r,q in items); delivery,late_fee=self.delivery_charges(sub); disc=self.discount(sub); total=sub+delivery+late_fee-disc
        main=tk.Frame(self.body,bg=BG); main.pack(fill="both",expand=True,padx=45)
        left=self.card(main); left.pack(side="left",fill="both",expand=True,padx=(0,12))
        tk.Label(left,text="Delivery Details",bg=WHITE,fg=TEXT,font=(FONT,15,"bold")).pack(anchor="w",padx=22,pady=20)
        entries={}
        # Delivery address is intentionally blank on every fresh checkout.
        # It is only stored after the customer explicitly enters it and places the order.
        for label,key,value in [("Name","name",self.user["name"]),("Mobile","phone",self.user["phone"]),("Address","address","")]:
            tk.Label(left,text=label,bg=WHITE,fg=MUTED,font=(FONT,8,"bold")).pack(anchor="w",padx=22)
            e=tk.Entry(left,font=(FONT,10),relief="solid",bd=1); e.insert(0,value); e.pack(fill="x",padx=22,ipady=7,pady=(3,12)); entries[key]=e
        tk.Label(left,text="Payment",bg=WHITE,fg=MUTED,font=(FONT,8,"bold")).pack(anchor="w",padx=22)
        payment=tk.StringVar(value="Cash on Delivery")
        for p in ["Cash on Delivery","UPI / Demo Payment","Card / Demo Payment"]:
            tk.Radiobutton(left,text=p,variable=payment,value=p,bg=WHITE,activebackground=WHITE,
                           selectcolor=LIGHT,fg=TEXT,font=(FONT,9)).pack(anchor="w",padx=18,pady=2)
        right=self.card(main); right.pack(side="right",fill="y"); right.config(width=350); right.pack_propagate(False)
        tk.Label(right,text="Final Bill",bg=WHITE,fg=TEXT,font=(FONT,15,"bold")).pack(anchor="w",padx=22,pady=20)
        bill_lines=[("Food subtotal",sub),("Delivery",delivery)]
        if late_fee: bill_lines.append(("Late-night fee",late_fee))
        bill_lines.append(("Discount",-disc)); bill_lines.append(("TOTAL",total))
        for l,v in bill_lines:
            tk.Label(right,text=f"{l:<17}{self.money(v)}",bg=WHITE,fg=GREEN if v<0 else TEXT,
                     font=(FONT,11,"bold" if l=="TOTAL" else "normal")).pack(anchor="w",padx=22,pady=5)
        estimate=max(r["eta"] for r,q in items) + 10
        tk.Label(right,text=f"⏱ Estimated arrival: {estimate}–{estimate+15} min",bg=LIGHT,fg=DARK,font=(FONT,9,"bold"),pady=9).pack(fill="x",padx=22,pady=10)
        tk.Label(left,text="📍 Complete delivery address is mandatory before placing the order.",bg=WHITE,fg=TEAL,font=(FONT,8,"bold")).pack(anchor="w",padx=22,pady=(0,12))
        def place():
            name=entries["name"].get().strip(); phone="".join(x for x in entries["phone"].get() if x.isdigit()); address=entries["address"].get().strip()
            if not name or len(phone)!=10 or not address:
                messagebox.showwarning("Delivery details required","Please enter your name, valid 10-digit mobile number and complete delivery address before placing the order."); return
            self.user=self.db.user(name,phone,address); self.refresh_nav()
            code="FF"+datetime.now().strftime("%y%m%d%H%M%S")+str(random.randint(10,99))
            restaurant=items[0][0]["restaurant"] if all(r["restaurant"]==items[0][0]["restaurant"] for r,q in items) else "FoodFlow Marketplace"
            desc="; ".join(f"{r['name']} x{q}" for r,q in items)
            self.order={"code":code,"total":total,"restaurant":restaurant,"status":0}
            self.db.add_order({"user_id":self.user["id"],"code":code,"restaurant":restaurant,"items":desc,
                               "subtotal":sub,"delivery":delivery+late_fee,"discount":disc,"total":total,
                               "address":address,"payment":payment.get()})
            self.cart.clear(); self.coupon=None; self.show_order_success()
        self.button(right,"PLACE ORDER  ✓",place,width=26).pack(pady=6)
        self.button(right,"Back to Cart",self.show_cart,bg="#E8F2F0",fg=DARK,width=26).pack()

    def show_order_success(self):
        self.clear()
        box=self.card(self.body); box.pack(fill="x",padx=170,pady=65,ipady=25)
        tk.Label(box,text="✓",bg=GREEN,fg=WHITE,font=(FONT,28,"bold"),width=3).pack(pady=12)
        tk.Label(box,text="Order Placed Successfully!",bg=WHITE,fg=TEXT,font=(FONT,22,"bold")).pack()
        tk.Label(box,text=f"Order ID • {self.order['code']}",bg=WHITE,fg=TEAL,font=(FONT,11,"bold")).pack(pady=8)
        tk.Label(box,text=f"{self.money(self.order['total'])}  •  Your order is being prepared",
                 bg=WHITE,fg=MUTED,font=(FONT,10)).pack()
        self.button(box,"Track Live Order →",self.show_tracking,width=20).pack(pady=18)

    # ----------------------------- TRACKING -----------------------------
    def show_tracking(self):
        self.clear()
        if not self.order:
            rows=self.db.orders(self.user["id"])
            if rows:
                r=rows[0]; self.order={"code":r["order_code"],"total":r["total"],"restaurant":r["restaurant"],"status":r["status"]}
            else:
                self.title("Live Tracking","Place an order first.")
                self.button(self.body,"Order Food",self.show_menu,width=18).pack(pady=50); return
        self.title("Live Order Tracking",f"Order #{self.order['code']} • {self.order['restaurant']}")
        hero=tk.Frame(self.body,bg=DARK,height=90); hero.pack(fill="x",padx=42,pady=3); hero.pack_propagate(False)
        tk.Label(hero,text="CURRENT STATUS",bg=DARK,fg="#B8FFF5",font=(FONT,8,"bold")).pack(anchor="w",padx=22,pady=(14,2))
        tk.Label(hero,text=self.statuses[self.order["status"]][0],bg=DARK,fg=WHITE,font=(FONT,22,"bold")).pack(anchor="w",padx=22)
        main=tk.Frame(self.body,bg=BG); main.pack(fill="both",expand=True,padx=42,pady=12)
        timeline=self.card(main); timeline.pack(side="left",fill="both",expand=True,padx=(0,12))
        tk.Label(timeline,text="Delivery Journey",bg=WHITE,fg=TEXT,font=(FONT,15,"bold")).pack(anchor="w",padx=22,pady=18)
        for i,(title,desc,icon) in enumerate(self.statuses):
            done=i<self.order["status"]; active=i==self.order["status"]
            row=tk.Frame(timeline,bg=WHITE,height=62); row.pack(fill="x",padx=25); row.pack_propagate(False)
            bg=GREEN if done else TEAL if active else "#E7EFED"; fg=WHITE if done or active else MUTED
            tk.Label(row,text="✓" if done else icon if active else str(i+1),bg=bg,fg=fg,
                     font=(EMOJI_FONT,11,"bold"),width=3).pack(side="left",pady=9)
            tx=tk.Frame(row,bg=WHITE); tx.pack(side="left",padx=12)
            tk.Label(tx,text=title,bg=WHITE,fg=DARK if done or active else MUTED,font=(FONT,10,"bold")).pack(anchor="w",pady=(8,0))
            tk.Label(tx,text=desc,bg=WHITE,fg=MUTED,font=(FONT,8)).pack(anchor="w")
        side=self.card(main); side.pack(side="right",fill="y"); side.config(width=330); side.pack_propagate(False)
        tk.Label(side,text="Order Details",bg=WHITE,fg=TEXT,font=(FONT,15,"bold")).pack(anchor="w",padx=20,pady=18)
        for l,v in [("Order ID",self.order["code"]),("Restaurant",self.order["restaurant"]),("Amount",self.money(self.order["total"]))]:
            tk.Label(side,text=l,bg=WHITE,fg=MUTED,font=(FONT,8,"bold")).pack(anchor="w",padx=20,pady=(4,0))
            tk.Label(side,text=v,bg=WHITE,fg=TEXT,font=(FONT,9,"bold")).pack(anchor="w",padx=20,pady=(1,5))
        if self.order["status"]<5:
            self.button(side,"Next Demo Status →",self.next_status,width=25).pack(pady=18)
            tk.Label(side,text="Demo mode: press Next Status to simulate the delivery journey.",
                     bg=LIGHT,fg=DARK,font=(FONT,8),wraplength=270,justify="left",pady=9).pack(fill="x",padx=20)
        else:
            tk.Label(side,text="✓ Delivered successfully",bg="#DCFCE7",fg=GREEN,font=(FONT,10,"bold"),pady=10).pack(fill="x",padx=20,pady=18)

    def next_status(self):
        if self.order["status"]<5:
            self.order["status"]+=1
            self.db.conn.execute("UPDATE orders SET status=? WHERE order_code=?",(self.order["status"],self.order["code"]))
            self.db.conn.commit()
            self.show_tracking()
            if self.order["status"]==5: messagebox.showinfo("Delivered","Your FoodFlow order has been delivered!")

    # ----------------------------- ORDER HISTORY -----------------------------
    def show_orders(self):
        self.clear(); self.title("Order History","Every completed order is saved in your local database.")
        rows=self.db.orders(self.user["id"])
        if not rows:
            box=self.card(self.body); box.pack(fill="x",padx=80,pady=50,ipady=35)
            tk.Label(box,text="📦",bg=WHITE,font=(EMOJI_FONT,40)).pack()
            tk.Label(box,text="No orders yet",bg=WHITE,fg=TEXT,font=(FONT,18,"bold")).pack(pady=5)
            self.button(box,"Start Ordering",self.show_menu,width=18).pack(pady=12); return
        for r in rows[:12]:
            box=self.card(self.body); box.pack(fill="x",padx=42,pady=5)
            tk.Label(box,text="🧾",bg=LIGHT,font=(EMOJI_FONT,22),width=3).pack(side="left",padx=12,pady=10)
            info=tk.Frame(box,bg=WHITE); info.pack(side="left",fill="both",expand=True,pady=10)
            tk.Label(info,text=f"{r['restaurant']}  •  {r['order_code']}",bg=WHITE,fg=TEXT,font=(FONT,10,"bold")).pack(anchor="w")
            tk.Label(info,text=r["items"],bg=WHITE,fg=MUTED,font=(FONT,8),wraplength=650,justify="left").pack(anchor="w",pady=2)
            tk.Label(info,text=datetime.fromisoformat(r["created_at"]).strftime("%d %b %Y • %I:%M %p"),
                     bg=WHITE,fg=MUTED,font=(FONT,8)).pack(anchor="w")
            status=self.statuses[r["status"]][0]
            tk.Label(box,text=status,bg=LIGHT if r["status"]<5 else "#DCFCE7",fg=DARK if r["status"]<5 else GREEN,
                     font=(FONT,8,"bold"),padx=10,pady=6).pack(side="right",padx=12)
            tk.Label(box,text=self.money(r["total"]),bg=WHITE,fg=TEXT,font=(FONT,12,"bold")).pack(side="right",padx=12)

    # ----------------------------- PROFILE -----------------------------
    def show_profile(self):
        self.clear(); self.title("My Profile","Your basic details are stored locally for this demo.")
        box=self.card(self.body); box.pack(fill="x",padx=180,pady=20,ipady=20)
        tk.Label(box,text="👤",bg=WHITE,font=(EMOJI_FONT,40)).pack(pady=8)
        address=self.user["address"] or "Not added yet — address will be requested at checkout."
        for l,v in [("Name",self.user["name"]),("Mobile",self.user["phone"]),("Address",address)]:
            tk.Label(box,text=l,bg=WHITE,fg=MUTED,font=(FONT,8,"bold")).pack(anchor="w",padx=45,pady=(8,0))
            tk.Label(box,text=v,bg=WHITE,fg=TEXT,font=(FONT,11,"bold")).pack(anchor="w",padx=45,pady=(2,4))
        self.button(box,"Logout",self.logout,bg=RED,width=18).pack(pady=18)

    def logout(self):
        self.user=None; self.cart.clear(); self.favorites=set(); self.order=None
        self.refresh_nav(); self.show_login()

# ----------------------------- RUN -----------------------------
if __name__ == "__main__":
    root=tk.Tk()
    app=FoodFlow(root)
    root.protocol("WM_DELETE_WINDOW",lambda:(app.db.close(),root.destroy()))
    root.mainloop()