# 第 4 章：變數與資料型別 — 完整教學

本章深入介紹 Python 的變數概念、四大基本資料型別，以及型別轉換。透過逐步教程，你將學會如何正確宣告與使用變數。

---

## 目錄

1. [什麼是變數](#1-什麼是變數)
2. [變數的命名規則](#2-變數的命名規則)
3. [資料型別詳解](#3-資料型別詳解)
4. [型別檢查與轉換](#4-型別檢查與轉換)
5. [逐步教程](#5-逐步教程)

---

## 1. 什麼是變數

### 概念說明

**變數**（Variable）是程式中用來存放資料的「容器」或「標籤」。你可以把變數想像成一個盒子：
- 盒子有名字（變數名稱）
- 盒子裡可以放東西（資料值）
- 盒子裡的東西可以隨時更換（重新賦值）

### Python 的特性：動態型別

Python 是**動態型別**語言，代表：
- 不需要事先宣告變數型別
- 變數可以隨時被賦予不同型別的值
- 型別由賦值時的值自動決定

```python
# 同一變數可存放不同型別
x = 10       # x 現在是整數
x = "hello"  # x 現在是字串
x = 3.14     # x 現在是浮點數
```

### 變數的宣告與賦值

Python 使用 `=` 進行賦值（assignment）：

```python
變數名稱 = 值
```

- **左邊**：變數名稱
- **右邊**：要存入的值（可以是字面量、表達式或另一個變數）

---

## 2. 變數的命名規則

### 合法規則

| 規則 | 說明 |
|------|------|
| 可用字元 | 英文字母（a-z, A-Z）、數字（0-9）、底線（_） |
| 開頭限制 | **不可**以數字開頭；必須是字母或底線 |
| 區分大小寫 | `name` 與 `Name` 是不同變數 |

### 合法與非法範例

```python
# ✅ 合法
name = "Alice"
user_name = "Bob"
_age = 25
x1 = 10
MAX_VALUE = 100

# ❌ 非法
1name = "test"      # 數字開頭
user-name = "John"  # 含連字號
class = "A"         # 保留字不可作為變數名
```

### 命名慣例（PEP 8）

| 風格 | 適用情境 | 範例 |
|------|----------|------|
| 小寫 + 底線 | 變數、函式 | `user_name`, `total_count` |
| 首字大寫 | 類別 | `Person`, `BankAccount` |
| 全大寫 + 底線 | 常數 | `MAX_SIZE`, `PI` |

### 避免使用 Python 保留字

常見保留字：`if`, `else`, `for`, `while`, `def`, `class`, `return`, `import`, `True`, `False`, `None` 等。

---

## 3. 資料型別詳解

### 3.1 整數（int）

**用途**：儲存整數，無小數點。

| 項目 | 說明 |
|------|------|
| 型別名稱 | `int` |
| 範圍 | 幾乎無限制（受記憶體影響） |
|  literal 範例 | `0`, `42`, `-100`, `1_000_000` |

```python
age = 25
count = -10
big_number = 1_000_000  # 下底線可當千分位，不影響數值
```

### 3.2 浮點數（float）

**用途**：儲存有小數的數值。

| 項目 | 說明 |
|------|------|
| 型別名稱 | `float` |
| 表示方式 | 小數點或科學記號 |
| literal 範例 | `3.14`, `0.5`, `2e3` (= 2000.0) |

```python
price = 99.9
temperature = -3.5
scientific = 1.5e6  # 1.5 × 10⁶ = 1500000.0
```

### 3.3 布林（bool）

**用途**：表示真（True）或假（False），用於條件判斷。

| 項目 | 說明 |
|------|------|
| 型別名稱 | `bool` |
| 僅有兩值 | `True`、`False`（首字大寫） |
| 來源 | 比較運算、邏輯運算、直接賦值 |

```python
is_active = True
is_empty = False
result = (10 > 5)   # result 為 True
```

### 3.4 字串（str）

**用途**：儲存文字，由字元組成。

| 項目 | 說明 |
|------|------|
| 型別名稱 | `str` |
| 表示方式 | 單引號、雙引號、三引號 |
| 特性 | 不可變（immutable） |

```python
name = "Alice"
message = 'Hello, World!'
multi_line = """這是一段
可以換行的
多行字串"""
```

---

## 4. 型別檢查與轉換

### 使用 type() 檢查型別

```python
x = 42
print(type(x))        # <class 'int'>

y = 3.14
print(type(y))        # <class 'float'>

z = "hello"
print(type(z))        # <class 'str'>
```

### 型別轉換函式

| 函式 | 轉換目標 | 範例 |
|------|----------|------|
| `int()` | 整數 | `int("42")` → 42 |
| `float()` | 浮點數 | `float("3.14")` → 3.14 |
| `str()` | 字串 | `str(100)` → "100" |
| `bool()` | 布林 | `bool(1)` → True |

```python
# 字串轉數值
num_str = "123"
num_int = int(num_str)    # 123
num_float = float("3.14") # 3.14

# 數值轉字串
age = 25
age_str = str(25)        # "25"

# 數值轉布林（0 為 False，非 0 為 True）
bool(0)   # False
bool(1)   # True
bool(-1)  # True
```

### 轉換注意事項

- `int("3.14")` 會**錯誤**，需先 `float("3.14")` 再 `int()`
- `int(3.9)` 會**截斷**小數 → 3（非四捨五入）

---

## 5. 逐步教程

### 步驟 1：建立新檔案

1. 在 `Basic` 資料夾中建立 `04-variables-data-types.py`
2. 或開啟既有的該檔案

---

### 步驟 2：建立第一個變數

在檔案中輸入：

```python
# 步驟 2：建立變數
name = "Python 學習者"
print(name)
```

執行後預期輸出：`Python 學習者`

---

### 步驟 3：嘗試不同資料型別

新增以下程式碼：

```python
# 步驟 3：四種基本型別
age = 25                    # int
height = 168.5              # float
is_student = True           # bool
course = "Python 基礎"      # str

print("年齡:", age, "型別:", type(age))
print("身高:", height, "型別:", type(height))
print("是否為學生:", is_student, "型別:", type(is_student))
print("課程:", course, "型別:", type(course))
```

執行後預期看到各變數的值與型別。

---

### 步驟 4：變數重新賦值

```python
# 步驟 4：變數可重新賦值
score = 85
print("原始分數:", score)

score = 92  # 重新賦值
print("更新後分數:", score)

# 動態型別：同一變數可改變型別
score = "優等"
print("字串型別:", score, type(score))
```

---

### 步驟 5：多變數賦值

```python
# 步驟 5：一次賦值多個變數
x = y = z = 0
print("x={}, y={}, z={}".format(x, y, z))

# 同時賦予不同值
a, b, c = 1, 2, 3
print("a={}, b={}, c={}".format(a, b, c))
```

---

### 步驟 6：型別轉換練習

```python
# 步驟 6：型別轉換
user_input = "100"          # input() 回傳字串
num = int(user_input)       # 轉成整數
print("轉換後數值:", num + 50)  # 150

# 數值轉字串
price = 99.9
price_str = str(price)
print("價格字串:", price_str, "| 型別:", type(price_str))
```

---

### 步驟 7：實作小程式 — 簡易個人資訊

將以上概念整合為一個小程式：

```python
# 步驟 7：整合練習 — 個人資訊
name = "小明"
age = 18
height = 175.5
is_male = True

print("=== 個人資訊 ===")
print(f"姓名: {name}")
print(f"年齡: {age} 歲")
print(f"身高: {height} 公分")
print(f"性別: {'男' if is_male else '女'}")
print(f"\n變數型別檢查:")
print(f"  name: {type(name).__name__}")
print(f"  age: {type(age).__name__}")
print(f"  height: {type(height).__name__}")
print(f"  is_male: {type(is_male).__name__}")
```

---

### 步驟 8：進階練習（選做）

1. **變數交換**：不透過第三變數，交換 `a` 與 `b` 的值
   ```python
   a, b = 10, 20
   a, b = b, a  # Python 的簡潔寫法
   print(a, b)  # 20 10
   ```

2. **型別轉換陷阱**：嘗試 `int("3.14")` 觀察錯誤，再用 `int(float("3.14"))` 修正

3. **命名練習**：將 `user_name`、`user_age`、`is_valid` 等變數賦值並印出

---

## 學習檢查清單

完成本章後，請確認：

- [ ] 能說明什麼是變數以及 Python 的動態型別
- [ ] 能正確命名變數（合法字元、不可數字開頭）
- [ ] 能辨識並使用 `int`、`float`、`bool`、`str`
- [ ] 能使用 `type()` 檢查變數型別
- [ ] 能使用 `int()`、`float()`、`str()` 進行型別轉換
- [ ] 能完成步驟 7 的個人資訊程式並理解每個變數的型別

---

## 常見錯誤

| 錯誤 | 原因 | 解法 |
|------|------|------|
| `NameError: name 'x' is not defined` | 使用未賦值的變數 | 先賦值再使用 |
| `SyntaxError: invalid syntax` | 變數名以數字開頭或使用保留字 | 改用合法變數名 |
| `ValueError: invalid literal for int()` | 字串無法轉成整數（如 `"3.14"`） | 先轉 `float` 再轉 `int` |

---

*本章對應 `04-variables-data-types.py`，建議邊閱讀邊在該檔案中實作。*
