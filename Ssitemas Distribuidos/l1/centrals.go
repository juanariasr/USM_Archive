package main

import (
	"fmt"
	"math"
	"math/rand"
	"net"
    "encoding/json"
	"sync"
)

type Message struct {
    Tresure int `json:"tresure"`
    Captain string `json:"captain"`
    Planet string `json:"planet"`
}

func get_planet_treasures() map[string]int {
    max_tresures := 15
    base_leter := byte('A')
    planets := make(map[string]int)
    n_leters := 6

    for i := 0; i < n_leters; i++ {
        planets[string(base_leter + byte(i))] = rand.Intn(max_tresures)
    }

    return planets
}

func central(planetas map[string]int, wg *sync.WaitGroup) {
	defer wg.Done()
	s, err := net.Listen("tcp", ":8080")
	if err != nil {
		fmt.Println(err)
		return
	}

	for {
		conn, err := s.Accept()
		if err != nil {
			fmt.Println(err)
			continue
		}

        handleSolicitude(conn, planetas)
	}
}


func handleSolicitude(conn net.Conn, planetas map[string]int) {
	defer conn.Close()

    var msg Message
    err := json.NewDecoder(conn).Decode(&msg)
    if err != nil {
        fmt.Println("Error al decodificar el mensaje", err)
    }

	fmt.Printf("Recepcion de solicitud desde el Planeta P%s, del capitan %s \n", msg.Planet, msg.Captain)

    aux := math.Inf(1)
    min_planeta := ""
    for planeta, botin := range planetas {
        if float64(botin) < aux {
            aux = float64(botin)
            min_planeta = planeta
        }
    }
    planetas[min_planeta] += msg.Tresure

	fmt.Printf("Botín asignado al planeta P%s, cantidad actual: %d\n", min_planeta, planetas[min_planeta])
    fmt.Println("Botin Planetas: ", planetas)
}


func main() {

    // Crear los planetas y asignarls los tesoros
    planetas := get_planet_treasures()
    fmt.Println("Tesoros planetas: ", planetas)

    task_counter := 5
    var wg sync.WaitGroup
    for i:=0; i<task_counter; i++ {
		wg.Add(1)
		go central(planetas, &wg)
		wg.Wait()
	}
}
