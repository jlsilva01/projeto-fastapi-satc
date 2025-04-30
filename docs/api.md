# API v1

Base path: `/api/v1`

## Endpoints

### GET `/items`
- Lista todos os itens  
- **Resposta**: `200 OK`  
  ```json
  [{ "id":1, "name":"Foo", "description":"Bar"}]
  ```

### POST `/items`
- Cria um novo item  
- **Body**:  
  ```json
  { "id":2, "name":"Baz", "description":"Qux" }
  ```
- **Resposta**: `201 Created` retorna o item criado  

### GET `/items/{item_id}`
- Obtém um único item  
- **Parâmetro**: `item_id`  
- **Resposta**: `200 OK` ou `404 Not Found`

### PUT `/items/{item_id}`
- Atualiza um item  
- **Body**: objeto completo  
- **Resposta**: `200 OK` ou `404 Not Found`

### DELETE `/items/{item_id}`
- Remove um item  
- **Resposta**: `204 No Content` ou `404 Not Found`  
