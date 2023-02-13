import express from "express";
import { Request, Response } from "express";

const app = express();

app.get("/", (_req: Request, res: Response) => {
  res.end("<h1>Hello Node</h1>");
});

app.listen(81, () => console.log(`Node initialized with port: 81`));
