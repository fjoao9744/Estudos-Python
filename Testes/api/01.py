from supabase import create_client

# Substitua pelos valores corretos
url = "https://jjuogzrclyvjcctbiqpq.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpqdW9nenJjbHl2amNjdGJpcXBxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyNzI5MzQxNiwiZXhwIjoyMDQyODY5NDE2fQ.BFCy3drXWPNZCFs_TAM4X3awqLG_Us0IMlN8holWe1U"

supabase = create_client(url, key)

# Exemplo de operação
response = supabase.table('smogon').select('*').execute()
data = supabase.table('tabela 1').select('*').execute()

print(response)
print(data)
