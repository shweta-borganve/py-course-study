# Project 9: Inventory Management System

**Difficulty:** ⭐⭐⭐⭐ Medium-Hard  
**Real-world Use:** Store management, warehouse operations, e-commerce

## Project Overview

Build an **Inventory Management System** for a store:
- Track product inventory
- Manage stock levels
- Purchase orders and receiving
- Sales tracking
- Low stock alerts
- Supplier management
- Reports and analytics
- Barcode/SKU tracking

## Features to Implement

1. **Product Management**:
   - Add/update/delete products
   - Store: SKU, name, category, description, price
   - Track quantity on hand
   - Set minimum/maximum stock levels
   - Supplier information

2. **Stock Management**:
   - Receive stock
   - Track stock movements
   - Transfer between locations
   - Write off damaged/expired items
   - Cycle counting

3. **Sales**:
   - Process sales (decrease stock)
   - Return handling (increase stock)
   - Automatic stock updates
   - Track sales history

4. **Purchasing**:
   - Create purchase orders
   - Track delivery status
   - Supplier management
   - Reorder quantities

5. **Alerts & Notifications**:
   - Low stock alerts
   - Overstocked alerts
   - Expiring products (if tracking dates)
   - Slow-moving items

6. **Reporting**:
   - Stock levels report
   - Sales reports
   - Purchase orders report
   - Supplier performance
   - Inventory turnover
   - Valuation report (total inventory value)

7. **Categories & Organization**:
   - Organize products by category
   - Multiple warehouses/locations
   - Shelf location tracking

8. **Analytics**:
   - Most sold products
   - Slow-moving inventory
   - Inventory value
   - Stock turnover rate

## Technologies/Concepts Needed
- Complex data structures
- File I/O (CSV, JSON)
- Mathematical calculations
- Sorting and filtering
- Date/time operations
- Business logic
- Reporting

## Step-by-Step Guidance

### Step 1: Design Data Structures
```python
products = [
    {
        "id": 1,
        "sku": "PROD001",
        "name": "Laptop",
        "category": "Electronics",
        "description": "Dell XPS 15",
        "unit_price": 1299.99,
        "quantity_on_hand": 15,
        "min_quantity": 5,
        "max_quantity": 50,
        "supplier_id": 1,
        "reorder_quantity": 10,
        "location": "A-1-3",  # Aisle-Shelf-Bin
        "created_date": "2025-01-01",
        "last_restocked": "2025-02-08"
    }
]

suppliers = [
    {
        "id": 1,
        "name": "Tech Wholesale Co",
        "contact_person": "John Smith",
        "phone": "555-1234",
        "email": "sales@techwholesale.com",
        "address": "123 Business Park",
        "lead_time_days": 7,
        "rating": 4.5
    }
]

sales = [
    {
        "id": 1,
        "date": "2025-02-09",
        "product_id": 1,
        "quantity": 2,
        "unit_price": 1299.99,
        "total": 2599.98,
        "customer": "XYZ Corp",
        "notes": "Bulk order"
    }
]

purchase_orders = [
    {
        "id": 1,
        "date": "2025-02-08",
        "supplier_id": 1,
        "items": [
            {
                "product_id": 1,
                "quantity": 20,
                "unit_price": 1000.00
            }
        ],
        "status": "pending",  # pending, received, partial
        "expected_delivery": "2025-02-15",
        "total": 20000.00
    }
]

stock_movements = [
    {
        "id": 1,
        "date": "2025-02-09 14:30",
        "product_id": 1,
        "movement_type": "sale",  # sale, receive, return, loss
        "quantity": -2,
        "before_qty": 15,
        "after_qty": 13,
        "reason": "Sale",
        "reference": "Sale-001"
    }
]
```

### Step 2: Create Core Functions
- `add_product(sku, name, category, price, supplier_id)`
- `update_stock(product_id, quantity_change, reason)`
- `record_sale(product_id, quantity)`
- `process_return(product_id, quantity)`
- `create_purchase_order(supplier_id, items)`
- `receive_shipment(po_id, received_items)`
- `get_low_stock_items()`
- `get_overstocked_items()`
- `get_inventory_value()`
- `generate_sales_report(start_date, end_date)`
- `generate_inventory_report()`

