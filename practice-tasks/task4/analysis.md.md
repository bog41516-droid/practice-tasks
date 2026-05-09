# Анализ WEB-приложений

## Популярные архитектуры
- ASP.NET Core (C#)
- Spring Boot (Java)
- Django (Python)
- Node.js Express

## Для компании, использующей Delphi + MS SQL
Рекомендуется использовать **WebBroker** (ISAPI) для создания REST API, развёртывание на IIS.

## Пример эндпоинта на Delphi
```pascal
procedure TWebModule1.GetProducts(Sender: TObject; Request: TWebRequest; Response: TWebResponse; var Handled: Boolean);
var
  conn: TADOConnection;
  qry: TADOQuery;
  json: string;
begin
  conn := TADOConnection.Create(nil);
  try
    conn.ConnectionString := 'Provider=SQLOLEDB;Data Source=localhost;Initial Catalog=TourismDB;Integrated Security=SSPI';
    conn.Open;
    qry := TADOQuery.Create(nil);
    try
      qry.Connection := conn;
      qry.SQL.Text := 'SELECT * FROM Products FOR JSON PATH';
      qry.Open;
      json := qry.Fields[0].AsString;
      Response.Content := json;
      Response.ContentType := 'application/json';
    finally
      qry.Free;
    end;
  finally
    conn.Free;
  end;
end;