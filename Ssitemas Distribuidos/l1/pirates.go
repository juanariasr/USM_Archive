package main

import (
	"encoding/json"
	"fmt"
	"math/rand"
	"net"
	"os"
	"strconv"
	"sync"
)

type Message struct {
    Tresure int `json:"tresure"`
    Captain string `json:"captain"`
    Planet string `json:"planet"`
}

// ===== Funciones Piratas =====
func get_random_planet() string {
    base_leter := byte('A')
    n_leters := 6
    random_leter := int(base_leter) + rand.Intn(n_leters)
    return string(rune(random_leter))
}

func find_tresure(wg *sync.WaitGroup) {
	defer wg.Done()
	c, err := net.Dial("tcp", ":8080")
	if err != nil {
		fmt.Println(err)
		return
	}
    max_tresures := 15
    msg := Message {
        Tresure: rand.Intn(max_tresures),
        Captain: "C" + strconv.Itoa(rand.Intn(3) + 1),
        Planet: get_random_planet(),
    }

    jsonData, err := json.Marshal(msg)
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Printf("Capitan %s encontro un botin de %d en el Planeta P%s, enviando solicitud de asignacion\n", msg.Captain, msg.Tresure, msg.Planet)

	_, err = c.Write(jsonData)
    if err != nil {
        fmt.Println(err)
    }
	c.Close()
}

func main(){
    // Conectarse al servidor TCP en el puerto 8080
    conn, err := net.Dial("tcp", "localhost:8080")
    if err != nil {
        fmt.Println(err)
        os.Exit(1)
    }
    defer conn.Close()

    var wg sync.WaitGroup
    task_counter := 5
    wg.Add(task_counter)

    for i:=0; i<task_counter; i++ {
        go find_tresure(&wg)
    }
    wg.Wait()
    fmt.Println("Los capitanes dejaron de buscar tesoros")
}