### Step 3: Build Menu System
```
=== Inventory Management System ===
1. Add Product
2. View Products
3. Record Sale
4. Process Return
5. Create Purchase Order
6. Receive Shipment
7. Update Stock (Adjust)
8. Manage Suppliers
9. View Alerts (Low Stock, Overstock)
10. Generate Reports
11. Analytics
12. Exit
```

### Step 4: Alert System
```python
def check_alerts():
    alerts = []
    
    for product in products:
        # Low stock alert
        if product["quantity_on_hand"] < product["min_quantity"]:
            alerts.append({
                "type": "LOW_STOCK",
                "product": product["name"],
                "current": product["quantity_on_hand"],
                "minimum": product["min_quantity"]
            })
        
        # Overstock alert
        if product["quantity_on_hand"] > product["max_quantity"]:
            alerts.append({
                "type": "OVERSTOCK",
                "product": product["name"],
                "current": product["quantity_on_hand"],
                "maximum": product["max_quantity"]
            })
    
    return alerts
```

## Example Usage

```
Choose option: 1
Add new product:
SKU: PROD001
Name: Wireless Mouse
Category: Electronics
Unit Price: 25.99
Supplier: Tech Wholesale Co
Min Quantity: 10
Max Quantity: 100
✓ Product added!

Choose option: 3
Record Sale:
Product: Wireless Mouse
Quantity: 5
Sale Price: $25.99 each
Total: $129.95
✓ Sale recorded! (Stock: 45 → 40)

Choose option: 9
=== Current Alerts ===
🔴 LOW STOCK: USB Cable (15 units, minimum 20)
🔴 LOW STOCK: Keyboard (8 units, minimum 10)
🟡 OVERSTOCK: Monitor (120 units, maximum 100)
Recommendation: Create purchase orders for low stock items

Choose option: 10
Generate Report:
1. Inventory Report
2. Sales Report
3. Purchase Orders Report
4. Supplier Performance
Choice: 1

=== Inventory Report (Feb 9, 2025) ===
Total Products: 45
Total Quantity: 2,345 units
Inventory Value: $125,450.75

Stock Status:
- Optimal: 35 products
- Low Stock: 8 products
- Overstock: 2 products

Top 10 Products by Quantity:
1. USB Cable - 450 units - $4,495.50
2. Mouse Pad - 380 units - $1,900.00
3. Keyboard - 290 units - $7,250.00
...

Choose option: 11
=== Analytics ===
Best Selling Products (This Month):
1. Laptop - 8 units sold - $10,399.92
2. Monitor - 15 units sold - $3,974.85
3. Keyboard - 22 units sold - $1,871.78

Slowest Moving Products (Not sold in 30 days):
1. Graphics Card - 3 units
2. SSD - 5 units
3. RAM - 2 units

Inventory Turnover Rate: 2.3 (Good)
Average Stock Level: 52 units
Inventory Value Trend: ↑ 5% increase
```

## Real-World Enhancement Ideas
1. **Barcode/QR Scanning**: Scan items for quick updates
2. **Multi-location**: Track inventory across multiple warehouses
3. **Expiry Date Tracking**: Manage expiring products
4. **Cost Tracking**: Track product cost vs selling price
5. **Forecasting**: Predict demand and suggest orders
6. **Supplier Comparison**: Compare prices and lead times
7. **Backorder Management**: Track items on backorder
8. **Cycle Counting**: Physical inventory verification
9. **Mobile App**: Access from warehouse floor
10. **Integration**: Connect to POS system
11. **Lot/Serial Tracking**: Track specific batches
12. **Kitting**: Bundle products together

## Grading Criteria
- ✅ Can add and manage products
- ✅ Stock tracking is accurate
- ✅ Sales/returns process correctly
- ✅ Alerts are triggered at right thresholds
- ✅ Purchase orders work
- ✅ Reports are accurate and useful
- ✅ Data persists between sessions
- ✅ Mathematical calculations correct
- ✅ User interface is intuitive
- ✅ Can handle multiple products efficiently

## Tips for Implementation
- Use unique IDs for tracking
- Maintain stock movement history
- Always validate quantities (no negative stock)
- Implement soft deletes (mark as deleted, don't remove)
- Create audit trails for stock changes
- Use clear status indicators (color coding in reports)
