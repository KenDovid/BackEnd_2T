// routes/items.routes.js
import { Router } from "express";
import {
    getItems,
    getItem,
    createItem,
    updateItem,
    patchItem,
    deleteItem
} from "../controllers/items.controller.js";

const router = Router();

router.get("/items", getItems);
router.get("/items/:id", getItem);
router.post("/items", createItem);
router.put("/items/:id", updateItem);
router.patch("/items/:id", patchItem);
router.delete("/items/:id", deleteItem);

export default router;
