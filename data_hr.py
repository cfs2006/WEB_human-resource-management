from faker import Faker
import mysql.connector
import random
import bcrypt

fake = Faker('vi_VN')

# Kết nối DB
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="quanlynhansucongviec"  
)
cursor = conn.cursor()

# TẠO USERS GIẢ (50 người)

print("Đang tạo users...")

for i in range(50):
    username      = fake.user_name() + str(random.randint(1, 999))
    email         = fake.email()
    password      = "123456"
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    status        = random.choice([0, 1])

    cursor.execute("""
        INSERT IGNORE INTO users (username, email, password_hash, status)
        VALUES (%s, %s, %s, %s)
    """, (username, email, password_hash, status))

conn.commit()
print("Tạo xong 50 users!")

# GÁN ROLE CHO USERS

print("Đang gán roles...")

cursor.execute("SELECT id FROM users WHERE id > 1")
users = cursor.fetchall()

for user in users:
    user_id = user[0]
    role_id = random.choice([1, 2])  # 1=ADMIN, 2=User

    cursor.execute("""
        INSERT IGNORE INTO user_roles (user_id, role_id)
        VALUES (%s, %s)
    """, (user_id, role_id))

conn.commit()
print("Gán xong roles!")

# TẠO SESSIONS GIẢ

print("Đang tạo sessions...")

cursor.execute("SELECT id FROM users")
all_users = cursor.fetchall()

for user in all_users[:20]:  # 20 sessions
    session_id = fake.uuid4()
    user_id    = user[0]
    expires_at = fake.future_datetime(end_date='+30d')

    cursor.execute("""
        INSERT INTO sessions (session_id, user_id, expires_at)
        VALUES (%s, %s, %s)
    """, (session_id, user_id, expires_at))

conn.commit()
print("Tạo xong sessions!")

cursor.close()
conn.close()
print("Hoàn thành!")
