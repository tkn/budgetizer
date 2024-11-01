import streamlit as st
from st_supabase_connection import SupabaseConnection, execute_query

# Initialize connection.
conn = st.connection("supabase",type=SupabaseConnection)

# Perform query.
rows = execute_query(conn.table("budgets").select("*"))

st.write(rows)

# Print results.
for row in rows.data:
    st.write(f"{row['name']} has a :{row['year']}:")