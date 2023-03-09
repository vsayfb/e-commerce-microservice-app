import express from "express";
import { Request, Response } from "express";
import { Kafka } from "kafkajs";

const app = express();

const kafka = new Kafka({
  clientId: "my-app",
  brokers: ["kafka:9092"],
});

const producer = kafka.producer({});
const consumer = kafka.consumer({ groupId: "test-group" });

const consume = async () => {
  await consumer.connect();

  await consumer.subscribe({ topic: "new_customer", fromBeginning: true });

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      console.log(message.value.toString());
    },
  });
};

consume();

app.get("/:name", async (req: Request, res: Response) => {
  await producer.connect();

  await producer.send({
    topic: "new_product",
    messages: [{ value: Buffer.from(req.params.name) }],
  });

  res.end(req.params.name);
});

app.listen(81, () => console.log(`Node initialized with port: 81`));
