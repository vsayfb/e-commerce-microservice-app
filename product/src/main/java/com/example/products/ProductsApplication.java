package com.example.products;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class ProductsApplication {

    @Autowired
    private KafkaTemplate<String, String> kafkaTemplate;

    public static void main(String[] args) {
        SpringApplication.run(ProductsApplication.class, args);
    }


    @GetMapping(value = "/")
    public String hello() {
        return "Hello Java";
    }

    public void sendMessage(String msg) {
        kafkaTemplate.send("add_to_basket", msg);
    }

    @KafkaListener(topics = "new_product", groupId = "java-group")
    public void listen(String message) {
        System.out.println("Received Message in topic - new_product " + message);

        sendMessage("Hello from Spring Boot, " + message);

    }

}

